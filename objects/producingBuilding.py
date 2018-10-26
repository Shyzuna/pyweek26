from settings.enums import BuildingStates


class ProducingBuilding():

    def __init__(self, network, buildingData, state):
        self.network = network
        self.buildingData = buildingData
        self.state = state

    def produce(self):
        if self.network is not None:
            for producingType, producingValue in self.buildingData['produce'].items():
                if self.state == BuildingStates.OFF:
                    break
                self.network.produceResources(producingValue, producingType)
                print("Production de ", producingValue, producingType)
