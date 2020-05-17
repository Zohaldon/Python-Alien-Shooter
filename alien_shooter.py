import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
    # Initialize pygame, settings and screen for Alien shooter
    pygame.init()
    as_settings = Settings()
    screen = pygame.display.set_mode((as_settings.screen_width, as_settings.screen_height))
    pygame.display.set_caption("Alien Shooter")

    # Create ship
    ship = Ship(screen)

    # start game
    while True:
        gf.check_events()
        # add color to the screen
        screen.fill(as_settings.bg_color)
        ship.blitme()   
        # make screen visible
        pygame.display.flip()

run_game()