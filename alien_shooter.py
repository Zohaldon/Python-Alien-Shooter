import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats

def run_game():
    # Initialize pygame, settings and screen for Alien shooter
    pygame.init()
    as_settings = Settings()
    screen = pygame.display.set_mode((as_settings.screen_width, as_settings.screen_height))
    pygame.display.set_caption("Alien Shooter")

    stats = GameStats(as_settings)
    # Create ship
    ship = Ship(as_settings, screen)
    
    # Group to store bullet
    bullets = Group()
    aliens = Group()

    # Create fleet of alien
    gf.create_fleet(as_settings, screen, ship, aliens)
    
    # Start game
    while True:
        gf.check_events(as_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(as_settings, screen, ship, aliens, bullets)
        gf.update_aliens(as_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(as_settings, screen, ship, aliens, bullets)

run_game()