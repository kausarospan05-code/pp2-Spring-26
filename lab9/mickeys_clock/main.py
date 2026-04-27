import pygame
import os
import sys
from clock import get_time_angles

pygame.init()

WIDTH, HEIGHT = 400, 400 
CENTER = (WIDTH // 2, HEIGHT // 2)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()

base_dir = os.path.dirname(os.path.abspath(__file__))
img_dir = os.path.join(base_dir, "images")

def load_and_scale(name, size=None):
    img = pygame.image.load(os.path.join(img_dir, name)).convert_alpha()
    if size:
        img = pygame.transform.scale(img, size)
    return img

# Load assets
clock_bg = load_and_scale("clock.png", (WIDTH, HEIGHT))
hour_hand = load_and_scale("hour_hand.png")
minute_hand = load_and_scale("minute_hand.png")
tail = load_and_scale("tail.png") 

def blit_rotate_center(surf, image, center, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=center).center)
    surf.blit(rotated_image, new_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# ЛОГИКА: clock.py файлынан бұрыштарды алу
    # Ол жерде уақытқа байланысты градустар есептеледі (мысалы: 1 сек = 6 градус)
    
    h_angle, m_angle, s_angle = get_time_angles()

    # Rendering
    screen.fill((255, 255, 255)) # White clock edges
    #Event Handling: pygame.QUIT арқылы бағдарламаның дұрыс жабылуын қамтамасыз етеді.

#Rendering: Әр кадрда экран ақ түспен тазаланып, жаңа бұрыштар бойынша тілдер қайтадан салынып отырады.

#Clock.tick(60): Процессорды артық жүктемей, бірқалыпты 60 кадр жиілігін ұстайды.
    # Draw Background
    screen.blit(clock_bg, (0, 0))
# 2. Тілдерді қабат-қабат етіп салу (Орталық нүктеге қатысты айналдыру)
    # Тәртібі: Секунд -> Сағат -> Минут
    # Draw the Tail & Hands
    blit_rotate_center(screen, tail, CENTER, s_angle)
    blit_rotate_center(screen, hour_hand, CENTER, h_angle)
    blit_rotate_center(screen, minute_hand, CENTER, m_angle)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()