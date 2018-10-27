from objects.building import Building
from settings.enums import BuildingsName
from objects.consumingBuilding import ConsumingBuilding
from objects.producingBuilding import ProducingBuilding
from settings.buildingsSettings import ALL_BUILDINGS_SETTINGS


class TriHydrogenPlant(Building, ConsumingBuilding, ProducingBuilding):

    def __init__(self, position):
        Building.__init__(self, position, ALL_BUILDINGS_SETTINGS[BuildingsName.TRIHYDROGEN_PLANT])
        ConsumingBuilding.__init__(self, self.network, self.buildingData, self.state, self.level)
        ProducingBuilding.__init__(self, self.network, self.buildingData, self.state, self.level)
