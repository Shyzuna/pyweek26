import pygame

from modules.displayManager import displayManager
from modules.mapManager import mapManager
from modules.inputManager import inputManager
from modules.guiManager import guiManager
from settings import settings
from modules.mapGenerator import MapGenerator
from settings.enums import ObjectCategory,BuildingTypes,BuildingShortcuts,Buildings
from objects.network import Network
from state.player import Player
from objects.headquarters import HeadQuarters

from objects.battery import Battery
from objects.crusher import Crusher
from objects.drill import Drill
from objects.solarpanel import SolarPanel

class GameManager:

    def __init__(self):
        pass

    def init(self):
        self.buildingList = {
            BuildingTypes.GENERAL: [],
            BuildingTypes.GATHERER: [(Buildings.CRUSHER, Crusher), (Buildings.DRILL, Drill)],
            BuildingTypes.REFINER: [],
            BuildingTypes.PRODUCER: [(Buildings.SOLARPANEL, SolarPanel)],
            BuildingTypes.CAPACITOR: [(Buildings.BATTERY, Battery)],
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
        self._buildings = [HeadQuarters(position=settings.DEFAULT_HQ_POS, uid=1)]
        self.networks = {
            'electric': []
        }

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

    def createBuildings(self, toBuild):
        for building in toBuild:
            x_tobuild = building.position[0]
            y_tobuild = building.position[1]

            otherBuildingsPosition = [
                (x_tobuild - 1, y_tobuild),
                (x_tobuild, y_tobuild - 1),
                (x_tobuild + 1, y_tobuild),
                (x_tobuild, y_tobuild + 1)
            ]

            # Check other buildings next to the one to build
            for i in range(0, len(otherBuildingsPosition)):
                x = otherBuildingsPosition[i][0]
                y = otherBuildingsPosition[i][1]
                if y in self._buildings and x in self._buildings[y]:
                    otherBuilding = self._buildings[y][x]
                    for networkType, network in building.networks.items():
                        # Check if other building has same network types
                        if networkType in otherBuilding.networks:
                            # If other building network is None create one with the two buildings
                            if otherBuilding.networks[networkType] is None:
                                network = Network()
                                network.addBuildings(building, otherBuilding, networkType)
                                otherBuilding.networks[networkType] = network
                                building.networks[networkType] = network
                                self.networks[networkType].append(network)
                            # Else connect the new building
                            else:
                                otherBuilding.networks[networkType].addBuildings(building, otherBuilding, networkType)

            self._buildings.append(building)

    def removeBuildings(self, toRemove):
        for building in toRemove:
            x_tobuild = building.position[0]
            y_tobuild = building.position[1]

            otherBuildingsPosition = [
                (x_tobuild - 1, y_tobuild),
                (x_tobuild, y_tobuild - 1),
                (x_tobuild + 1, y_tobuild),
                (x_tobuild, y_tobuild + 1)
            ]

            otherBuildingsList = []

            # Check other buildings next to the one to remove
            for i in range(0, len(otherBuildingsPosition)):
                x = otherBuildingsPosition[i][0]
                y = otherBuildingsPosition[i][1]
                if y in self._buildings and x in self._buildings[y]:
                    otherBuilding = self._buildings[y][x]
                    otherBuildingsList.append(otherBuilding)

                    for networkType, network in building.networks.items():
                        # Check if other building has same network types
                        if networkType in otherBuilding.networks:
                            # Remove the connections
                            otherBuilding.networks[networkType].removeConnections(otherBuilding, building)

                            # If no buildings left, remove network
                            if len(otherBuilding.networks[networkType] < 2):
                                self.networks[networkType].remove(otherBuilding.networks[networkType])
                                otherBuilding.networks[networkType] = None
                                continue

            # For all neighbors check if path still exists
            for i in range(0, len(otherBuildingsList) - 1):
                for j in range(i + 1, len(otherBuildingsList)):
                    other1 = otherBuildingsList[i]
                    other2 = otherBuildingsList[j]

                    for networkType, network in other1.networks.items():
                        if networkType in other2.networks and networkType in building.networks:
                            # If not exists split the two networks
                            if not other2.networks[networkType].pathExists(other1, other2):
                                newNetwork = Network(self.networks[networkType].append(other2.networks[networkType].splitNetworks(other1, other2)))

                            # Update buildings
                            for buildingToUpdate in newNetwork.nodes.keys():
                                for build in self._buildings:
                                    if build.id == buildingToUpdate:
                                        build.networks[networkType] = newNetwork


            self._buildings.remove(building)

gameManager = GameManager()
