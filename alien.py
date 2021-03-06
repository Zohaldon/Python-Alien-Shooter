import pygame 
from pygame.sprite import Sprite
import os 

class Alien(Sprite):
    """Class to represent a single alien."""
    def __init__(self, as_settings, screen):
        """Initialize the alien and set starting position.""" 
        super(Alien, self).__init__()
        self.screen = screen
        self.as_settings = as_settings

        # get image path
        current_path = os.path.dirname(__file__)
        images_path = os.path.join(current_path, 'images')
        alien_image_path = os.path.join(images_path, 'alien.png')
        
        # Load alien image and add rect
        self.image = pygame.image.load(alien_image_path)
        self.rect = self.image.get_rect()
        
        # Add alien at top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the alien's position.        
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at current location."""
        self.screen.blit(self.image, self.rect) 
    
    def check_edges(self):
        """Return trye if alien is at the edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien to right side"""
        self.x += (self.as_settings.alien_speed_meter * self.as_settings.fleet_direction)
        self.rect.x = self.x