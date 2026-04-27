import pygame
import math
#S — Square (Квадрат)
# T — Right Triangle (Прямоугольный треугольник)
# U — Equilateral Triangle (Равносторонний треугольник)
# H — Rhombus (Ромб)


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    color = (255, 255, 255) 
    mode = 'pencil' 
    start_pos = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: mode = 'rectangle'
                if event.key == pygame.K_s: mode = 'square'
                if event.key == pygame.K_t: mode = 'right_triangle'
                if event.key == pygame.K_u: mode = 'eq_triangle'
                if event.key == pygame.K_h: mode = 'rhombus'
                if event.key == pygame.K_p: mode = 'pencil'
                
                if event.key == pygame.K_1: color = (255, 0, 0) 
                if event.key == pygame.K_2: color = (0, 255, 0) 

            if event.type == pygame.MOUSEBUTTONDOWN:
                start_pos = event.pos 
#Егер "ауыр" тамақты жесең (weight 3), жыланның ұзындығы бірден 3 блокқа өседі (Length_of_snake += food_weight).
            if event.type == pygame.MOUSEBUTTONUP:
                end_pos = event.pos
                if start_pos:
                    if mode == 'rectangle':
                        pygame.draw.rect(screen, color, (start_pos[0], start_pos[1], end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]), 2)
                    
                    elif mode == 'square':
                        side = max(abs(end_pos[0]-start_pos[0]), abs(end_pos[1]-start_pos[1]))
                        pygame.draw.rect(screen, color, (start_pos[0], start_pos[1], side, side), 2)
                    
                    elif mode == 'right_triangle':
                        points = [start_pos, (start_pos[0], end_pos[1]), end_pos]
                        pygame.draw.polygon(screen, color, points, 2)

                    elif mode == 'eq_triangle':
                        side = end_pos[0] - start_pos[0]
                        height = (math.sqrt(3)/2) * side
                        points = [start_pos, (end_pos[0], start_pos[1]), ((start_pos[0]+end_pos[0])/2, start_pos[1]-height)]
                        pygame.draw.polygon(screen, color, points, 2)
                    
                    elif mode == 'rhombus':
                        mid_x, mid_y = (start_pos[0]+end_pos[0])/2, (start_pos[1]+end_pos[1])/2
                        points = [(mid_x, start_pos[1]), (end_pos[0], mid_y), (mid_x, end_pos[1]), (start_pos[0], mid_y)]
                        pygame.draw.polygon(screen, color, points, 2)
                        
                    start_pos = None

            if event.type == pygame.MOUSEMOTION and mode == 'pencil':
                if pygame.mouse.get_pressed()[0]:
                    pygame.draw.circle(screen, color, event.pos, 2)

        pygame.display.flip()
        clock.tick(60)

main()