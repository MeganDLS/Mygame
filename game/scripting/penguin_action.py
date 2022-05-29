
from ast import Not
from constants import *
from game.scripting.action import Action
from game.shared.point import Point
from game.services.keyboard_service import KeyboardService

class PenguinAction(Action):
    """
    Responsible for getting the direction and moving the penguin.
    """
    def __init__(self, keyboard):
        """Constructs a new instance using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard
        self._direction = Point(0, 0)


    def execute(self, cast, script):
        """Executes action.
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score = cast.get_first_actor("Score")
        dibble = cast.get_first_actor("Dibble")
        self._direction = Point(0, 0)
        penguin = cast.get_first_actor("Penguin")
        x = penguin._position.get_x()
        y = penguin._position.get_y()

        handle_collisions_class = script.get_second_action("update")
        game_over = handle_collisions_class.get_is_game_over()

        if not game_over:
            if self._keyboard_service.is_key_down('left'):
                if x >= 50:
                    self._direction = Point(-CELL_SIZE, 0)
                    score.add_points()
            if self._keyboard_service.is_key_down('right'):
                if x <= (MAX_X - 50):
                    self._direction = Point(CELL_SIZE, 0)
                    score.add_points()
            if self._keyboard_service.is_key_down('up'):
                if y >= 50:
                    self._direction = Point(0, -CELL_SIZE)
                    score.add_points()
            if self._keyboard_service.is_key_down('down'):
                if y <= MAX_Y - 50:
                    self._direction = Point(0, CELL_SIZE)
                    score.add_points()

            penguin.set_velocity(self._direction)
            penguin.move_next()

        else:
            penguin.set_velocity(Point(0,0))