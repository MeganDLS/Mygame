"""
"""
from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.
    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.
        Args:
            cast (Cast): The cast of Actors in the game.
          
        """
        
        dibble = cast.get_actors("Dibble")
        ice = cast.get_actors("Ice")
        penguin = cast.get_first_actor("Penguin")
        score = cast.get_first_actor("Score")
        lives = cast.get_first_actor("Lives")
        messages = cast.get_actors("Message")
        self._video_service.clear_buffer()

        for dib in dibble:
            self._video_service.draw_image(dib)
        self._video_service.draw_actors([score])
        self._video_service.draw_actor(lives)
        for icee in ice:
            self._video_service.draw_image(icee)
        self._video_service.draw_actors(messages)
        self._video_service.draw_image(penguin)
        self._video_service.flush_buffer()