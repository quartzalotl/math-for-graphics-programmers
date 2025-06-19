import pygame

screen_width = 1170
screen_height = 781

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("A Beautiful Sunset") # Adds title to the window
bg_img = pygame.image.load("Chapter Two/nightsky.jpeg")
alienbird = pygame.image.load("Chapter Two/alienbird.png")

done = False
white = pygame.Color(255, 255, 255)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(bg_img, (0, 0))
    screen.blit(alienbird, (148, 167))
    pygame.display.update()
pygame.quit()