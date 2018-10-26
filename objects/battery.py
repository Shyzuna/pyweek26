import pygame
import os

from settings import settings
from settings.enums import ObjectCategory
from objects.building import Building
from settings.enums import BuildingsName
from settings.buildingsSettings import ALL_BUILDINGS_SETTINGS


class Battery(Building):

    def __init__(self, position):

        self.position = position
        self.size = [1, 1]
        self.connections = {'inputs': {'Electricity': False},
                            'outputs': {'Electricity': False}}

        self.cur_capacity = 0

        self.networks = {
            ObjectCategory.ENERGY: None
        }

        Building.__init__(self, self.position, self.connections, ALL_BUILDINGS_SETTINGS[BuildingsName.BATTERY])

    def update_capacity(self, value):
        overflow = 0
        max_capacity = self.buildingData['capacity'][ObjectCategory.ENERGY]

        if max_capacity >= self.cur_capacity + value:
            overflow = self.cur_capacity - max_capacity + value
            self.cur_capacity += value

        return overflow

    def is_full(self):
        max_capacity = self.buildingData['capacity'][ObjectCategory.ENERGY]
        if self.cur_capacity == max_capacity:
            return True
        else:
            return False

    def is_empty(self):
        if self.cur_capacity == 0:
            return True
        else:
            return False

    def fill(self):
        max_capacity = self.buildingData['capacity'][ObjectCategory.ENERGY]
        self.cur_capacity = max_capacity

    def empty(self):
        self.cur_capacity = 0

    def updateProduction(self):
        if self.networks[ObjectCategory.ENERGY] is not None:
            self.networks[ObjectCategory.ENERGY].instantStock += self.cur_capacity

    def updateStock(self):
        if self.networks[ObjectCategory.ENERGY] is not None:
            max_capacity = self.buildingData['capacity'][ObjectCategory.ENERGY]
            network = self.networks[ObjectCategory.ENERGY]
            if network.instantProduction > 0 and not self.is_full():
                if self.cur_capacity + network.instantProduction > max_capacity:
                    toFill = max_capacity - self.cur_capacity
                    self.cur_capacity += toFill
                    network.instantProduction -= toFill
                    print("Recharge batterie", toFill)
                else:
                    self.cur_capacity += network.instantProduction
                    print("Recharge batterie", network.instantProduction)
                    network.instantProduction = 0
            elif not self.is_empty():
                if self.cur_capacity - network.consumedStock > 0:
                    self.cur_capacity -= network.consumedStock
                    print("Decharge batterie 1", network.consumedStock)
                else:
                    network.consumedStock -= self.cur_capacity
                    print("Decharge batterie 2", self.cur_capacity)
                    self.cur_capacity = 0
