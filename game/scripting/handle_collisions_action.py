
"""
"""
# from raylib import PlayMusicStream, PlaySound
from constants import *
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    Interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to set up what happens when the penguin touches ice
    Move with is, when the penguin touches dibbles, dibbles disappear and when the penguin touches neither, game is over.
    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._winner = False
        self._loser = False

    def execute(self, cast, script):
        """Executes the handle collisions action.
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
        
            if self._winner:
                self._handle_winner(cast)
            
            if self._loser:
                self._handle_loser(cast)
    
    def _handle_segment_collision(self, cast):
        """Game over if penguin falls into the water and sets off the bubbles.
        TODO disappears penguin
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        penguin = cast.get_first_actor("Penguin")
        icee = cast.get_actors("Ice")
        dibbles = cast.get_actors("Dibbles")
        life = cast.get_first_actor("Lives")
        
        y = penguin.get_position().get_y()
        if y <= 100:
            self._winner= True
            self._is_game_over = True
            # PlaySound(ICE_SOUND)
            
        for ice in icee:
            if ice.get_position().equals(penguin.get_position()):
                life.remove_life()
                # PlayMusicStream(WELCOME_SOUND)

                if life._lives == 0:
                    self._is_game_over = True
                    self._loser = True
                    # PlaySound(OVER_SOUND)
                position = Point(MAX_X/2, 500)
                penguin.set_position(position)


    def _handle_winner(self, cast):
        """When the penguin reaches a cheese dibble and where to show the message
        """
        if self._winner:
            message = Actor()
            message.set_text("Yum!")
            message.set_color = BLACK
            position = Point(MAX_X/2, MAX_Y/2)
            message.set_position(position)
            cast.add_actor("Message", message)

    def _handle_loser(self, cast):
        """Shows the 'game over' message.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._loser:
            message = Actor()
            message.set_text("Try Again!")
            message.set_color = BLACK
            position = Point(MAX_X/2, MAX_Y/2)
            message.set_position(position)
            cast.add_actor("Message", message)


    def get_is_game_over(self):
        """
        """
        return self._is_game_over

    def get_is_winner(self):
        """
        """
        return self._winner

    