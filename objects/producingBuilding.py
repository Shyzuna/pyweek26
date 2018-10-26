from settings.enums import BuildingStates


class ProducingBuilding():

    def __init__(self, network, buildingData, state, level):
        self.network = network
        self.buildingData = buildingData
        self.state = state
        self.level = level

    def produce(self):
        if self.network is not None:
            for producingType, producingValue in self.buildingData['produce'].items():
                if self.state == BuildingStates.OFF:
                    break
                self.network.produceResources(producingValue[self.level], producingType)
                print("Production de ", producingValue[self.level], producingType)
