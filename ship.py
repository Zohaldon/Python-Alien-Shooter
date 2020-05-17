import pygame
import os
class Ship():
    """Initialize ship and set it's initial position"""
    def __init__(self, screen):
        self.screen = screen

        # get image path
        current_path = os.path.dirname(__file__)
        resource_path = os.path.join(current_path, 'images')
        image_path = os.path.join(resource_path, 'ship_steady.png')
        
        # Load ship image and set rect
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # New ship at bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    
    def blitme(self):
        """Render ship at it's current location"""
        self.screen.blit(self.image, self.rect)