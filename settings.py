class Settings():
    """
    Class to set all settings for Ailen shooter game
    """
    def __init__(self):
        """Initialize game settings"""
        # screen settings 
        self.screen_height = 700
        self.screen_width = 1050
        self.bg_color = (41, 40, 40)

        # Ship settings
        self.ship_speed_meter = 1.5
        self.allowed_ship = 3

        # Bullet settings
        self.bullet_speed_meter = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 240, 240, 240
        self.allowed_bullets = 10

        # Alien settings
        self.alien_speed_meter = 0.4
        self.fleet_drop_speed = 10

        # fleet_direction ; 1 = right and -1 is left
        self.fleet_direction = 1