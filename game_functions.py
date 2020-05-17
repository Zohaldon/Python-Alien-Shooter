import sys
import pygame

def check_keydown_events(event, ship):
    """Respond to key press"""
    # Move right
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        ship.image = ship.moving_ship_image
    # Move left
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
        ship.image = ship.moving_ship_image

def check_keyup_events(event, ship):
    """Respond to key release"""
    # Stop moving right
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
        ship.image = ship.ship_steady_image
    # Stop moving left
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
        ship.image = ship.ship_steady_image

def check_events(ship):
    """ 
    Catch and respond to any event caused in game
    Captures mouse and keyboard key presses
    """
    # catch keyboard and mouse event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(as_settings, screen, ship):
    # add color to the screen
    screen.fill(as_settings.bg_color)
    ship.blitme()   
    # make screen visible
    pygame.display.flip()