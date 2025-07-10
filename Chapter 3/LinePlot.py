import pygame

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

done = False
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
blue = pygame.Color(125, 125, 255)
green = pygame.Color(0, 255, 0)
xorigin_offset = int(screen.get_width() / 2)
yorigin_offset = int(screen.get_height() / 2)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # draw x axis
    for x in range (-500, 500):
        screen.set_at((x + xorigin_offset, yorigin_offset), green)

    # draw y axis
    for y in range (-500, 500):
        screen.set_at((xorigin_offset, y + yorigin_offset), green)
    
    # draw a brute force line
    for x in range(-500, 500):
        y = 2 * x + 4  # equation of the line to draw, you can still see some gaps in this
        screen.set_at((x + xorigin_offset, y + yorigin_offset), red)
        y = int(0.05 * x) - 100  # 'stepping' occurring with near-horizontal slope due to pixel rounding to nearest int
        screen.set_at((x + xorigin_offset, y + yorigin_offset), blue)
        y = (10 * x) - 100  # equation of the line to draw -> even more gaps and skips in this line
        screen.set_at((x + xorigin_offset, y + yorigin_offset), white)

    pygame.display.update()
pygame.quit()
