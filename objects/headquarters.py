import pygame
import os

from settings import settings
from settings.enums import BuildingsName
from settings.buildingsSettings import ALL_BUILDINGS_SETTINGS
from objects.building import Building


class HeadQuarters(Building):

    def __init__(self, position):

        self.position = position
        self.size = [1, 1]
        self.connections = {'inputs': {'Electricity': False},
                            'outputs': None}

        self.networks = {
            'electric': None
        }

        #self.img = pygame.image.load(os.path.join(settings.BUILDINGS_PATH, "HEADQUARTERS.png"))
        #self.img = pygame.transform.scale(self.img, (settings.TILE_WIDTH * self.size[0],
        #                                             settings.TILE_HEIGHT * self.size[1]))

        Building.__init__(self, self.position, self.connections, ALL_BUILDINGS_SETTINGS[BuildingsName.HEADQUARTERS])

    def updateProduction(self):
        pass

    def update(self):
        pass