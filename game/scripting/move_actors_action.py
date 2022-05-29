"""
"""
from game.scripting.action import Action
 
class MoveActorsAction(Action):
    """
    The responsibility of MoveActors Action is to move all the actors.
    """

    def execute(self, cast, script):
        """
        Implements method overriding of the 'execute' method in the Action Class.
        Arguments:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of actions in the game
        """
        
        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()