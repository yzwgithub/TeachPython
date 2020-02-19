import pygame
import sys
import time

pygame.init()
y = 100
screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font(None, 40)
str = "I'm xiaoming and i like wangzai!"
text = font.render(str, 0, (255, 0, 0))
while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if y > -100:
        y = y-1
    else:
        y = 600
    time.sleep(0.01)
    screen.blit(text, (y, 250))
    pygame.display.update()
