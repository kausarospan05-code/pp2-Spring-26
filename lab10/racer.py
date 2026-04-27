import pygame, sys
from pygame.locals import *
import random, time

# Initializing 
pygame.init()

# Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

# Colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Other Variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((400,600))
pygame.display.set_caption("Racer")

class Enemy(pygame.sprite.Sprite): #class Coin(pygame.sprite.Sprite):
                                   #"Мұнда мен монета үшін жеке класс аштым. Ол Enemy класына ұқсас, бірақ мұның мақсаты — соғысу емес, жиналу."
    def __init__(self):
        super().__init__() 
        self.image = pygame.Surface((40, 70))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0) #self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
        #"Бұл жол монетаның экранның жоғарғы жағынан кездейсоқ (random) жерден шығуын қамтамасыз етеді."

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)#x=0,y=speed 
        #0 — оңға-солға қозғалмайды, ал SPEED — тек төмен қарай жүреді деген сөз
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
#Y осі: Егер объектінің top (жоғарғы) координатасы 600-ден (экран биіктігі) асып кетсе, 
# ол экраннан шығып кетті деп есептеледі.

#Телепортация: Біз объектіні өшірмейміз, жай ғана оның координатасын қайтадан 0-ге 
# (экранның төбесіне) қоямыз және X осі бойынша жаңа кездейсоқ орын береміз. Бұл компьютер жадын үнемдейді.
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.Surface((40, 70))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0: #шарты арқылы машинаның экраннан шығып кетпеуін қадағалаймыз
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Extra Task: Adding randomly appearing coins
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def reset(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.reset()

# Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(WHITE)#DISPLAYSURF.fill(WHITE): Ескі кадрды өшіреді. (Егер өшірмесек, машинаның артында ұзын із қалып қояды)
    
    # Extra Task: Showing number of collected coins
    scores = font_small.render(f"Score: {SCORE}", True, BLACK)
    coin_count = font_small.render(f"Coins: {COINS}", True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coin_count, (300, 10))

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
#DISPLAYSURF.blit(...): Жаңа орында тұрған объектілерді экранға қайта салады
    # Collision with Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    
    # Collision with Coin
    if pygame.sprite.spritecollideany(P1, coins): #if pygame.sprite.spritecollideany(P1, coins):
#соқтығысуды тексеретін функция. Егер ойыншы (P1) мен монета (coins) түйіссе, COINS айнымалысына +1 қосылады, ал монета reset() болып жоғарыға қайта кетеді.
        COINS += 1
        C1.reset()

    pygame.display.update()
    FramePerSec.tick(FPS)