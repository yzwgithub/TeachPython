import pygame
import sys
import random
pygame.init()
screen = pygame.display.set_mode((400, 300))
x = 0
y = 0

y_1 = random.randint(0, 50) * 6
is_click = False
while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            y, y = event.pos
            y_1 = random.randint(0, 50) * 6
            is_click = True
    if is_click:
        x = x + 1
    if x >= 600:
        is_click = False
        x = 0
        y = 0

    pygame.draw.circle(screen, (0, 0, 0), (x, y), 5, 0)
    pygame.draw.rect(screen, (255, 0, 0), (380, y_1, 50, 50), 0)
    pygame.display.update()
