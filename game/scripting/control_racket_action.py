from constants import *
from game.casting.ball import Ball
from game.scripting.action import Action


class ControlRacketAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        # skipper = cast.get_first_actor(BALL_GROUP)
        # if self._keyboard_service.is_key_down(LEFT):
        #     Ball.swing.left()
        # elif self._keyboard_service.is_key_down(RIGHT):
        #     Ball.swing_right()
        # elif self._keyboard_service.is_key_down(UP):
        #     Ball.swing_up()
        # elif self._keyboard_service.is_key_down(DOWN):
        #     Ball.swing_down()
        # else:
        #     Ball.stop_moving(Ball)
        racket = cast.get_first_actor(RACKET_GROUP)
        if self._keyboard_service.is_key_down(LEFT): 
            racket.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT): 
            racket.swing_right()  
        # elif self._keyboard_service.is_key_down(UP): 
        #     racket.swing_up()  
        # elif self._keyboard_service.is_key_down(DOWN): 
        #     racket.swing_down()  
        else: 
            racket.stop_moving()        