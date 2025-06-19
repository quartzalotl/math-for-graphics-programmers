import pygame

screen_width = 700
screen_height = 300

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))

done = False
white = pygame.Color(255, 255, 255)

pygame.font.init()
title_font = pygame.font.Font('Chapter 2/fonts/CHAOS METAL.ttf', 120) # Font name, Size, Bold, Italic
subtitle_font = pygame.font.Font('Chapter 2/fonts/Agasiz.ttf', 80) # Font name, Size, Bold, Italic
name = title_font.render("Quartzalotl", False, white) # text, anti-alias, color
statement = subtitle_font.render("Always Climbing", False, white) # text, anti-alias, color

print(pygame.font.get_fonts())

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(name, (20, 10)) # Draw an existing drawn surface on top of another
    screen.blit(statement, (100, 200)) # Draw an existing drawn surface on top of another
    pygame.display.update()
pygame.quit()