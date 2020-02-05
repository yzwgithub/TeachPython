# 计时器
import pygame
import time
import sys

start_time = time.time()

pygame.init()
screen = pygame.display.set_mode((200, 100))

font = pygame.font.Font(None, 30)
while True:
    screen.fill((255, 255, 255))
    end_time = time.time()
    time_ = end_time - start_time
    time_ = int(time_)
    text = font.render(str(time_), 0, (255, 0, 0))
    screen.blit(text, (100, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
