from objects.building import Building
from settings.enums import BuildingsName
from objects.consumingBuilding import ConsumingBuilding
from objects.producingBuilding import ProducingBuilding
from objects.miningBuilding import MiningBuilding
import modules.gameManager
from settings.buildingsSettings import ALL_BUILDINGS_SETTINGS


class DrillDiHydrogen(Building, ConsumingBuilding, ProducingBuilding, MiningBuilding):

    def __init__(self, position):
        Building.__init__(self, position, ALL_BUILDINGS_SETTINGS[BuildingsName.DRILL_DIHYDROGEN])
        ConsumingBuilding.__init__(self, self.network, self.buildingData, self.state, self.level)
        ProducingBuilding.__init__(self, self.network, self.buildingData, self.state, self.level)
        MiningBuilding.__init__(self, modules.gameManager.gameManager.getResourceAt(self.position))
