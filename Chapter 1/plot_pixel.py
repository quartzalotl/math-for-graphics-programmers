import pygame

pygame.init()  # initialize pygame

screen_width = 1000
screen_height = 800
white = pygame.Color(255, 255, 255)

screen = pygame.display.set_mode((screen_width, screen_height)) # get_mode: create and return display surface object

# Keep graphics window open
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # pygame.QUIT is an event triggered when there is an attempt tp close the window
            done = True
    screen.set_at((100, 100), white)  # origin is at the top left
    screen.set_at((200, 200), white)
    pygame.display.update()
pygame.quit()

'''
Notes:
    - origin is at top left because of the way electron scan lines went across and down the screen
    - you must orient the coordinate system based on how the axes are specific to the platform
'''
