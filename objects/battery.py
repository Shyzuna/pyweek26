from objects.building import Building
from objects.producingBuilding import ProducingBuilding
from objects.stockingBuilding import StockingBuilding
from settings.enums import BuildingsName, BuildingStates, ObjectCategory
from settings.buildingsSettings import ALL_BUILDINGS_SETTINGS


class Battery(Building, ProducingBuilding, StockingBuilding):

    def __init__(self, position):
        Building.__init__(self, position, ALL_BUILDINGS_SETTINGS[BuildingsName.BATTERY])
        ProducingBuilding.__init__(self, self.network, self.buildingData, BuildingStates.ON, self.level)
        StockingBuilding.__init__(self, self.network, self.buildingData, ObjectCategory.ENERGY, self.level)

    def sendEnergy(self, amount):
        if not self.is_empty():
            if amount <= self.cur_capacity[ObjectCategory.ENERGY]:
                self.cur_capacity[ObjectCategory.ENERGY] -= amount
                return 0
            else:
                leftToSend = self.cur_capacity[ObjectCategory.ENERGY] - amount
                self.cur_capacity[ObjectCategory.ENERGY] = 0
                return leftToSend
        return 0
