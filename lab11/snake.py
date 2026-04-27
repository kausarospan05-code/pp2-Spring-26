import pygame
import time
import random

pygame.init()

# Colors
BLACK, WHITE, RED, GREEN, YELLOW = (0,0,0), (255,255,255), (213,50,80), (0,255,0), (255,255,102)

WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
dis = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 25)

def gameLoop():
    game_over = False
    game_close = False
    x1, y1 = WIDTH / 2, HEIGHT / 2
    x1_change, y1_change = 0, 0
    snake_List = []
    Length_of_snake = 1
    
    speed = 10
    
    # Food setup
    foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
    foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
    food_weight = random.choice([1, 3]) # Weights: 1 or 3
    food_timer = pygame.time.get_ticks() # Current time

    while not game_over:
        while game_close:
            dis.fill(BLACK)
            msg = font_style.render("Lost! C-Play Again, Q-Quit", True, RED)
            dis.blit(msg, [WIDTH / 6, HEIGHT / 3])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: game_over = True; game_close = False
                    if event.key == pygame.K_c: gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: x1_change = -BLOCK_SIZE; y1_change = 0
                elif event.key == pygame.K_RIGHT: x1_change = BLOCK_SIZE; y1_change = 0
                elif event.key == pygame.K_UP: y1_change = -BLOCK_SIZE; x1_change = 0
                elif event.key == pygame.K_DOWN: y1_change = BLOCK_SIZE; x1_change = 0

        # Check for food expiration (7 seconds timer)
        current_time = pygame.time.get_ticks()
        if current_time - food_timer > 7000:
            foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
            foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
            food_weight = random.choice([1, 3])
            food_timer = current_time

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0: game_close = True
        
        x1 += x1_change
        y1 += y1_change
        dis.fill(BLACK)
        
        # Draw food (Color based on weight)
        color = GREEN if food_weight == 1 else YELLOW
        pygame.draw.rect(dis, color, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])
        
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake: del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head: game_close = True

        for segment in snake_List:
            pygame.draw.rect(dis, WHITE, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            Length_of_snake += food_weight # Add based on weight
            foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
            foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
            food_weight = random.choice([1, 3])
            food_timer = pygame.time.get_ticks() # Reset timer
            
        clock.tick(speed)

    pygame.quit()
    quit()

gameLoop()