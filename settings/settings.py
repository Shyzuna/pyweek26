import os
from settings.enums import ObjectCategory

# Generation
SEED = None  #93917774  # None for random
SEED_POWER = 8
DELTA_PERCENT = 0.1
RESOURCES = [ObjectCategory.HYDROGEN, ObjectCategory.DIHYGROGEN, ObjectCategory.TRIHYGROGEN, ObjectCategory.TRIHELIUM]
SPOT_NUMBERS = [0.01, 0.06, 0.03, 0.02]  # percent
REPARTITION_NUMBERS = [0.04, 0.02, 0.014, 0.06]  # percent
TOTAL_RES = 1000

# Display
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 800
FPS = 60


# Paths
TILES_PATH = os.path.join('data', 'tiles')
RESOURCES_PATH = os.path.join('data', 'resources')
FONT_PATH = os.path.join('data', 'fonts')
GUI_PATH = os.path.join('data', 'gui')

# Map parameters
TILE_WIDTH = 60
TILE_HEIGHT = 60
TILES_NUM_WIDTH = 64
TILES_NUM_HEIGHT = 64

BORDER_TILES_NUM = 3
BORDER_TILES_WIDTH = TILE_WIDTH * BORDER_TILES_NUM
BORDER_TILES_HEIGHT = TILE_HEIGHT * BORDER_TILES_NUM

MAP_WIDTH = TILE_WIDTH * TILES_NUM_WIDTH
MAP_HEIGHT = TILE_HEIGHT * TILES_NUM_HEIGHT
MAP_SIZE = (TILES_NUM_WIDTH + BORDER_TILES_NUM, TILES_NUM_HEIGHT + BORDER_TILES_NUM)
RECT_MAX_X = MAP_WIDTH - SCREEN_WIDTH + BORDER_TILES_WIDTH
RECT_MAX_Y = MAP_HEIGHT - SCREEN_HEIGHT + BORDER_TILES_HEIGHT
DEFAULT_HQ_POS = (4, 4)

# Scroll parameters
SCROLL_SPEED_HORIZONTAL = 1.0
SCROLL_SPEED_VERTICAL = 1.0
SCROLL_MOUSE_MARGIN = 5
SCROLL_MOUSE_MAX_X = SCREEN_WIDTH - SCROLL_MOUSE_MARGIN
SCROLL_MOUSE_MAX_Y = SCREEN_HEIGHT - SCROLL_MOUSE_MARGIN

# UI
UI_TOP_BAR = 0.06
UI_SIDE_BAR = 0.1
