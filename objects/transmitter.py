from settings.enums import BuildingsName, BuildingStates
from settings.buildingsSettings import ALL_BUILDINGS_SETTINGS

from objects.consumingBuilding import ConsumingBuilding
from objects.building import Building


class Transmitter(Building, ConsumingBuilding):

    def __init__(self, position, earth):
        Building.__init__(self, position, ALL_BUILDINGS_SETTINGS[BuildingsName.TRANSMITTER])
        ConsumingBuilding.__init__(self, self.network, self.buildingData, self.state, self.level)
        self._earth = earth

    def consume(self):
        self.state = BuildingStates.ON if self.network is not None else BuildingStates.OFF
        print(self.state)
        if self._earth.isSending() and self.state == BuildingStates.ON:
            ConsumingBuilding.consume(self)
