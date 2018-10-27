from settings.enums import ObjectCategory
import modules.gameManager


class StockingBuilding():

    def __init__(self, network, buildingData, type, level):
        self.network = network
        self.buildingData = buildingData
        self.cur_capacity = {type: 0}
        self.type = type
        self.level = level

    def is_full(self):
        max_capacity = self.buildingData['stock'][self.type][self.level]
        if self.cur_capacity[self.type] == max_capacity:
            return True
        else:
            return False

    def is_empty(self):
        if self.cur_capacity[self.type] == 0:
            return True
        else:
            return False

    def fill(self):
        max_capacity = self.buildingData['stock'][self.type][self.level]
        self.cur_capacity[self.type] = max_capacity

    def empty(self):
        self.cur_capacity[self.type] = 0

    def produceStock(self):
        if self.network is not None:
            for stockingType in self.buildingData['stock'].keys():
                self.network.produceStock(self.cur_capacity[self.type], stockingType)

    def stock(self):
        if self.network is not None:
            for stockingType in self.buildingData['stock'].keys():
                self.network.fillStock(self, stockingType)

    def geCurrentMaxStock(self):
        return self.buildingData['stock'][self.type][self.level]

    def updateTotalResCap(self):
        prevCap = self.buildingData['stock'][self.type][self.level - 1]
        delta = self.buildingData['stock'][self.type][self.level] - prevCap
        modules.gameManager.gameManager.getPlayer().upgradeResourceCapWith(self.type, delta)
