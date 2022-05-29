"""
"""
from constants import *
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color


class Lives(Actor):
    """
    The responsibility of Lives is to keep track of penguin's lives.
   
    """
    def __init__(self, position):
        """Creates an instance of score
        Arguments:
            position

        """
        super().__init__()
        self._lives = 3
        self.set_position(position)
        self.set_color(WHITE)
        self._prepare_score()
        

    def remove_life(self):
        """Removes a life
        """
        self._lives -= 1
        self._prepare_score()

    def _prepare_score(self):
        """ Sets up score display
        """
        text = str(self._lives)
        self.set_text(f"Lives: {text}")