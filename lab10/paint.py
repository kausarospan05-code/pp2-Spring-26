import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))#окно для рисования. Размері — 640-та 480 пиксель
    clock = pygame.time.Clock()#Таймер қосамыз, чтобы картинка "не дергалась" и FPS тұрақты болсын.
    
    radius = 15 #Кистьтің қалыңдығы (размер круга)
    color = (255, 255, 255) # Start with White
    mode = 'pencil' # Modes: pencil, rectangle, circle, eraser
    #Текущий режим
    # Store points for shapes
    start_pos = None

    while True:
        pressed_keys = pygame.key.get_pressed() #Қай кнопка басылып тұрғанын тексеріп отырамыз (мысалы, Alt немесе Ctrl)
        alt_held = pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT]
        ctrl_held = pressed_keys[pygame.K_LCTRL] or pressed_keys[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#Егер "X" басылса, программа выключается
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held: return
                if event.key == pygame.K_F4 and alt_held: return
                
                # Mode selection бассақ — режимдер ауысады (Rectangle, Circle, Pencil, Eraser)
                if event.key == pygame.K_r: mode = 'rectangle'
                if event.key == pygame.K_c: mode = 'circle'
                if event.key == pygame.K_p: mode = 'pencil'
                if event.key == pygame.K_e: mode = 'eraser'
                
                # Color Selection
                if event.key == pygame.K_1: color = (255, 0, 0) # Red
                if event.key == pygame.K_2: color = (0, 255, 0) # Green
                if event.key == pygame.K_3: color = (0, 0, 255) # Blue

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mode in ['rectangle', 'circle']:
                    start_pos = event.pos #Мышканы басқан кезде біз start_pos-ты (начальные координаты) запоминаем

            if event.type == pygame.MOUSEBUTTONUP:
                if mode == 'rectangle' and start_pos:
                    end_pos = event.pos
                    width = end_pos[0] - start_pos[0]
                    height = end_pos[1] - start_pos[1]
                    pygame.draw.rect(screen, color, (start_pos[0], start_pos[1], width, height), 2)
                    start_pos = None
                elif mode == 'circle' and start_pos:
                    end_pos = event.pos
                    # Calculate radius using distance formula
                    r = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2)**0.5)
                    pygame.draw.circle(screen, color, start_pos, r, 2)
                    start_pos = None

            if event.type == pygame.MOUSEMOTION:
                if mode == 'pencil':
                    if pygame.mouse.get_pressed()[0]:
                        pygame.draw.circle(screen, color, event.pos, radius)
                elif mode == 'eraser':
                    if pygame.mouse.get_pressed()[0]:#Это тот же карандаш, только цвет черный (фонның түсі), поэтому он "өшіреді"
                        pygame.draw.circle(screen, (0, 0, 0), event.pos, radius)

        pygame.display.flip() #Все, что мы нарисовали в памяти, шығарамыз экранға
        clock.tick(60) #Ограничение по кадрам, чтобы программа "ұшпай", нормально жұмыс істеуі үшін

main()
#Controls for Paint:
# P:Pencil | R: Rectangle | C: Circle | E: Eraser
# 1, 2, 3: Change colors (Red, Green, Blue)
# For Rectangle/Circle: Click and drag