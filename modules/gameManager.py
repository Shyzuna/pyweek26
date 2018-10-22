import pygame

from modules.displayManager import displayManager
from modules.mapManager import mapManager
from modules.inputManager import inputManager
from modules.guiManager import guiManager
from settings import settings
from modules.mapGenerator import MapGenerator
from settings.enums import ObjectCategory,BuildingTypes
from state.player import Player

from objects.Battery import Battery
from objects.Crusher import Crusher
from objects.Drill import Drill
import objects.SolarPanel as SolarPanel

class GameManager:

    def __init__(self):
        pass

    def init(self):
        self.buildingList = {
            BuildingTypes.GENERAL: [],
            BuildingTypes.GATHERER: [Crusher, Drill],
            BuildingTypes.REFINER: [],
            BuildingTypes.PRODUCER: [SolarPanel.SolarPanel],
            BuildingTypes.CAPACITOR: [Battery],
            BuildingTypes.CONNECTOR: [],
        }
        self.clock = pygame.time.Clock()
        mapManager.init()
        inputManager.init()
        displayManager.init()
        guiManager.init(self.buildingList)
        displayManager.createBaseMapSurface(mapManager.baseMap)
        self._mg = MapGenerator()
        self._resources = self._mg.generateSettingsMap()
        self._player = Player()

    def start(self):
        pygame.event.set_grab(True)

        while not inputManager.done:
            self.clock.tick(settings.FPS)
            deltaTime = self.clock.get_time()

            inputManager.loop()
            (deltaX, deltaY) = mapManager.scroll(inputManager.directionState, deltaTime)
            self.scrollObjects(deltaX, deltaY)
            displayManager.display(mapManager.currentRect, self._resources)
            guiManager.displayGui(displayManager.screen, self._player)
            pygame.display.flip()
        pygame.quit()

    def scrollObjects(self, deltaX, deltaY):
        for resource in self._resources:
            resource.current_x -= deltaX
            resource.current_y -= deltaY



gameManager = GameManager()