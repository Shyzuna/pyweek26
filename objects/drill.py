import pygame
import os

from settings import settings
from objects.building import Building
from settings.enums import BuildingStates

class Drill(Building):

    def __init__(self, position):

        self.position = position
        self.size = [1, 1]
        self.connections = {'inputs': {'hydrogen_rock': False, 'Electricity': False},
                            'outputs': {'hydrogen_gaz': False}}
        self.max_prod = 2
        self.cur_prod = 0
        self.ratio = 1
        self.consumption = 5

        self.networks = {
            'electric': None
        }

        self.img = pygame.image.load(os.path.join(settings.BUILDINGS_PATH, "DRILL.png"))
        self.img = pygame.transform.scale(self.img, (settings.TILE_WIDTH * self.size[0],
                                                     settings.TILE_HEIGHT * self.size[1]))

        Building.__init__(self, self.position, self.size, self.connections, self.img)

    def updateProduction(self, deltaTime):
        pass

    def updateConsumption(self, deltaTime):
        if self.networks['electric'] is not None:
            nbElectricity = self.networks['electric'].nbResources
            nbCons = self.consumption * deltaTime
            print("drill consomme " + str(self.consumption * deltaTime))
            print("reste dans le reseau " + str(self.networks['electric'].nbResources))
            if nbCons <= nbElectricity:
                self.networks['electric'].nbResources -= nbCons
                self.state = BuildingStates.ON
                print("reste apres conso " + str(self.networks['electric'].nbResources))
            else:
                self.state = BuildingStates.OFF
                print("drill OFF")
