import pygame

from modules.displayManager import displayManager
from modules.mapManager import mapManager
from modules.inputManager import inputManager
from settings import settings
from modules.mapGenerator import MapGenerator

from settings.enums import ObjectCategory

class GameManager:

    def __init__(self):
        pass

    def init(self):
        self.clock = pygame.time.Clock()
        mapManager.init()
        inputManager.init()
        displayManager.init()
        displayManager.createBaseMapSurface(mapManager.baseMap)
        self._mg = MapGenerator()
        self._resources = self._mg.generateSettingsMap()

    def start(self):
        while not inputManager.done:
            self.clock.tick(settings.FPS)
            deltaTime = self.clock.get_time()

            inputManager.loop()
            (deltaX, deltaY) = mapManager.scroll(inputManager.directionState, deltaTime)
            self.scrollObjects(deltaX, deltaY)
            displayManager.display(mapManager.currentRect, self._resources)
        pygame.quit()

    def scrollObjects(self, deltaX, deltaY):
        for resource in self._resources:
            print (deltaX)
            print (deltaY)
            resource.current_x -= deltaX
            resource.current_y -= deltaY



gameManager = GameManager()