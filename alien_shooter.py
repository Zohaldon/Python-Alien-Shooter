import sys
import pygame

def run_game():
    # set display 
    pygame.init()
    screen = pygame.display.set_mode((1050,700))
    pygame.display.set_caption("Alien Shooter")

    # start game
    while True:
        # catch keyboard and mouse event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # make screen visible
        pygame.display.flip()

run_game()