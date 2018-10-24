import pygame
import os

from settings import settings
from objects.building import Building
from settings.enums import ObjectCategory
import modules.gameManager

class Crusher(Building):

    def __init__(self, position):

        self.position = position
        self.size = [1, 1]
        self.connections = {'inputs': {'helium_rock': False, 'Electricity': False},
                            'outputs': {'helium_gaz': False}}
        self.max_prod = 2
        self.cur_prod = 0
        self.ratio = 1
        self.consumption = 1

        self.networks = {
            'electric': None
        }

        self.img = pygame.image.load(os.path.join(settings.BUILDINGS_PATH, "CRUSHER.png"))
        self.img = pygame.transform.scale(self.img, (settings.TILE_WIDTH * self.size[0],
                                                     settings.TILE_HEIGHT * self.size[1]))

        self.linkedRes = modules.gameManager.gameManager.getResourceAt(self.position)

        Building.__init__(self, self.position, self.size, self.connections, self.img, [ObjectCategory.TRIHELIUM])

    def updateProduction(self, deltaTime):
        pass

    def updateConsumption(self, deltaTime):
        pass
