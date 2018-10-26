import pygame
import os

from settings import settings
from settings.enums import ObjectCategory
from objects.building import Building
from settings.enums import BuildingStates, BuildingsName
from settings.buildingsSettings import ALL_BUILDINGS_SETTINGS


class SolarPanel(Building):

    def __init__(self, position):

        self.position = position
        self.size = [1, 1]
        self.connections = {'inputs': None,
                            'outputs': {'Electricity': False}}

        self.networks = {
            ObjectCategory.ENERGY: None
        }

        Building.__init__(self, self.position, self.connections, ALL_BUILDINGS_SETTINGS[BuildingsName.SOLARPANEL])

        self.state = BuildingStates.ON

    def updateProduction(self):
        if self.networks[ObjectCategory.ENERGY] is not None:
            self.networks[ObjectCategory.ENERGY].instantProduction += self.buildingData['produce'][ObjectCategory.ENERGY]
            print("solarpanel genere " + str(self.buildingData['produce'][ObjectCategory.ENERGY]))

    def update(self):
        pass

    # def update(self):
    #     # Update production
    #     if gameManager.is_night:
    #         self.cur_prod = 0
    #         # do nothing
    #     else:
    #         self.cur_prod = self.max_prod
    #         to_deliver = self.cur_prod
    #         # Giving away power to non full batteries in same network
    #         for battery in gameManager.get_batteries():
    #             cur_capacity = battery.cur_capacity
    #             max_capacity = battery.max_capacity
    #             if battery.is_full():
    #                 # go to next battery
    #                 pass
    #             elif cur_capacity + to_deliver <= max_capacity:
    #                 # this one can take everything
    #                 battery.update_capacity(to_deliver)
    #                 to_deliver = 0
    #             else:
    #                 # partial delivery
    #                 battery.fill()
    #                 to_deliver = to_deliver - (max_capacity - cur_capacity)
    #
    #     # TODO Update connections array
