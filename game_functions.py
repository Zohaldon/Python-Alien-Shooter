import sys
import pygame

def check_events():
    """ 
    Catch and respond to any event caused in game
    Captures mouse and keyboard key presses
    """
    # catch keyboard and mouse event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(as_settings, screen, ship):
    # add color to the screen
    screen.fill(as_settings.bg_color)
    ship.blitme()   
    # make screen visible
    pygame.display.flip()