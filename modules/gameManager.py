import pygame

from modules.displayManager import displayManager
from modules.mapManager import mapManager
from modules.inputManager import inputManager
from modules.guiManager import guiManager
from settings import settings
from modules.mapGenerator import MapGenerator
from settings.enums import ObjectCategory
from settings.enums import BuildingShortcuts
from state.player import Player
from objects.battery import Battery
from objects.solarpanel import SolarPanel
from objects.drill import Drill
from objects.crusher import Crusher
from objects.headquarters import HeadQuarters

class GameManager:

    def __init__(self):
        pass

    def init(self):
        self.clock = pygame.time.Clock()
        mapManager.init()
        inputManager.init()
        displayManager.init()
        guiManager.init()
        displayManager.createBaseMapSurface(mapManager.baseMap)
        self._mg = MapGenerator()
        self._resources = self._mg.generateSettingsMap()
        self._player = Player()
        self._buildings = [HeadQuarters(position=settings.DEFAULT_HQ_POS, uid=1)]

    def start(self):
        pygame.event.set_grab(True)

        while not inputManager.done:
            self.clock.tick(settings.FPS)
            deltaTime = self.clock.get_time()

            inputManager.loop()
            (deltaX, deltaY) = mapManager.scroll(inputManager.directionState, deltaTime)
            self.scrollObjects(deltaX, deltaY)
            if inputManager.keyPressed is not None:
                self.processKeyPressed(inputManager.keyPressed, inputManager.mousePosInTiles)
            displayManager.display(mapManager.currentRect, self._resources, self._buildings)
            guiManager.displayGui(displayManager.screen, self._player)
            pygame.display.flip()
        pygame.quit()

    def scrollObjects(self, deltaX, deltaY):
        for resource in self._resources:
            resource.current_x -= deltaX
            resource.current_y -= deltaY

    def processKeyPressed(self, keyPressed, mousePosInTiles):
        print(self._buildings)
        if keyPressed in [shortcut.value for shortcut in BuildingShortcuts]:
            print(keyPressed)
            print(BuildingShortcuts['BATTERY'])
            if keyPressed == BuildingShortcuts['BATTERY'].value:
                self.addBuilding(buildingType='BATTERY', posInTiles=mousePosInTiles)
            elif keyPressed == BuildingShortcuts['SOLARPANEL'].value:
                self.addBuilding(buildingType='SOLARPANEL', posInTiles=mousePosInTiles)
            elif keyPressed == BuildingShortcuts['DRILL'].value:
                self.addBuilding(buildingType='DRILL', posInTiles=mousePosInTiles)
            elif keyPressed == BuildingShortcuts['CRUSHER'].value:
                self.addBuilding(buildingType='CRUSHER', posInTiles=mousePosInTiles)

    def getNewBuildingUid(self):
        max_uid = 1
        for building in self._buildings:
            if building.uid > max_uid:
                max_uid = building.uid

        return max_uid + 1

    def addBuilding(self, buildingType, posInTiles):
        uid = self.getNewBuildingUid()

        #TODO: avoid overlapping
        print("addBuilding flag")
        if buildingType == 'BATTERY':
            print("battery")
            self._buildings.append(Battery(position=posInTiles, uid=uid))
        if buildingType == 'SOLARPANEL':
            print("SOLARPANEL")
            self._buildings.append(SolarPanel(position=posInTiles, uid=uid))
        elif buildingType == 'CRUSHER':
            print("CRUSHER")
            self._buildings.append(Crusher(position=posInTiles, uid=uid))
        elif buildingType == 'DRILL':
            print("DRILL")
            self._buildings.append(Drill(position=posInTiles, uid=uid))

    def deleteBuilding(self, pos):
        remove_index = -1

        for building, index in self._buildings:
            # TODO: position with size matching function
            if building.position == pos:
                remove_index = index

        if remove_index >= 0:
            self._buildings.remove(remove_index)
            return True
        else:
            return False


gameManager = GameManager()