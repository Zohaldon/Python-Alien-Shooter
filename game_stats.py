class GameStats():
    """Track game progress"""
    def __init__(self, as_settings):
        self.as_settings = as_settings
        self.reset_stats()
        self.game_active = True
        
    def reset_stats(self):
        self.ships_left = self.as_settings.allowed_ship