import sys
import pygame

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
            # Move right
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            # Move left
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            # Stop moving right
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            # Stop moving left
            if event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(as_settings, screen, ship):
    # add color to the screen
    screen.fill(as_settings.bg_color)
    ship.blitme()   
    # make screen visible
    pygame.display.flip()