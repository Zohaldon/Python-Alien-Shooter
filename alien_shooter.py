import sys
import pygame

def run_game():
    # set display 
    pygame.init()
    screen = pygame.display.set_mode((1050,700))
    pygame.display.set_caption("Alien Shooter")

    # background color
    bg_color = (41, 40, 40)

    # start game
    while True:
        # catch keyboard and mouse event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # add color to the screen
        screen.fill(bg_color)    
        # make screen visible
        pygame.display.flip()

run_game()