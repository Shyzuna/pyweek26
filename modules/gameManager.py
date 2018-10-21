import pygame

from modules.displayManager import displayManager
from modules.mapManager import mapManager
from objects.resource import Resource
from settings import settings
from modules.mapGenerator import MapGenerator

from settings.enums import ObjectCategory

class GameManager:

    def __init__(self):
        pass

    def init(self):
        self.clock = pygame.time.Clock()
        mapManager.init()
        displayManager.init()
        displayManager.createBaseMapSurface(mapManager.baseMap)
        self._mg = MapGenerator()
        self._resources = self._mg.generateSettingsMap()

    def start(self):
        #while 1:
        self.done = False
        while not self.done:

            # Events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.done = True

            self.clock.tick(settings.FPS)
            self.deltaTime = self.clock.get_time()
            displayManager.display(mapManager.currentRect, self._resources)
        pygame.quit()


gameManager = GameManager()