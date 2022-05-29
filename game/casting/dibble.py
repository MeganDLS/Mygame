from constants import *
from game.casting.actor import Actor
from game.shared.point import Point

class Dibble(Actor):
    """
    A record of points made or lost. 
    The responsibility of Score is to keep track scores and 
    add points. 
    Attributes:
        self._score (int) 
        self._prepare_score: calls the _prepare_score method to print on screen
    """
    def __init__(self, image, x, y):
        super().__init__()
        self._image = image
        self._position = Point(x, y) 
    
    
    # def __init__(self, position):
    #     """Creates an instance of score
    #     Arguments:
    #         _player_name
    #         _position
    #     """
    #     super().__init__()
    #     self._image = DIBBLE
    #     self._position = Point(100, 100)
        
    # def get_image(self):
    #     """Gets the cheezy dibble image."""
    #     return self._image

       