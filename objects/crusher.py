from objects.building import Building
from settings.enums import ObjectCategory, BuildingsName
from objects.electricBuilding import ElectricBuilding
import modules.gameManager
from settings.buildingsSettings import ALL_BUILDINGS_SETTINGS


class Crusher(Building, ElectricBuilding):

    def __init__(self, position):

        self.position = position
        self.size = [1, 1]
        self.connections = {'inputs': {'helium_rock': False, 'Electricity': False},
                            'outputs': {'helium_gaz': False}}
        self.ratio = 1

        self.networks = {
            ObjectCategory.ENERGY: None
        }

        self.linkedRes = modules.gameManager.gameManager.getResourceAt(self.position)

        Building.__init__(self, self.position, self.connections, ALL_BUILDINGS_SETTINGS[BuildingsName.CRUSHER])
        ElectricBuilding.__init__(self, self.networks, ALL_BUILDINGS_SETTINGS[BuildingsName.CRUSHER])
    def updateProduction(self):
        pass

    def update(self):
        pass
