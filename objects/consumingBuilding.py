import pygame
import uuid

from settings.enums import ObjectCategory
from settings.enums import BuildingStates


class ElectricBuilding():

    def __init__(self, network, buildingData):
        self.network = network
        self.buildingData = buildingData

    def updateProduction(self):
        if self.networks[ObjectCategory.ENERGY] is not None:
            self.networks[ObjectCategory.ENERGY].instantConsumption += self.buildingData['consume'][ObjectCategory.ENERGY]

    def update(self):
        consumption = self.buildingData['consume'][ObjectCategory.ENERGY]
        network = self.networks[ObjectCategory.ENERGY]
        if network is not None:
            self.state = BuildingStates.ON
            if self.consumption <= network.instantProduction:
                network.instantProduction -= consumption
                print("Batiment ON")
            else:
                leftToConsume = consumption - network.instantProduction
                if network.consumedStock + leftToConsume <= network.instantStock:
                    network.consumedStock += leftToConsume
                    print("Batiment sur batterie")
                else:
                    print("Batiment OFF")
                    self.state = BuildingStates.OFF
