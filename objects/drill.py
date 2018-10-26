from objects.building import Building
from settings.enums import BuildingsName
from objects.electricBuilding import ElectricBuilding
from settings.enums import ObjectCategory
import modules.gameManager
from settings.buildingsSettings import ALL_BUILDINGS_SETTINGS


class Drill(Building, ElectricBuilding):

    def __init__(self, position):

        self.position = position
        self.size = [1, 1]
        self.connections = {'inputs': {'hydrogen_rock': False, 'Electricity': False},
                            'outputs': {'hydrogen_gaz': False}}

        self.networks = {
            ObjectCategory.ENERGY: None,
            ObjectCategory.HYDROGEN: None
        }

        self.linkedRes = modules.gameManager.gameManager.getResourceAt(self.position)

        Building.__init__(self, self.position, self.connections, ALL_BUILDINGS_SETTINGS[BuildingsName.DRILL])
        ElectricBuilding.__init__(self, self.networks, ALL_BUILDINGS_SETTINGS[BuildingsName.DRILL])

    def updateProduction(self):
        ElectricBuilding.updateProduction(self)

