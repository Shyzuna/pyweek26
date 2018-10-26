from settings.enums import ObjectCategory
from settings.enums import BuildingStates


class ConsumingBuilding():

    def __init__(self, network, buildingData, state, level):
        self.network = network
        self.buildingData = buildingData
        self.state = state
        self.level = level

    def consume(self):
        if self.network is not None:
            tempState = BuildingStates.ON
            for consumingType, consumeValue in self.buildingData['consume'].items():
                if tempState == BuildingStates.OFF:
                    break
                tempState = self.network.consumeResources(consumeValue[self.level], consumingType)
                print("Consommation de ", consumeValue[self.level], consumingType, tempState)
            self.state = tempState
