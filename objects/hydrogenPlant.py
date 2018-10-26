from objects.building import Building
from settings.enums import BuildingsName
from objects.consumingBuilding import ConsumingBuilding
from objects.producingBuilding import ProducingBuilding
import modules.gameManager
from settings.buildingsSettings import ALL_BUILDINGS_SETTINGS


class HydrogenPlant(Building, ConsumingBuilding, ProducingBuilding):

    def __init__(self, position):

        self.position = position
        self.network = None
        self.linkedRes = modules.gameManager.gameManager.getResourceAt(self.position)

        Building.__init__(self, self.position, ALL_BUILDINGS_SETTINGS[BuildingsName.HYDROGEN_PLANT])
        ConsumingBuilding.__init__(self, self.network, self.buildingData, self.state, self.level)
        ProducingBuilding.__init__(self, self.network, self.buildingData, self.state, self.level)
