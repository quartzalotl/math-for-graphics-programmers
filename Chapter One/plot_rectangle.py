import pygame

pygame.init()  # initialize pygame

screen_width = 1000
screen_height = 800
white = pygame.Color(255, 255, 255)

screen = pygame.display.set_mode((screen_width, screen_height)) # get_mode: create and return display surface object

def draw_star(x, y, brightness):
    pygame.draw.rect(screen, white, (x, y, brightness, brightness))

gemini_half = [
    (100, 50, 15),
    (130, 160, 10),
    (45, 189, 11),
    (200, 170, 10),
    (160, 350, 11),
    (75, 450, 12),
    (135, 560, 14),
    (300, 545, 13),
]

# Keep graphics window open
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # pygame.QUIT is an event triggered when there is an attempt tp close the window
            done = True
    for star in gemini_half:
        draw_star(*star)
    pygame.display.update()
pygame.quit()
