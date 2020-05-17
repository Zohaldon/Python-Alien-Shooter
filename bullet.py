import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """
    Class to handle fired bullets
    """
    def __init__(self, as_settings, screen, ship):
        """Create bullet at ship's location"""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet
        self.rect = pygame.Rect(0,0, as_settings.bullet_width, as_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store bullet's position
        self.y = float(self.rect.y)

        self.color = as_settings.bullet_color
        self.speed_factor = as_settings.bullet_speed_meter
    
    def update(self):
        """Move bullet to the top"""
        # Set bullet
        self.y -= self.speed_factor
        # Update bullet on screen
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Render bullet on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)