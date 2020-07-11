import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((800, 600))

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.draw.circle(screen, (255, 0, 0), (400, 150), 20, 2)
    pygame.draw.line(screen, (255, 0, 0), (400, 170), (400, 230), 2)
    pygame.draw.line(screen, (255, 0, 0), (400, 190), (380, 200), 2)
    pygame.draw.line(screen, (255, 0, 0), (400, 190), (420, 200), 2)
    pygame.draw.line(screen, (255, 0, 0), (400, 230), (390, 290), 2)
    pygame.draw.line(screen, (255, 0, 0), (400, 230), (410, 290), 2)
    pygame.display.update()
