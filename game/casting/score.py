"""
"""
from constants import *
from game.casting.actor import Actor
from game.shared.point import Point

class Score(Actor):
    """
    The responsibility of Score is to keep track the score.
    """
    def __init__(self, position):
        """Creates an instance of score
        Arguments:
            _position
        """
        super().__init__()
        self._score = 0
        self.set_position(position)
        self.set_color(WHITE)
        self._prepare_score()
        

    def add_points(self):
        """Adds the given points to the score's total points.
        """
        self._score += 1
        self._prepare_score()

    def _prepare_score(self):
        """
        Text set up
        """
        text = str(self._score)
        self.set_text(f"Score : {text}")
       