"""
"""
from constants import *
from game.casting.actor import Actor
from game.shared.point import Point

class Penguin(Actor):
    """
    Main player in the game.
    
    The responsibility of Penguin is to hold the image and hold the updated position.
        
    """
    def __init__(self):
        super().__init__()
        self._image = PENGUIN
        self._position = Point(200, 325)
        self._velocity = Point(0, 0)
    

    def get_image(self):
        """Gets the penguin's image."""
        return self._image
    
    def move_next(self):
        """Moves the penguin."""
        position = self.get_position()
        velocity = self.get_velocity()
        new_position = position.add(velocity)
        self.set_position(new_position)
