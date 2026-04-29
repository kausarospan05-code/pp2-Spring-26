import pygame
from datetime import datetime
import os

def get_color(mode):
    d = {'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255), 'black': (0, 0, 0)}
    return d.get(mode, (0, 0, 0))

def draw_line_segment(surf, start, end, width, mode, tool):
    color = (255, 255, 255) if tool == 'eraser' else get_color(mode)
    # Using a thicker line for the freehand tool to ensure it feels smooth
    pygame.draw.line(surf, color, start, end, width * 2)

def draw_shape(surf, tool, start, end, radius, mode):
    color = get_color(mode)
    if tool == 'line':
        pygame.draw.line(surf, color, start, end, radius)
    elif tool == 'rectangle':
        x, y = min(start[0], end[0]), min(start[1], end[1])
        w, h = abs(start[0] - end[0]), abs(start[1] - end[1])
        pygame.draw.rect(surf, color, (x, y, w, h), radius)
    elif tool == 'circle':
        rad = int(((end[0]-start[0])**2 + (end[1]-start[1])**2)**0.5)
        pygame.draw.circle(surf, color, start, rad, radius)
    elif tool == 'square':
        side = min(abs(end[0]-start[0]), abs(end[1]-start[1]))
        x = start[0] if end[0] > start[0] else start[0] - side
        y = start[1] if end[1] > start[1] else start[1] - side
        pygame.draw.rect(surf, color, (x, y, side, side), radius)
    elif tool in ['right_triangle', 'equilateral_triangle', 'rhombus']:
        pts = []
        if tool == 'right_triangle': 
            pts = [start, (start[0], end[1]), end]
        elif tool == 'rhombus':
            mx, my = (start[0]+end[0])//2, (start[1]+end[1])//2
            pts = [(mx, start[1]), (end[0], my), (mx, end[1]), (start[0], my)]
        elif tool == 'equilateral_triangle':
            side = abs(end[0] - start[0])
            h = int(0.866 * side)
            pts = [(start[0], end[1]), (end[0], end[1]), ((start[0]+end[0])//2, end[1]-h)]
        if pts: pygame.draw.polygon(surf, color, pts, radius)

def flood_fill(surf, pos, new_color):
    target = surf.get_at(pos)
    if target == new_color: return
    pixels = [pos]
    w, h = surf.get_size()
    while pixels:
        x, y = pixels.pop()
        if 0 <= x < w and 0 <= y < h and surf.get_at((x, y)) == target:
            surf.set_at((x, y), new_color)
            pixels.extend([(x+1, y), (x-1, y), (x, y+1), (x, y-1)])

def save_canvas(surf):
    
    if not os.path.exists("assets"):
        os.makedirs("assets")
        
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    name = f"assets/paint_{timestamp}.png"
    pygame.image.save(surf, name)
    print(f"Canvas saved to: {name}")