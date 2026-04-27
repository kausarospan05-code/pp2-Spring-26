import pygame
import time
import random

pygame.init()

# Constants
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)

WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20 #Тор өлшемі:Жыланның бір бөлігі мен тамақтың өлшемі. Бұл ойын алаңl анықтайды

dis = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Practice')
clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)

def show_score(score, level):
    #Экранның сол жақ жоғарғы бұрышына ұпай мен деңгейді шығаратын функция.
    value = font_style.render(f"Score: {score}  Level: {level}", True, YELLOW)
    dis.blit(value, [0, 0])

def gameLoop():
    game_over = False
    game_close = False

    x1, y1 = WIDTH / 2, HEIGHT / 2 #Жыланның бастапқы орны — экранның центрі.
    x1_change, y1_change = 0, 0 #Жыланның қозғалыс бағыты. Басында ол бір орында тұрады.

    snake_List = []
    Length_of_snake = 1
    #Жыланның денесін сақтайтын тізім және оның бастапқы ұзындығы.
    
    # Task: Levels and Speed
    speed = 10
    level = 1

    # Task: Random Food position
    foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
    #Тамақ тордың бойында (20-ға еселі нүктеде) пайда болуы үшін осы формула қолданылады.
    foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0

    while not game_over:
        while game_close == True: #Ойыншы жеңілген кезде шығатын терезе логикасы (Қайта бастау немесе шығу)
            dis.fill(BLACK)
            msg = font_style.render("Lost! Press C-Play Again or Q-Quit", True, RED)
            dis.blit(msg, [WIDTH / 6, HEIGHT / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: #Ойыншы жеңілген кезде шығатын терезе логикасы (Қайта бастау немесе шығу)
                    x1_change = -BLOCK_SIZE; y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = BLOCK_SIZE; y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -BLOCK_SIZE; x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = BLOCK_SIZE; x1_change = 0

        # Task: Checking for border collision
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True #Шекараны тексеру: Егер жылан қабырғаға тисе, game_close іске қосылады.
        
        x1 += x1_change #Жыланның жаңа координатасын есептейміз
        y1 += y1_change
        dis.fill(BLACK)
        pygame.draw.rect(dis, GREEN, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])
        
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
            #Жыланның басын тізімге қосып, егер ұзындығы асса, ескі құйрығын del арқылы өшіреміз

        # Check for self-collision
        for x in snake_List[:-1]:#Егер бас (snake_Head) дененің кез келген бөлігіне тең болса — ойын бітеді
            if x == snake_Head:
                game_close = True

        for segment in snake_List:
            pygame.draw.rect(dis, WHITE, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE])

        show_score(Length_of_snake - 1, level)
        pygame.display.update()

        # Task: Snake eats food
        if x1 == foodx and y1 == foody: #Бас пен тамақ беттессе, ұзындықты арттырып, жаңа тамақ шығарамыз
            foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
            foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
            Length_of_snake += 1
            
            # Task: Increase level and speed every 3 foods
            if (Length_of_snake - 1) % 3 == 0:
                level += 1
                speed += 2
#Әр 3 тамақ жеген сайын деңгейді (level + 1) және жылдамдықты (speed + 2) арттырамыз
        clock.tick(speed)

    pygame.quit()
    quit()

gameLoop()