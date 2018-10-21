import pygame
from settings import settings

class MapManager:

    def __init__(self):
        pass

    def init(self):
        self.resourcesObject = []

        # Current displayed part of map
        self.currentRect = pygame.Rect(0, 0, settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)

        self.createBaseMap()

    def createBaseMap(self):
        self.baseMap = []

        for i in range(0, settings.TILES_NUM_HEIGHT):
            line = []
            for j in range(0, settings.TILES_NUM_WITDH):
                line.append(0)
            self.baseMap.append(line)


mapManager = MapManager()
