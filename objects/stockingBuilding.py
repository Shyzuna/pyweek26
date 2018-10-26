from settings.enums import ObjectCategory


class StockingBuilding():

    def __init__(self, network, buildingData, type):
        self.network = network
        self.buildingData = buildingData
        self.cur_capacity = {type: 0}
        self.type = type

    def is_full(self):
        max_capacity = self.buildingData['stock'][self.type]
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
        max_capacity = self.buildingData['stock'][self.type]
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