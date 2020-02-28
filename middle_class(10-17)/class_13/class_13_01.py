import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((800, 600), depth=8)

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
