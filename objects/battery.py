from objects.building import Building
from objects.producingBuilding import ProducingBuilding
from objects.stockingBuilding import StockingBuilding
from settings.enums import BuildingsName, BuildingStates, ObjectCategory
from settings.buildingsSettings import ALL_BUILDINGS_SETTINGS


class Battery(Building, ProducingBuilding, StockingBuilding):

    def __init__(self, position):

        self.position = position
        self.network = None

        Building.__init__(self, self.position, ALL_BUILDINGS_SETTINGS[BuildingsName.BATTERY])

        self.state = BuildingStates.ON
        ProducingBuilding.__init__(self, self.network, ALL_BUILDINGS_SETTINGS[BuildingsName.BATTERY], self.state)
        StockingBuilding.__init__(self, self.network, ALL_BUILDINGS_SETTINGS[BuildingsName.BATTERY], ObjectCategory.ENERGY)
