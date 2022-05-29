"""
"""
import pathlib
from game.shared.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 
#Text
FONT_SIZE = 20
CAPTION = "Skipper"

WHITE = Color(255, 255, 255)
BLACK = Color(0, 0, 0)

#Sounds
ICE_SOUND = "assets\\sounds\\boing.wav"
WELCOME_SOUND = "assets\\sounds\\start.wav"
OVER_SOUND = "assets\\sounds\\over.wav"

#Grid
COLUMNS = 9
ROWS = 6
CELL_SIZE = 5

#Screen
MAX_X = 1200
MAX_Y = 800
FRAME_RATE = 15

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

ICEAA = "assets\\smlice.png"
ICEBB = "assets\\iceb.png"
ICECC = "assets\\iceb.png"

ICETRAIN = [ICEAA, ICEBB, ICECC, ICEAA, ICECC]

PENGUIN = "assets\\smlskipper.png"
DIBBLE = "assets\\cheeto.png"











# import pathlib as Path
# #raylib
# #Set up an absolute pathto see what the parent directory is
# # ROOTDIR = Path(__file__).parent
# #Calling the div operator to concatenate - works on linux mac and windows.
# # IMAGES = ROOTDIR / "images"
# # FONTS = ROOTDIR / ASSETSDIR / "fonts"
# # IMAGES = ROOTDIR / ASSETSDIR / "images"


# # SCREEN
# SCREEN_WIDTH = 1200
# SCREEN_HEIGHT = 800
# CENTER_X = SCREEN_WIDTH / 2
# CENTER_Y = SCREEN_HEIGHT / 2

# # FONT
# FONT_SERIF = "fonts\\Quicksand-Medium.ttf"
# FONT_SCRIPT = "fonts/Sacramento-Regular.ttf"
# FONT_BIG = 50

# SCENE = "images/scene.png"

# TITLE = 0
# GAMEPLAY = 1
# END = 2