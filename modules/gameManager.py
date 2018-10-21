import pygame

from modules.displayManager import displayManager
from modules.mapManager import mapManager
from objects.resource import Resource
from settings import settings

from settings.enums import ObjectCategory

class GameManager:

    def __init(self):
        pass

    def init(self):
        self.clock = pygame.time.Clock()
        mapManager.init()
        displayManager.init()
        displayManager.createBaseMapSurface(mapManager.baseMap)

    def start(self):
        while 1:
            self.done = False
            while not self.done:
                self.clock.tick(settings.FPS)
                self.deltaTime = self.clock.get_time()
                displayManager.display(mapManager.currentRect, [Resource((50, 50), (50, 50), ObjectCategory.HYDROGEN.value, 100)])


gameManager = GameManager()