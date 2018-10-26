from settings.enums import ObjectCategory
from settings.enums import BuildingStates


class ConsumingBuilding():

    def __init__(self, network, buildingData, state):
        self.network = network
        self.buildingData = buildingData
        self.state = state

    def consume(self):
        if self.network is not None:
            tempState = BuildingStates.ON
            for consumingType, consumeValue in self.buildingData['consume'].items():
                if tempState == BuildingStates.OFF:
                    break
                tempState = self.network.consumeResources(consumeValue, consumingType)
                print("Consommation de ", consumeValue, consumingType, tempState)
            self.state = tempState
