import pygame
import os

from settings import settings
from objects.building import Building


class Battery(Building):

    def __init__(self, position):

        self.position = position
        self.size = [1, 1]
        self.connections = {'inputs': {'Electricity': False},
                            'outputs': {'Electricity': False}}

        self.max_capacity = 50
        self.cur_capacity = 0

        self.networks = {
            'electric': None
        }

        self.img = pygame.image.load(os.path.join(settings.BUILDINGS_PATH, "BATTERY.png"))
        self.img = pygame.transform.scale(self.img, (settings.TILE_WIDTH*self.size[0],
                                                     settings.TILE_HEIGHT*self.size[1]))

        Building.__init__(self, self.position, self.size, self.connections, self.img)

    def update_capacity(self, value):
        overflow = 0

        if self.max_capacity >= self.cur_capacity + value:
            overflow = self.cur_capacity - self.max_capacity + value
            self.cur_capacity += value

        return overflow

    def is_full(self):
        if self.cur_capacity == self.max_capacity:
            return True
        else:
            return False

    def is_empty(self):
        if self.cur_capacity == 0:
            return True
        else:
            return False

    def fill(self):
        self.cur_capacity = self.max_capacity

    def empty(self):
        self.cur_capacity = 0

    def updateProduction(self):
        if self.networks['electric'] is not None:
            self.networks['electric'].instantStock += self.cur_capacity

    def updateStock(self):
        if self.networks['electric'] is not None:
            network = self.networks['electric']
            if network.instantProduction > 0 and not self.is_full():
                if self.cur_capacity + network.instantProduction > self.max_capacity:
                    toFill = self.max_capacity - self.cur_capacity
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
