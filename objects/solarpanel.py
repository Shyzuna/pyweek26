from objects.building import Building
from objects.producingBuilding import ProducingBuilding
from settings.enums import BuildingStates, BuildingsName
from settings.buildingsSettings import ALL_BUILDINGS_SETTINGS


class SolarPanel(Building, ProducingBuilding):

    def __init__(self, position):

        self.position = position
        self.network = None

        Building.__init__(self, self.position, ALL_BUILDINGS_SETTINGS[BuildingsName.SOLARPANEL])

        self.state = BuildingStates.ON
        ProducingBuilding.__init__(self, self.network, ALL_BUILDINGS_SETTINGS[BuildingsName.SOLARPANEL], self.state)
