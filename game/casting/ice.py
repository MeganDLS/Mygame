from constants import *
from game.casting.actor import Actor
from game.shared.point import Point

class Ice(Actor):
    """
    Chunks of ice are in the game.
    
    The responsibility of Ice is to prepare the ice chunks in the game.
    """
    def __init__(self, image, x, y, velocity):
        super().__init__()
        self._image = image
        self._position = Point(x, y)
        self._velocity = Point(velocity, 0)

    