import os
from settings.enums import ObjectCategory

# Generation
SEED = None  #93917774  # None for random
SEED_POWER = 8
DELTA_PERCENT = 0.1
RESOURCES = [ObjectCategory.HYDROGEN, ObjectCategory.DIHYDROGEN, ObjectCategory.TRIHYDROGEN, ObjectCategory.TRIHELIUM]
SPOT_NUMBERS = [0.08, 0.03, 0.01, 0.01]  # percent
REPARTITION_NUMBERS = [1.6, 0.3, 0.05, 0.02]  # percent
TOTAL_RES = 100000


# Display
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 800
FPS = 60
AUTO_SIZE = True

# Paths
TILES_PATH = os.path.join('data', 'tiles')
RESOURCES_PATH = os.path.join('data', 'resources')
BUILDINGS_PATH = os.path.join('data', 'buildings')
FONT_PATH = os.path.join('data', 'fonts')
GUI_PATH = os.path.join('data', 'gui')
MUSIC_PATH = os.path.join('data', 'music')

# Map parameters
TILE_WIDTH = 64
TILE_HEIGHT = 64
TILES_NUM_WIDTH = 64
TILES_NUM_HEIGHT = 64

BORDER_TILES_NUM = 3
BORDER_TILES_WIDTH = TILE_WIDTH * BORDER_TILES_NUM
BORDER_TILES_HEIGHT = TILE_HEIGHT * BORDER_TILES_NUM

MAP_WIDTH = TILE_WIDTH * TILES_NUM_WIDTH + BORDER_TILES_WIDTH * 2
MAP_HEIGHT = TILE_HEIGHT * TILES_NUM_HEIGHT + BORDER_TILES_HEIGHT * 2
RECT_MAX_X = MAP_WIDTH - SCREEN_WIDTH
RECT_MAX_Y = MAP_HEIGHT - SCREEN_HEIGHT
DEFAULT_HQ_POS = (4, 4)
DEFAULT_TRANSMITTER_POS = (4, 8)

# Scroll parameters
SCROLL_SPEED_HORIZONTAL = 1.0
SCROLL_SPEED_VERTICAL = 1.0
SCROLL_MOUSE_MARGIN = 5
SCROLL_MOUSE_MAX_X = SCREEN_WIDTH - SCROLL_MOUSE_MARGIN
SCROLL_MOUSE_MAX_Y = SCREEN_HEIGHT - SCROLL_MOUSE_MARGIN

# UI
UI_TOP_BAR = 0.06
UI_SIDE_BAR = 0.1
CONTRACTS_WINDOW_GAP_X = 15
CONTRACTS_WINDOW_GAP_Y = 7
MAX_AVAILABLE_CONTRACTS = 4
UI_CENTRAL_FRAME = (0.8, 0.8)

# Earth params
EARTH_HOUR_ROTATING_FREQ = 5

# Game Value
BUILDING_MAX_LEVEL = 4
