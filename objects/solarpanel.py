from objects.building import Building
from objects.producingBuilding import ProducingBuilding
from settings.enums import BuildingStates, BuildingsName
from settings.buildingsSettings import ALL_BUILDINGS_SETTINGS


class SolarPanel(Building, ProducingBuilding):

    def __init__(self, position):
        Building.__init__(self, position, ALL_BUILDINGS_SETTINGS[BuildingsName.SOLARPANEL])
        ProducingBuilding.__init__(self, self.network, self.buildingData, BuildingStates.ON, self.level)
