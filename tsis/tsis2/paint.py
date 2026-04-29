import pygame
from tools import get_color, draw_line_segment, draw_shape, flood_fill, save_canvas

WIDTH, HEIGHT = 900, 750
UI_HEIGHT = 100
FPS = 60

def draw_ui(screen, font, tool, color, size):
    pygame.draw.rect(screen, (240, 240, 240), (0, 0, WIDTH, UI_HEIGHT))
    lines = [
        f"Tools: P-Pen, E-Eraser, L-Line, T-Rect, C-Circle, S-Square, R-RightTri, Q-EquiTri, H-Rhombus, F-Fill, A-Text",
        f"Colors: 1-Black, 2-Red, 3-Green, 4-Blue | Size: 5-Small, 6-Med, 7-Large",
        f"Action: Ctrl+S Save, X-Clear, ESC-Exit",
        f"CURRENT: Tool [{tool.upper()}] | Color [{color.upper()}] | Size [{size}px]"
    ]
    for i, line in enumerate(lines):
        text = font.render(line, True, (50, 50, 50))
        screen.blit(text, (15, 10 + (i * 20)))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("TSIS 2 Paint")
    clock = pygame.time.Clock()

    radius, color_mode, tool = 5, 'black', 'pen'
    drawing, start_pos = False, None
    text_active, text_pos, text_value = False, None, ""

    font = pygame.font.SysFont("Verdana", 14)
    text_font = pygame.font.SysFont("Arial", 24)

    canvas = pygame.Surface((WIDTH, HEIGHT - UI_HEIGHT))
    canvas.fill((255, 255, 255))

    running = True
    while running:
        screen.fill((200, 200, 200))
        ctrl_held = pygame.key.get_pressed()[pygame.K_LCTRL] or pygame.key.get_pressed()[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s and ctrl_held:
                    save_canvas(canvas)
                elif text_active:
                    if event.key == pygame.K_RETURN:
                        canvas.blit(text_font.render(text_value, True, get_color(color_mode)), text_pos)
                        text_active = False
                    elif event.key == pygame.K_BACKSPACE: text_value = text_value[:-1]
                    elif event.key == pygame.K_ESCAPE: text_active = False
                    else: text_value += event.unicode
                else:
                    if event.key == pygame.K_ESCAPE: running = False
                    if event.key == pygame.K_x: canvas.fill((255, 255, 255))
                    
                    tools_map = {pygame.K_p:'pen', pygame.K_e:'eraser', pygame.K_l:'line', pygame.K_t:'rectangle', 
                                 pygame.K_c:'circle', pygame.K_s:'square', pygame.K_r:'right_triangle', 
                                 pygame.K_q:'equilateral_triangle', pygame.K_h:'rhombus', pygame.K_f:'fill', pygame.K_a:'text'}
                    if event.key in tools_map: tool = tools_map[event.key]
                    
                    colors_map = {pygame.K_1:'black', pygame.K_2:'red', pygame.K_3:'green', pygame.K_4:'blue'}
                    if event.key in colors_map: color_mode = colors_map[event.key]
                    
                    sizes_map = {pygame.K_5:2, pygame.K_6:5, pygame.K_7:10}
                    if event.key in sizes_map: radius = sizes_map[event.key]

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[1] >= UI_HEIGHT:
                    adj = (event.pos[0], event.pos[1] - UI_HEIGHT)
                    if tool == 'fill': flood_fill(canvas, adj, get_color(color_mode))
                    elif tool == 'text': text_active, text_pos, text_value = True, adj, ""
                    else: drawing, start_pos = True, adj

            if event.type == pygame.MOUSEMOTION and drawing:
                adj = (event.pos[0], event.pos[1] - UI_HEIGHT)
                if tool in ['pen', 'eraser']:
                    draw_line_segment(canvas, start_pos, adj, radius, color_mode, tool)
                    start_pos = adj

            if event.type == pygame.MOUSEBUTTONUP and drawing:
                draw_shape(canvas, tool, start_pos, (event.pos[0], event.pos[1] - UI_HEIGHT), radius, color_mode)
                drawing = False

        screen.blit(canvas, (0, UI_HEIGHT))
        if drawing and tool not in ['pen', 'eraser']:
            draw_shape(screen, tool, (start_pos[0], start_pos[1] + UI_HEIGHT), pygame.mouse.get_pos(), radius, color_mode)
        if text_active:
            screen.blit(text_font.render(text_value + "|", True, get_color(color_mode)), (text_pos[0], text_pos[1] + UI_HEIGHT))
        
        draw_ui(screen, font, tool, color_mode, radius)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()

if __name__ == "__main__":
    main()