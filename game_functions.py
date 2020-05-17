import sys
import pygame
from bullet import Bullet 

def check_keydown_events(event, as_settings, screen, ship, bullets):
    """Respond to key press"""
    # Move right
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        ship.image = ship.moving_ship_image
    # Move left
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
        ship.image = ship.moving_ship_image
    if event.key == pygame.K_SPACE:
        # Create bullet and add it to group
        fire_bullet(as_settings, screen, ship, bullets)
    if event.key == pygame.K_q:
        sys.exit()

def fire_bullet(as_settings, screen, ship, bullets):
    """ Fire bullets"""
    if len(bullets) < as_settings.allowed_bullets:
        new_bullet = Bullet(as_settings, screen, ship)
        bullets.add(new_bullet)

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

def check_events(as_settings, screen, ship, bullets):
    """ 
    Catch and respond to any event caused in game
    Captures mouse and keyboard key presses
    """
    # catch keyboard and mouse event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, as_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(as_settings, screen, ship, alien, bullets):
    # add color to the screen
    screen.fill(as_settings.bg_color)
    ship.blitme()
    alien.blitme()
    # Redraw all bullets behind ship
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # make screen visible
    pygame.display.flip()

def update_bullets(bullets):
    """ Update bullet and get rid of fired bullets not visible anymore"""
    bullets.update()
    # Delete bullets which are fired and invisible above screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)