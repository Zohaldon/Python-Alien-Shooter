import sys
import pygame
from bullet import Bullet 
from alien import Alien

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

def update_screen(as_settings, screen, ship, aliens, bullets):
    # add color to the screen
    screen.fill(as_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)
    # Redraw all bullets behind ship
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # make screen visible
    pygame.display.flip()

def update_bullets(as_settings, screen, ship, aliens, bullets):
    """ Update bullet and get rid of fired bullets not visible anymore"""
    bullets.update()
    # Delete bullets which are fired and invisible above screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisons(as_settings, screen, ship, aliens, bullets)

def check_bullet_alien_collisons(as_settings, screen, ship, aliens, bullets):
    """Handels ship and bullet hit"""
    # Check if bukket has hit alien, delete alien if bullet hit
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # Clear existing bullets and add new fleet
        bullets.empty()
        create_fleet(as_settings, screen, ship, aliens)


def get_number_aliens_x(as_settings, alien_width):
    """Determine the number of alien that can fit in row"""
    # Total available horizontal space on screen
    available_space_x = as_settings.screen_width - (2 * alien_width)
    # Total aliens that could be fitted horizontaly
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(as_settings, ship_height, alien_height):
    """Determine number of rows that can be fit in screen"""
    available_space_y = (as_settings.screen_height - ( 3 * alien_height) - ship_height )
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(as_settings, screen, aliens, alien_number, row_number):
    alien = Alien(as_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(as_settings, screen, ship, aliens):
    """Create full army of alien"""
    alien = Alien(as_settings, screen)
    number_aliens_x = get_number_aliens_x(as_settings, alien.rect.width)
    number_rows = get_number_rows(as_settings, ship.rect.height, alien.rect.height)
    # Create first row of alien
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(as_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(as_settings, aliens):
    """Drop alien if they reached the edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(as_settings, aliens)
            break

def change_fleet_direction(as_settings, aliens):
    """Change the fleets direction and drop them"""
    for alien in aliens.sprites():
        alien.rect.y += as_settings.fleet_drop_speed
    as_settings.fleet_direction *= -1

def update_aliens(as_settings, aliens):
    """Update the positions of all aliens in the fleet"""
    check_fleet_edges(as_settings, aliens)
    aliens.update()