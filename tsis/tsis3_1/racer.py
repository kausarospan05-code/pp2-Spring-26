import pygame
import random
import os
from persistence import load_settings

ASSETS_IMG = "assets/images"
ASSETS_SND = "assets/sound"

class Player:
    def __init__(self):
        self.lane = 1
        self.rect = pygame.Rect(0, 0, 78, 155)
        self.shield = False
        self.nitro_end = 0
        self.lives = 3
        self.image = self.load_image()

    def load_image(self):
        try:
            img = pygame.image.load(os.path.join(ASSETS_IMG, "Player.png")).convert_alpha()
            return pygame.transform.scale(img, (78, 155))
        except:
            return None

    def move_to_lane(self, lane):
        self.lane = max(0, min(2, lane))


class PowerUp:
    def __init__(self, x, y, ptype):
        self.rect = pygame.Rect(x, y, 52, 52)
        self.type = ptype
        self.spawn_time = pygame.time.get_ticks()
        self.image = self.load_image()

    def load_image(self):
        try:
            img = pygame.image.load(os.path.join(ASSETS_IMG, f"{self.type}.png")).convert_alpha()
            return pygame.transform.scale(img, (52, 52))
        except:
            return None

    def is_expired(self):
        return pygame.time.get_ticks() - self.spawn_time > 8500


class Obstacle:
    def __init__(self, lane, y, obs_type):
        self.lane = lane
        self.rect = pygame.Rect(0, y, 78, 155)
        self.type = obs_type
        self.image = self.load_image()

    def load_image(self):
        try:
            img = pygame.image.load(os.path.join(ASSETS_IMG, f"{self.type}.png")).convert_alpha()
            return pygame.transform.scale(img, (78, 155))
        except:
            return None


class RacerGame:
    def __init__(self, screen_width=800, screen_height=600):
        self.screen_w = screen_width
        self.screen_h = screen_height
        self.settings = load_settings()

        pygame.mixer.init()
        self.load_sounds()

        self.player = Player()
        self.coins = 0
        self.distance = 0
        self.score = 0
        self.speed = 6.8
        self.base_speed = 6.8
        self.obstacles = []
        self.powerups = []
        self.active_powerup = None
        self.last_spawn = 0
        self.difficulty_level = 1
        self.road_offset = 0

        # Background Music
        try:
            music_path = os.path.join(ASSETS_SND, "background.mp3")
            if os.path.exists(music_path):
                pygame.mixer.music.load(music_path)
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.4)
        except:
            pass

    def load_sounds(self):
        try:
            self.sound_crash = pygame.mixer.Sound(os.path.join(ASSETS_SND, "crash.wav"))
            self.sound_powerup = pygame.mixer.Sound(os.path.join(ASSETS_SND, "powerup.wav"))
        except:
            self.sound_crash = self.sound_powerup = None

    def update(self, keys, current_time):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player.move_to_lane(self.player.lane - 1)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.move_to_lane(self.player.lane + 1)

        self.distance += int(self.speed * 0.6)
        self.score = self.coins * 15 + self.distance // 10

        self.difficulty_level = 1 + self.distance // 2400
        self.speed = self.base_speed + self.difficulty_level * 0.65

        if current_time - self.last_spawn > max(420, 1180 - self.difficulty_level * 55):
            self.spawn_entities()
            self.last_spawn = current_time

        for obs in self.obstacles[:]:
            obs.rect.y += self.speed
            if obs.rect.y > self.screen_h + 120:
                self.obstacles.remove(obs)
            elif self.check_collision(obs):
                if self.handle_collision(obs) == "game_over":
                    return "game_over"

        for pu in self.powerups[:]:
            pu.rect.y += self.speed
            if pu.rect.y > self.screen_h + 120 or pu.is_expired():
                self.powerups.remove(pu)
            elif self.player.rect.colliderect(pu.rect):
                self.collect_powerup(pu)
                self.powerups.remove(pu)

        if self.player.nitro_end > current_time:
            self.speed = self.base_speed * 2.0

        return None

    def spawn_entities(self):
        lane = random.randint(0, 2)

        # SAFE SPAWN - машинаның үстіне зат шықпауы үшін
        if abs(lane - self.player.lane) == 0:
            lane = (self.player.lane + random.choice([-1, 1])) % 3

        # Traffic Enemy
        if random.random() < 0.63 + self.difficulty_level * 0.05:
            self.obstacles.append(Obstacle(lane, -220, "Enemy"))

        # Road Hazards
        if random.random() < 0.48 + self.difficulty_level * 0.04:
            hazard = random.choice(["Oil", "Barrier", "Pothole", "SpeedBump"])
            self.obstacles.append(Obstacle(lane, -220, hazard))

        # Power-ups (қызықты болу үшін)
        if random.random() < 0.23:
            ptype = random.choice(["Nitro", "Shield", "Repair"])
            self.powerups.append(PowerUp(lane * 200 + 98, -105, ptype))

    def check_collision(self, obs):
        return obs.lane == self.player.lane and abs(obs.rect.y - self.player.rect.y) < 125

    def handle_collision(self, obs):
        if self.player.shield:
            self.player.shield = False
            if obs in self.obstacles:
                self.obstacles.remove(obs)
            return None

        if self.sound_crash:
            self.sound_crash.play()

        if obs.type in ["Oil", "Pothole", "SpeedBump"]:
            self.speed = max(4.2, self.speed * 0.62)
            if obs in self.obstacles:
                self.obstacles.remove(obs)
        else:
            self.player.lives -= 1
            if self.player.lives <= 0:
                return "game_over"
            if obs in self.obstacles:
                self.obstacles.remove(obs)
        return None

    def collect_powerup(self, pu):
        if self.active_powerup:
            return
        if self.sound_powerup:
            self.sound_powerup.play()

        if pu.type == "Nitro":
            self.player.nitro_end = pygame.time.get_ticks() + 5000
            self.active_powerup = ("nitro", self.player.nitro_end)
        elif pu.type == "Shield":
            self.player.shield = True
            self.active_powerup = ("shield", None)
        elif pu.type == "Repair":
            self.player.lives = min(3, self.player.lives + 1)

    def draw(self, screen):
        screen.fill((20, 23, 48))
        road_width = 430
        road_x = self.screen_w // 2 - road_width // 2
        self.road_offset = (self.road_offset + self.speed * 2.1) % 115

        pygame.draw.rect(screen, (45, 50, 68), (road_x, 0, road_width, self.screen_h))

        for i in range(-4, 19):
            y = i * 115 - self.road_offset
            pygame.draw.rect(screen, (255, 240, 80), (self.screen_w//2 - 9, y, 18, 72))

        for i in range(4):
            x = road_x + i * (road_width // 3)
            pygame.draw.line(screen, (210, 210, 230), (x, 0), (x, self.screen_h), 7)

        for obs in self.obstacles:
            x = road_x + obs.lane * (road_width // 3) + 20
            if obs.image:
                screen.blit(obs.image, (x, obs.rect.y))

        for pu in self.powerups:
            x = road_x + pu.rect.x
            if pu.image:
                screen.blit(pu.image, (x, pu.rect.y))

        player_x = road_x + self.player.lane * (road_width // 3) + 20
        self.player.rect.topleft = (player_x, self.screen_h - 210)

        if self.player.image:
            screen.blit(self.player.image, self.player.rect)

        if self.player.shield:
            pygame.draw.rect(screen, (0, 255, 255), self.player.rect, width=7, border_radius=18)

        font = pygame.font.SysFont(None, 37)
        screen.blit(font.render(f"SCORE: {self.score}", True, (255, 255, 100)), (30, 22))
        screen.blit(font.render(f"DISTANCE: {self.distance//10}m", True, (200, 230, 255)), (30, 68))

        if self.active_powerup:
            name, end_time = self.active_powerup
            rem = max(0, (end_time - pygame.time.get_ticks()) // 1000)
            color = (255, 215, 0) if name == "nitro" else (0, 255, 255)
            screen.blit(font.render(f"{name.upper()} {rem}s", True, color), (self.screen_w - 270, 25))

        screen.blit(font.render(f"LIVES: {self.player.lives}", True, (255, 90, 90)), (self.screen_w - 175, 70))