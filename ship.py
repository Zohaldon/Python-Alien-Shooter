import pygame
import os
class Ship():
    """Initialize ship and set it's initial position"""
    def __init__(self, screen):
        self.screen = screen

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

        # Movement flag
        self.moving_right = False
        self.moving_left = False
    
    def blitme(self):
        """Render ship at it's current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based upon movement flag"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1