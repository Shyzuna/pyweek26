from objects.building import Building
from settings.enums import BuildingsName
from objects.consumingBuilding import ConsumingBuilding
from objects.producingBuilding import ProducingBuilding
import modules.gameManager
from settings.buildingsSettings import ALL_BUILDINGS_SETTINGS


class TriHeliumPlant(Building, ConsumingBuilding, ProducingBuilding):

    def __init__(self, position):
        Building.__init__(self, position, ALL_BUILDINGS_SETTINGS[BuildingsName.TRIHELIUM_PLANT])
        ConsumingBuilding.__init__(self, self.network, self.buildingData, self.state, self.level)
        ProducingBuilding.__init__(self, self.network, self.buildingData, self.state, self.level)