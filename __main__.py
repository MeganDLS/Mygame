"""
"""
from constants import *

from game.casting.actor import Actor
from game.casting.cast import Cast
from game.casting.penguin import Penguin
from game.casting.lives import Lives
from game.casting.score import Score
from game.casting.ice import Ice
from game.casting.dibble import Dibble
from game.director import Director
from game.scripting.action import Action
from game.scripting.script import Script
from game.scripting.draw_actors_action import DrawActorsAction
from game.scripting.penguin_action import PenguinAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point

def main():

    #Creates the cast: a penguin, the score, lives and ice chunks
    cast = Cast()
    cast.add_actor("Penguin", Penguin())
    cast.add_actor("Score", Score(Point(MAX_X-200, 25)))
    cast.add_actor("Dibble", Dibble(DIBBLE, 200, 100))
    cast.add_actor("Dibble", Dibble(DIBBLE, 300, 400))
    cast.add_actor("Dibble", Dibble(DIBBLE, 100, 100))
    cast.add_actor("Dibble", Dibble(DIBBLE, 400, 400))
    cast.add_actor("Dibble", Dibble(DIBBLE, 500, 100))
    cast.add_actor("Dibble", Dibble(DIBBLE, 500, 500))
    cast.add_actor("Dibble", Dibble(DIBBLE, 600, 400))
    cast.add_actor("Dibble", Dibble(DIBBLE, 700, 100))
    cast.add_actor("Dibble", Dibble(DIBBLE, 800, 400))
    cast.add_actor("Dibble", Dibble(DIBBLE, 700, 300))
    cast.add_actor("Dibble", Dibble(DIBBLE, 900, 400))
    cast.add_actor("Dibble", Dibble(DIBBLE, 1000, 400))

    cast.add_actor("Lives", Lives(Point(MAX_X-200, 50)))

    cast.add_actor("Ice", Ice(ICEAA, 100, 100, 1))
    cast.add_actor("Ice", Ice(ICEAA, 400, 100, 1))
    cast.add_actor("Ice", Ice(ICEAA, 700, 100, 1))    
    cast.add_actor("Ice", Ice(ICEBB, 300, 200, -4))
    cast.add_actor("Ice", Ice(ICEBB, 100, 200, -4))
    # cast.add_actor("Ice", Ice(ICEBB, 400, 200, -4))
    cast.add_actor("Ice", Ice(ICEBB, 500, 200, -4))
    cast.add_actor("Ice", Ice(ICECC, 100, 300, 2))
    cast.add_actor("Ice", Ice(ICECC, 300, 300, 2))
    cast.add_actor("Ice", Ice(ICECC, 500, 300, 2))
    cast.add_actor("Ice", Ice(ICEAA, 200, 400, -2))
    cast.add_actor("Ice", Ice(ICEAA, 900, 400, -2))
    cast.add_actor("Ice", Ice(ICEAA, 600, 400, -2))
    cast.add_actor("Ice", Ice(ICECC, 500, 500, 3))
    cast.add_actor("Ice", Ice(ICECC, 800, 500, 3))
    cast.add_actor("Ice", Ice(ICECC, 1100, 500, 3)) 

    keyboard = KeyboardService()
    video = VideoService()

    script = Script()
    script.add_action("input", PenguinAction(keyboard))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video))

    director = Director(video)
    director.start_game(cast, script)
    

if __name__ == "__main__":
    main()