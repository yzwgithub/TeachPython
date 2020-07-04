import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
t = pygame.image.load('t_01.jpg')
x = 0
y = 0
t_x = 0
t_y = 0
while True:
    screen.fill((255, 255, 255))
    mylist = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if mylist[pygame.K_LEFT]:
            x = x - 3

        if mylist[pygame.K_RIGHT]:
            x = x + 3

        if mylist[pygame.K_UP]:
            y = y - 3

        if mylist[pygame.K_DOWN]:
            y = y + 3

    screen.blit(t, (0 + x, 0 + y))
    pygame.draw.circle(screen, (255, 0, 0), (400 + x, 200 + y), 50, 2)
    pygame.draw.line(screen, (255, 0, 0), (400 + x, 250 + y), (400 + x, 450 + y), 2)

    pygame.display.update()
