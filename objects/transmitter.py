from settings.enums import BuildingsName
from settings.buildingsSettings import ALL_BUILDINGS_SETTINGS

from objects.consumingBuilding import ConsumingBuilding
from objects.building import Building


class Transmitter(Building, ConsumingBuilding):

    def __init__(self, position):
        Building.__init__(self, position, ALL_BUILDINGS_SETTINGS[BuildingsName.TRANSMITTER])
        ConsumingBuilding.__init__(self, self.network, self.buildingData, self.state, self.level)
