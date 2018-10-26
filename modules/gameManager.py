import pygame
import math

from modules.displayManager import displayManager
from modules.mapManager import mapManager
from modules.inputManager import inputManager
from modules.guiManager import guiManager
from modules.contractManager import contractManager
from settings import settings
from modules.mapGenerator import MapGenerator
from settings.enums import ObjectCategory,BuildingTypes,BuildingShortcuts,BuildingsName
from objects.network import Network
from state.player import Player

from objects.battery import Battery
from objects.crusher import Crusher
from objects.drill import Drill
from objects.solarpanel import SolarPanel
from objects.headquarters import HeadQuarters

class GameManager:

    def __init__(self):
        pass

    def init(self):
        self.buildingList = {
            BuildingTypes.GENERAL: [(BuildingsName.HEADQUARTERS, HeadQuarters)],
            BuildingTypes.GATHERER: [(BuildingsName.CRUSHER, Crusher), (BuildingsName.DRILL, Drill)],
            BuildingTypes.REFINER: [],
            BuildingTypes.PRODUCER: [(BuildingsName.SOLARPANEL, SolarPanel)],
            BuildingTypes.CAPACITOR: [(BuildingsName.BATTERY, Battery)],
            BuildingTypes.CONNECTOR: [],
        }
        self.clock = pygame.time.Clock()
        self._mg = MapGenerator()
        self._resources = self._mg.generateSettingsMap()
        displayManager.init()
        mapManager.init()
        inputManager.init()
        guiManager.init(self.buildingList)
        displayManager.createBaseMapSurface(mapManager.baseMap)
        self._player = Player()
        self._buildings = {  # Col / Row
            settings.DEFAULT_HQ_POS[1]: {settings.DEFAULT_HQ_POS[0]: HeadQuarters(position=settings.DEFAULT_HQ_POS)}
        }
        self.networks = {
            ObjectCategory.ENERGY: []
        }

    def start(self):
        #pygame.event.set_grab(True)

        time_since_update_res = 0

        while not inputManager.done:
            self.clock.tick(settings.FPS)
            deltaTime = self.clock.get_time()
            time_since_update_res += deltaTime

            # Update
            inputManager.loop(mapManager.currentRect)
            mapManager.scroll(inputManager.directionState, deltaTime)
            if inputManager.keyPressed is not None:
                self.processKeyPressed(inputManager.keyPressed, inputManager.absoluteMousePosInTiles)
                print("Current pos in tiles: ", inputManager.absoluteMousePosInTiles)

            if inputManager.toDelete is not None:
                inputManager.deleteMode = False
                toDeleteX = inputManager.toDelete[0]
                toDeleteY = inputManager.toDelete[1]
                print("remove en " + str(toDeleteX) + " " + str(toDeleteY))
                inputManager.toDelete = None
                if toDeleteY in self._buildings and toDeleteX in self._buildings[toDeleteY]:
                    self.removeBuilding(self._buildings[toDeleteY][toDeleteX])

            guiManager.updateGui(self._player, inputManager.mousePos)

            for networkList in self.networks.values():
                for network in networkList:
                    network.update()

            if time_since_update_res > 1000:
                time_since_update_res = 0
                # Update buildings
                # First compute instant prod, stock
                for y in self._buildings:
                    for x in self._buildings[y]:
                        self._buildings[y][x].updateProduction()

                # Then apply consumption
                for y in self._buildings:
                    for x in self._buildings[y]:
                        self._buildings[y][x].update()

                # Then apply stock
                self._player._resources[ObjectCategory.ENERGY] = 0
                for y in self._buildings:
                    for x in self._buildings[y]:
                        building = self._buildings[y][x]
                        building.updateStock()

                        if isinstance(building, Battery):
                            self._player._resources[ObjectCategory.ENERGY] += building.cur_capacity

            # Display
            displayManager.display(mapManager.currentRect, self._resources, self._buildings)
            guiManager.displayGui(displayManager.screen)
            pygame.display.flip()
        pygame.quit()

    def checkIsBuildingTile(self, tilePos):
        tx, ty = tilePos
        borderSize = settings.BORDER_TILES_NUM
        if (borderSize + settings.TILES_NUM_WIDTH + 1) > tx > (borderSize - 1) and \
                (borderSize + settings.TILES_NUM_HEIGHT + 1) > ty > (borderSize - 1):
            # check buildings
            if ty in self._buildings and tx in self._buildings[ty]:
                return True
        return False

    def checkElementAt(self, mPos):
        tPos = mapManager.getTilePosFromReal(mPos)
        res = self.getResourceAt(tPos)
        if res is not None:
            return res
        build = self.getBuildingAt(tPos)
        return build

    def checkTileValid(self, tilePos, allowedSpot):
        # in Map
        tx, ty = tilePos
        borderSize = settings.BORDER_TILES_NUM
        if (borderSize + settings.TILES_NUM_WIDTH + 1) > tx > (borderSize - 1) and\
                (borderSize + settings.TILES_NUM_HEIGHT + 1) > ty > (borderSize - 1):
            if allowedSpot is None:
                # check res
                for r in self._resources:
                    if r.getPos() == tilePos:
                        return False
                # check buildings
                if ty in self._buildings and tx in self._buildings[ty]:
                    return False
                return True
            else:
                # check buildings
                if ty in self._buildings and tx in self._buildings[ty]:
                    return False

                # check allowed resource
                for r in self._resources:
                    if r.getPos() == tilePos and r.getCategory() in allowedSpot:
                        return True
        return False

    def getResourceAt(self, tilePos):
        # get resource at
        for r in self._resources:
            if r.getPos() == tilePos:
                return r
        return None

    def getBuildingAt(self, tilePos):
        tx, ty = tilePos
        if ty in self._buildings and tx in self._buildings[ty]:
            return self._buildings[ty][tx]
        return None

    def processKeyPressed(self, keyPressed, mousePosInTiles):
        print(self._buildings)
        if keyPressed in [shortcut.value for shortcut in BuildingShortcuts] and self.isPosInMap(mousePosInTiles):
                print("key pressed: ", keyPressed)
                if keyPressed == BuildingShortcuts['BATTERY'].value:
                    self.addBuilding(buildingType='BATTERY', posInTiles=mousePosInTiles)
                elif keyPressed == BuildingShortcuts['SOLARPANEL'].value:
                    self.addBuilding(buildingType='SOLARPANEL', posInTiles=mousePosInTiles)
                elif keyPressed == BuildingShortcuts['DRILL'].value:
                    self.addBuilding(buildingType='DRILL', posInTiles=mousePosInTiles)
                elif keyPressed == BuildingShortcuts['CRUSHER'].value:
                    self.addBuilding(buildingType='CRUSHER', posInTiles=mousePosInTiles)


    def isPosInMap(self, posInTiles):
        return True

    def addBuilding(self, buildingType, posInTiles):

        #TODO: avoid overlapping
        print("addBuilding flag")
        building = None
        if buildingType == 'BATTERY':
            print("battery")
            building = Battery(position=posInTiles)
            self._player._resourcesCap[ObjectCategory.ENERGY] += building.max_capacity
        if buildingType == 'SOLARPANEL':
            print("SOLARPANEL")
            building = SolarPanel(position=posInTiles)
        elif buildingType == 'CRUSHER':
            print("CRUSHER")
            building = Crusher(position=posInTiles)
        elif buildingType == 'DRILL':
            print("DRILL")
            building = Drill(position=posInTiles)

        self.createBuilding(building)
        print(self._buildings)

    def createBuilding(self, building):
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
                            # If current building has no network yet create one with the two buildings
                            if building.networks[networkType] is None:
                                network = Network()
                                network.addConnections(building, otherBuilding)
                                otherBuilding.networks[networkType] = network
                                building.networks[networkType] = network
                                print("Création d'un nouveau network")
                                print("Nouveau 1 " + str(building.position[0]) + " " + str(
                                    building.position[1]))
                                print("Nouveau 2 " + str(otherBuilding.position[0]) + " " + str(
                                    otherBuilding.position[1]))
                                self.networks[networkType].append(network)
                            # Else add other building to existing network
                            else:
                                print("Ajout network other 1")
                                print("Ajout network other 1 1 " + str(building.position[0]) + " " + str(
                                    building.position[1]))
                                print("Ajout network other 1 2 " + str(otherBuilding.position[0]) + " " + str(
                                    otherBuilding.position[1]))
                                building.networks[networkType].addConnections(otherBuilding, building)
                                otherBuilding.networks[networkType] = building.networks[networkType]
                        # Else connect the new building
                        else:
                            # If current building has no network yet add to existing one
                            if building.networks[networkType] is None:
                                print("Ajout network other 2 ")
                                print("Ajout network other 2 1 " + str(building.position[0]) + " " + str(
                                    building.position[1]))
                                print("Ajout network other 2 2 " + str(otherBuilding.position[0]) + " " + str(
                                    otherBuilding.position[1]))
                                otherBuilding.networks[networkType].addConnections(building, otherBuilding)
                                building.networks[networkType] = otherBuilding.networks[networkType]
                            # Else merge the two networks if differents
                            elif otherBuilding.networks[networkType] != building.networks[networkType]:
                                otherBuilding.networks[networkType].mergeConnections(building.networks[networkType])
                                otherBuilding.networks[networkType].addConnections(building, otherBuilding)
                                print("Merge network ")
                                print("Merge network 1 " + str(building.position[0]) + " " + str(
                                    building.position[1]))
                                print("Merge network 2 " + str(otherBuilding.position[0]) + " " + str(
                                    otherBuilding.position[1]))
                                # Update other buildings network
                                for abs in self._buildings.values():
                                    for bUpdate in abs.values():
                                        if bUpdate.id in building.networks[networkType].nodes.keys():
                                            if bUpdate.networks[networkType] in self.networks[networkType]:
                                                self.networks[networkType].remove(bUpdate.networks[networkType])
                                                print(str(self.networks[networkType]))
                                            bUpdate.networks[networkType] = otherBuilding.networks[networkType]
                                building.networks[networkType] = otherBuilding.networks[networkType]
                            # Else just update connections
                            else:
                                print("Update network ")
                                print("Update network 1 " + str(building.position[0]) + " " + str(
                                    building.position[1]))
                                print("Update network 2 " + str(otherBuilding.position[0]) + " " + str(
                                    otherBuilding.position[1]))
                                otherBuilding.networks[networkType].addConnections(building, otherBuilding)



        if building.position[1] in self._buildings:
            self._buildings[building.position[1]].update({building.position[0]: building})
        else:
            self._buildings.update({building.position[1]: {building.position[0]: building}})

        if isinstance(building, Battery):
            self._player._resourcesCap[ObjectCategory.ENERGY] += building.buildingData['capacity'][ObjectCategory.ENERGY]

    def removeBuilding(self, building):
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

                for networkType, network in building.networks.items():
                    # Check if other building has same network types
                    if networkType in otherBuilding.networks:
                        # Remove the connections if not already None
                        print("test connection adjacente " + str(otherBuilding.position[0]) + " " + str(
                            otherBuilding.position[1]))
                        if otherBuilding.networks[networkType] is not None:
                            print("remove connection adjacente " + str(otherBuilding.position[0]) + " " + str(otherBuilding.position[1]))
                            otherBuilding.networks[networkType].removeConnections(otherBuilding, building)

                            # If no buildings left, remove network
                            if len(otherBuilding.networks[networkType].nodes.keys()) < 2:
                                if otherBuilding.networks[networkType] in self.networks[networkType]:
                                    self.networks[networkType].remove(otherBuilding.networks[networkType])
                                otherBuilding.networks[networkType] = None
                            # Else network has to split
                            else:
                                otherBuildingsList.append(otherBuilding)


        # For all neighbors check if path still exists
        for i in range(0, len(otherBuildingsList) - 1):
            for j in range(i + 1, len(otherBuildingsList)):
                other1 = otherBuildingsList[i]
                other2 = otherBuildingsList[j]

                for networkType, network in other1.networks.items():
                    if networkType in other2.networks and networkType in building.networks:
                        # If not exists split the two networks
                        if not other2.networks[networkType].pathExists(other1, other2):
                            newNetwork = Network()
                            newNetwork.nodes = other2.networks[networkType].splitNetworks()
                            self.networks[networkType].append(newNetwork)

                            # Update buildings
                            for buildingToUpdate in newNetwork.nodes.keys():
                                for abs in self._buildings.values():
                                    for build in abs.values():
                                        if build.id == buildingToUpdate:
                                            build.networks[networkType] = newNetwork

        print("remove en " + str(building.position[0]) + " " + str(building.position[1]))
        self._buildings[building.position[1]].pop(building.position[0])
        print(self._buildings)

        if isinstance(building, Battery):
            self._player._resourcesCap[ObjectCategory.ENERGY] -= building.max_capacity

gameManager = GameManager()
