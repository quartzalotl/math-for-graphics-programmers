import pygame

screen_width = 800
screen_height = 200

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))

done = False
white = pygame.Color(255, 255, 255)

pygame.font.init()
font = pygame.font.SysFont('Baskerville', 120, False, True) # Font name, Size, Bold, Italic
text = font.render("Quartzalotl", False, white) # text, anti-alias, color

print(pygame.font.get_fonts())

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(text, (10, 10)) # Draw an existing drawn surface on top of another
    pygame.display.update()
pygame.quit()