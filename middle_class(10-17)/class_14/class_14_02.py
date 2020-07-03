import pygame
import sys
pygame.init()

x = 450
y = 350
t = True

screen = pygame.display.set_mode((800, 600))

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.draw.circle(screen, (255, 0, 0), (400, 200), 50, 2)
    pygame.draw.line(screen, (255, 0, 0), (400, 250), (400, 450), 2)
    pygame.draw.line(screen, (255, 0, 0), (400, 300), (450, 350), 2)
    pygame.draw.line(screen, (255, 0, 0), (400, 300), (350, 350), 2)
    pygame.draw.line(screen, (255, 0, 0), (400, 450), (350, 500), 2)
    pygame.draw.line(screen, (255, 0, 0), (400, 450), (450, 500), 2)
    pygame.display.update()
