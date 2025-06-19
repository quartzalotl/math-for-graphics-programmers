import pygame
from pygame.locals import *  # mouse button support

screen_width = 1000
screen_height = 800

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))

done = False
white = pygame.Color(255, 255, 255)
clicks = []
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if len(clicks) < 3:
                clicks.append(pygame.mouse.get_pos())
    if len(clicks) == 3:
        pygame.draw.polygon(screen, white, clicks)
        clicks = []
    pygame.display.update()
pygame.quit()