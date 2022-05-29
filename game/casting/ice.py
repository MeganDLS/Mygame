"""
"""
from constants import *
from game.casting.actor import Actor
from game.shared.point import Point

class Ice(Actor):
    """
    Chunks of ice in the game.
    """
    def __init__(self, image, x, y, velocity):
        """
        image
        position
        velocity
        """
        super().__init__()
        self._image = image
        self._position = Point(x, y)
        self._velocity = Point(velocity, 0)

    