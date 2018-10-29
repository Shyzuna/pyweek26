import pygame
import os
from modules.displayManager import displayManager
from modules.mapManager import mapManager
from modules.inputManager import inputManager
from modules.guiManager import guiManager
from modules.researchManager import researchManager
from settings import settings
from modules.mapGenerator import MapGenerator
from settings.enums import ObjectCategory, BuildingTypes, BuildingStates, BuildingsName
from objects.network import Network
from objects.producingBuilding import ProducingBuilding
from objects.consumingBuilding import ConsumingBuilding
from objects.stockingBuilding import StockingBuilding
from objects.transmitter import Transmitter
from objects.earth import Earth
from state.player import Player
from settings.buildingsSettings import ALL_BUILDINGS_SETTINGS
from objects.battery import Battery
from objects.crusher import Crusher
from objects.drillHydrogen import DrillHydrogen
from objects.drillDihydrogen import DrillDiHydrogen
from objects.drillTrihydrogen import DrillTriHydrogen
from objects.solarpanel import SolarPanel
from objects.headquarters import HeadQuarters
from objects.warehouseHydrogen import WarehouseHydrogen
from objects.hydrogenPlant import HydrogenPlant
from objects.dihydrogenPlant import DiHydrogenPlant
from objects.hydrogenCombiner import HydrogenCombiner
from objects.dihydrogenCombiner import DiHydrogenCombiner
from objects.warehouseDihydrogen import WarehouseDiHydrogen
from objects.warehouseTrihydrogen import WarehouseTriHydrogen
from objects.warehouseTrihelium import WarehouseTriHelium
from objects.trihydrogenPlant import TriHydrogenPlant
from objects.triHeliumPlant import TriHeliumPlant

class GameManager:

    def __init__(self):
        pass

    def init(self):
        self._player = Player()
        baseHq = HeadQuarters(position=settings.DEFAULT_HQ_POS)
        baseHq.state = BuildingStates.ON

        self.buildingList = {
            BuildingTypes.GATHERER: {BuildingsName.DRILL_HYDROGEN: (DrillHydrogen, False),
                                     BuildingsName.DRILL_DIHYDROGEN: (DrillDiHydrogen, False),
                                     BuildingsName.DRILL_TRIHYDROGEN: (DrillTriHydrogen, False),
                                     BuildingsName.CRUSHER: (Crusher, False)},
            BuildingTypes.REFINER: {BuildingsName.HYDROGEN_COMBINER: (HydrogenCombiner, False),
                                    BuildingsName.DIHYDROGEN_COMBINER: (DiHydrogenCombiner, False)},
            BuildingTypes.PRODUCER: {BuildingsName.SOLARPANEL: (SolarPanel, True),
                                     BuildingsName.HYDROGEN_PLANT: (HydrogenPlant, False),
                                     BuildingsName.DIHYDROGEN_PLANT: (DiHydrogenPlant, False),
                                    BuildingsName.TRIHYDROGEN_PLANT: (TriHydrogenPlant, False),
                                    BuildingsName.TRIHELIUM_PLANT: (TriHeliumPlant, False)},
            BuildingTypes.CAPACITOR: {BuildingsName.BATTERY: (Battery, True),
                                      BuildingsName.WAREHOUSE_HYDROGEN: (WarehouseHydrogen, False),
                                      BuildingsName.WAREHOUSE_DIHYDROGEN: (WarehouseDiHydrogen, False),
                                      BuildingsName.WAREHOUSE_TRIHYDROGEN: (WarehouseTriHydrogen, False),
                                      BuildingsName.WAREHOUSE_TRIHELIUM: (WarehouseTriHelium, False)}
        }
        self._earth = Earth()
        self.clock = pygame.time.Clock()
        self._mg = MapGenerator()
        self._resources = self._mg.generateSettingsMap()
        self.instantProd = 0
        self.networks = []
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(settings.MUSIC_PATH, 'moonLake.mp3'))
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
        displayManager.init()
        mapManager.init()
        inputManager.init()
        researchManager.init(baseHq)
        guiManager.init(self.buildingList, self._earth)
        displayManager.createBaseMapSurface(mapManager.baseMap)
        self._buildings = {  # Col / Row
            settings.DEFAULT_HQ_POS[1]: {settings.DEFAULT_HQ_POS[0]: baseHq},
        }
        if settings.DEFAULT_TRANSMITTER_POS[1] in self._buildings:
            self._buildings[settings.DEFAULT_TRANSMITTER_POS[1]].update({settings.DEFAULT_TRANSMITTER_POS[0]: Transmitter(position=settings.DEFAULT_TRANSMITTER_POS, earth=self._earth)})
        else:
            self._buildings.update({settings.DEFAULT_TRANSMITTER_POS[1]: {settings.DEFAULT_TRANSMITTER_POS[0]: Transmitter(position=settings.DEFAULT_TRANSMITTER_POS, earth=self._earth)}})

    def start(self):
        #pygame.event.set_grab(True)

        time_since_update_res = 0
        time_since_hour_changed = 0

        while not inputManager.done:
            self.clock.tick(settings.FPS)
            deltaTime = self.clock.get_time()
            time_since_update_res += deltaTime
            time_since_hour_changed += deltaTime

            # Update
            researchManager.update(deltaTime)
            inputManager.loop(mapManager.currentRect)
            mapManager.scroll(inputManager.directionState, deltaTime)

            if inputManager.toDelete is not None:
                inputManager.deleteMode = False
                toDeleteX = inputManager.toDelete[0]
                toDeleteY = inputManager.toDelete[1]
                print("remove en " + str(toDeleteX) + " " + str(toDeleteY))
                inputManager.toDelete = None
                if toDeleteY in self._buildings and toDeleteX in self._buildings[toDeleteY]:
                    self.removeBuilding(self._buildings[toDeleteY][toDeleteX])

            guiManager.updateGui(self._player, inputManager.mousePos)

            for network in self.networks:
                network.update()

            self._earth.updateDisplayedHour(time_since_hour_changed)
            if time_since_update_res > 1000:
                time_since_update_res = 0
                self.instantProd = 0
                # Update buildings
                # First compute instant prod, stock
                for y in self._buildings:
                    for x in self._buildings[y]:
                        if isinstance(self._buildings[y][x], ProducingBuilding):
                            self._buildings[y][x].produce()
                        if isinstance(self._buildings[y][x], StockingBuilding):
                            self._buildings[y][x].produceStock()

                for network in self.networks:
                    self.instantProd += network.instantProduction[ObjectCategory.ENERGY]

                # Then apply consumption
                for y in self._buildings:
                    for x in self._buildings[y]:
                        if isinstance(self._buildings[y][x], ConsumingBuilding):
                            self._buildings[y][x].consume()
                        if isinstance(self._buildings[y][x], Transmitter):
                            self._earth.setTransmitterOn(self._buildings[y][x].state == BuildingStates.ON)

                # Then apply stock
                for objectType in ObjectCategory:
                    if objectType != ObjectCategory.CREDITS:
                        self._player._resources[objectType] = 0

                if self._earth.isSending() and self._earth.isTransmitterOn():
                    batteriesList = []
                    transmitter = None
                    for y in self._buildings:
                        for x in self._buildings[y]:
                            if isinstance(self._buildings[y][x], Battery):
                                batteriesList.append(self._buildings[y][x])
                            if isinstance(self._buildings[y][x], Transmitter):
                                transmitter = self._buildings[y][x]
                    self._earth.sendEnergy(transmitter, batteriesList)


                for y in self._buildings:
                    for x in self._buildings[y]:
                        building = self._buildings[y][x]

                        if isinstance(building, StockingBuilding):
                            building.stock()
                            self._player._resources[building.type] += building.cur_capacity[building.type]

            # Earth
            if time_since_hour_changed > settings.EARTH_HOUR_ROTATING_FREQ * 1000:
                time_since_hour_changed = 0
                self._earth.changeHour()

            # Display
            displayManager.display(mapManager.currentRect, self._resources, self._buildings)
            guiManager.displayGui(displayManager.screen)
            pygame.display.flip()
        pygame.quit()

    def unlockRes(self, res):
        self._player.unlockRes(res)

    def unlockBuildings(self, buildings):
        for cat, d in self.buildingList.items():
            for name, value in d.items():
                if name in buildings:
                    self.buildingList[cat][name] = (value[0], True)
        guiManager.setBuildingList(self.buildingList)
        guiManager.createSideButton()

    def upgradeBuildings(self, buildingType, param, value):
        if param in ALL_BUILDINGS_SETTINGS[buildingType].keys():
            if type(ALL_BUILDINGS_SETTINGS[buildingType][param]) == dict:
                for k, v in ALL_BUILDINGS_SETTINGS[buildingType][param].items():
                    if type(v) == list:
                        v = [i * value for i in v]
                    else:
                        v *= value
                    ALL_BUILDINGS_SETTINGS[buildingType][param][k] = v
                print(ALL_BUILDINGS_SETTINGS[buildingType][param])
            else:
                ALL_BUILDINGS_SETTINGS[buildingType][param] *= value

        if buildingType in [BuildingsName.BATTERY]:
            storage = 0
            resType = None
            for y in self._buildings:
                for x in self._buildings[y]:
                    if self._buildings[y][x].buildingData['name'] == buildingType.value:
                        building = self._buildings[y][x]
                        if isinstance(building, StockingBuilding):
                            resType = building.type
                            storage += building.geCurrentMaxStock()
            self._player.upgradeResourceCapTo(resType, storage)

    def getInstantProd(self):
        return self.instantProd

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
        build = self.getBuildingAt(tPos)
        if build is not None:
            return build
        res = self.getResourceAt(tPos)

        return res

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

    def getPlayer(self):
        return self._player

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

    def createBuilding(self, building):
        if self._player._resources[ObjectCategory.CREDITS] > building.buildingData['cost'][ObjectCategory.CREDITS][0]:
            self._player._resources[ObjectCategory.CREDITS] -= building.buildingData['cost'][ObjectCategory.CREDITS][0]
        else:
            return

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
                # If other building network is None create one with the two buildings
                if otherBuilding.network is None:
                    # If current building has no network yet create one with the two buildings
                    if building.network is None:
                        network = Network()
                        network.addConnections(building, otherBuilding)
                        otherBuilding.network = network
                        building.network = network
                        print("Création d'un nouveau network")
                        print("Nouveau 1 " + str(building.position[0]) + " " + str(
                            building.position[1]))
                        print("Nouveau 2 " + str(otherBuilding.position[0]) + " " + str(
                            otherBuilding.position[1]))
                        self.networks.append(network)
                    # Else add other building to existing network
                    else:
                        print("Ajout network other 1")
                        print("Ajout network other 1 1 " + str(building.position[0]) + " " + str(
                            building.position[1]))
                        print("Ajout network other 1 2 " + str(otherBuilding.position[0]) + " " + str(
                            otherBuilding.position[1]))
                        building.network.addConnections(otherBuilding, building)
                        otherBuilding.network = building.network
                # Else connect the new building
                else:
                    # If current building has no network yet add to existing one
                    if building.network is None:
                        print("Ajout network other 2 ")
                        print("Ajout network other 2 1 " + str(building.position[0]) + " " + str(
                            building.position[1]))
                        print("Ajout network other 2 2 " + str(otherBuilding.position[0]) + " " + str(
                            otherBuilding.position[1]))
                        otherBuilding.network.addConnections(building, otherBuilding)
                        building.network = otherBuilding.network
                    # Else merge the two networks if differents
                    elif otherBuilding.network != building.network:
                        otherBuilding.network.mergeConnections(building.network)
                        otherBuilding.network.addConnections(building, otherBuilding)
                        print("Merge network ")
                        print("Merge network 1 " + str(building.position[0]) + " " + str(
                            building.position[1]))
                        print("Merge network 2 " + str(otherBuilding.position[0]) + " " + str(
                            otherBuilding.position[1]))
                        # Update other buildings network
                        for abs in self._buildings.values():
                            for bUpdate in abs.values():
                                if bUpdate.id in building.network.nodes.keys():
                                    if bUpdate.network in self.networks:
                                        self.networks.remove(bUpdate.network)
                                        print(str(self.networks))
                                    bUpdate.network = otherBuilding.network
                        building.network = otherBuilding.network
                    # Else just update connections
                    else:
                        print("Update network ")
                        print("Update network 1 " + str(building.position[0]) + " " + str(
                            building.position[1]))
                        print("Update network 2 " + str(otherBuilding.position[0]) + " " + str(
                            otherBuilding.position[1]))
                        otherBuilding.network.addConnections(building, otherBuilding)

        if building.position[1] in self._buildings:
            self._buildings[building.position[1]].update({building.position[0]: building})
        else:
            self._buildings.update({building.position[1]: {building.position[0]: building}})

        if isinstance(building, StockingBuilding):
            self._player._resourcesCap[building.type] += building.buildingData['stock'][building.type][building.level]

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

                # Remove the connections if not already None
                print("test connection adjacente " + str(otherBuilding.position[0]) + " " + str(
                    otherBuilding.position[1]))
                if otherBuilding.network is not None:
                    print("remove connection adjacente " + str(otherBuilding.position[0]) + " " + str(otherBuilding.position[1]))
                    otherBuilding.network.removeConnections(otherBuilding, building)

                    # If no buildings left, remove network
                    if len(otherBuilding.network.nodes.keys()) < 2:
                        if otherBuilding.network in self.networks:
                            self.networks.remove(otherBuilding.network)
                        otherBuilding.network = None
                    # Else network has to split
                    else:
                        otherBuildingsList.append(otherBuilding)


        # For all neighbors check if path still exists
        for i in range(0, len(otherBuildingsList) - 1):
            for j in range(i + 1, len(otherBuildingsList)):
                other1 = otherBuildingsList[i]
                other2 = otherBuildingsList[j]
                # If not exists split the two networks
                if not other2.network.pathExists(other1, other2):
                    newNetwork = Network()
                    newNetwork.nodes = other2.network.splitNetworks()
                    self.networks.append(newNetwork)

                    # Update buildings
                    for buildingToUpdate in newNetwork.nodes.keys():
                        for abs in self._buildings.values():
                            for build in abs.values():
                                if build.id == buildingToUpdate:
                                    build.network = newNetwork

        print("remove en " + str(building.position[0]) + " " + str(building.position[1]))
        self._buildings[building.position[1]].pop(building.position[0])
        print(self._buildings)

        if isinstance(building, StockingBuilding):
            self._player._resourcesCap[building.type] -= building.buildingData['stock'][building.type][building.level]

gameManager = GameManager()
