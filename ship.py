import pygame
import os
class Ship():
    """Initialize ship and set it's initial position"""
    def __init__(self, as_settings, screen):
        self.screen = screen
        self.as_settings = as_settings

        # Get image path
        current_path = os.path.dirname(__file__)
        images_path = os.path.join(current_path, 'images')
        ship_image_path = os.path.join(images_path, 'ship_steady.png')
        # Load ship image and set rect
        self.image = pygame.image.load(ship_image_path)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # New ship at bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store ship location for center
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
    
    def blitme(self):
        """Render ship at it's current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based upon movement flag"""
        # Update ship's center value instead of rect
        if self.moving_right:
            self.center += self.as_settings.ship_speed_meter
        if self.moving_left:
            self.center -= self.as_settings.ship_speed_meter
        # Update rect based upon center value of ship
        self.rect.centerx = self.center