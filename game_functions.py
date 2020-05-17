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
            if event.key == pygame.K_RIGHT:
                # move ship right
                ship.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                # move ship right
                ship.moving_right = False

def update_screen(as_settings, screen, ship):
    # add color to the screen
    screen.fill(as_settings.bg_color)
    ship.blitme()   
    # make screen visible
    pygame.display.flip()