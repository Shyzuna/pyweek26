import os
from settings.enums import ObjectCategory

# Generation
SEED = None  #93917774  # None for random
SEED_POWER = 8
DELTA_PERCENT = 0.1
RESOURCES = [ObjectCategory.HYDROGEN, ObjectCategory.DIHYGROGEN, ObjectCategory.TRIHYGROGEN, ObjectCategory.TRIHELIUM]
SPOT_NUMBERS = [0.1, 0.06, 0.03, 0.02]  # percent
REPARTITION_NUMBERS = [0.4, 0.2, 0.14, 0.06]  # percent
TOTAL_RES = 1000

# Display
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 800
FPS = 60

# Paths
TILES_PATH = os.path.join('data', 'tiles')
RESOURCES_PATH = os.path.join('data', 'resources')

# Map parameters
TILE_WIDTH = 60
TILE_HEIGHT = 60
TILES_NUM_WITDH = 64
TILES_NUM_HEIGHT = 64
MAP_WIDTH = TILE_WIDTH * TILES_NUM_WITDH
MAP_HEIGHT = TILE_HEIGHT * TILES_NUM_HEIGHT
MAP_SIZE = (20, 20)
