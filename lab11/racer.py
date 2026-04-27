import pygame, sys
from pygame.locals import *
import random, time

#Қолданылды pygame.time.get_ticks(). Бұл программа басталғаннан бергі уақытты есептейді.

#Если прошло 7 секунд (7000 мс) и ты не съел еду, она исчезает и появляется в другом месте (respawn)
# Initializing 
pygame.init()
#Каждые 10 жиналған монета сайын жаудың (Enemy) жылдамдығы артады. Ойын қиындай түседі
# Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()


# Colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Other Variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
ENEMY_SPEED = 5 # Separate variable for Enemy speed
SCORE = 0
COINS = 0

DISPLAYSURF = pygame.display.set_mode((400,600))
pygame.display.set_caption("Racer")
font_small = pygame.font.SysFont("Verdana", 20)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.Surface((40, 70))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, ENEMY_SPEED) # Using the dynamic ENEMY_SPEED
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.Surface((40, 70))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Randomly choose weight: 1 (Small) or 3 (Big/Gold)
        self.weight = random.choice([1, 3])
        self.image = pygame.Surface((20, 20))
        # Color based on weight
        self.image.fill(YELLOW if self.weight == 1 else (255, 165, 0)) # Yellow vs Orange
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def reset(self):
        self.weight = random.choice([1, 3])
        self.image.fill(YELLOW if self.weight == 1 else (255, 165, 0))
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.reset()

P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(WHITE)
    
    # Check for Speed Increase (Every 10 coins)
    ENEMY_SPEED = 5 + (COINS // 10)

    scores = font_small.render(f"Score: {SCORE} Coins: {COINS} Speed: {ENEMY_SPEED}", True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Collision with Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.quit()
        sys.exit()
    
    # Collision with Coin (Adding weight to total)
    if pygame.sprite.spritecollideany(P1, coins):
        COINS += C1.weight # Added coin weight
        C1.reset()

    pygame.display.update()
    FramePerSec.tick(FPS)