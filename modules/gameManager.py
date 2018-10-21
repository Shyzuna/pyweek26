import pygame

from modules.displayManager import displayManager
from modules.mapManager import mapManager
from settings import settings

class GameManager:

    def __init__(self):
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
                displayManager.display(mapManager.currentRect)


gameManager = GameManager()