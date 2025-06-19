import pygame

screen_width = 1000
screen_height = 800

pygame.init()  # initialize pygame
pygame.display.set_mode((screen_width, screen_height)) # get_mode: create and return display surface object

# Keep graphics window open
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # pygame.QUIT is an event triggered when there is an attempt tp close the window
            done = True
    pygame.display.update()
pygame.quit()