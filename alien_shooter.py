import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # Initialize pygame, settings and screen for Alien shooter
    pygame.init()
    as_settings = Settings()
    screen = pygame.display.set_mode((as_settings.screen_width, as_settings.screen_height))
    pygame.display.set_caption("Alien Shooter")

    # Create ship
    ship = Ship(as_settings, screen)
    
    # Group to store bullet
    bullets = Group()

    # start game
    while True:
        gf.check_events(as_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(as_settings, screen, ship, bullets)

run_game()