import pygame

screen_width = 1000
screen_height = 800

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    for x in range(screen_width):
        for y in range(screen_height):
            screen.set_at((x, y), pygame.Color(255, int(x/screen_width*255), int(y/screen_height*255)))
    pygame.display.update()
pygame.quit()