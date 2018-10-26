from objects.building import Building
from settings.enums import BuildingsName
from objects.consumingBuilding import ConsumingBuilding
from objects.miningBuilding import MiningBuilding
import modules.gameManager
from settings.buildingsSettings import ALL_BUILDINGS_SETTINGS


class Crusher(Building, ConsumingBuilding, MiningBuilding):

    def __init__(self, position):
        Building.__init__(self, position, ALL_BUILDINGS_SETTINGS[BuildingsName.CRUSHER])
        ConsumingBuilding.__init__(self, self.network, self.buildingData, self.state, self.level)
        MiningBuilding.__init__(self, modules.gameManager.gameManager.getResourceAt(self.position))
