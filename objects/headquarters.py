
from settings.enums import BuildingsName
from settings.buildingsSettings import ALL_BUILDINGS_SETTINGS
from settings.enums import ObjectCategory

from objects.building import Building


class HeadQuarters(Building):

    def __init__(self, position):

        self.position = position
        self.size = [1, 1]
        self.connections = {'inputs': {'Electricity': False},
                            'outputs': None}

        self.networks = {
            ObjectCategory.ENERGY: None
        }

        Building.__init__(self, self.position, self.connections, ALL_BUILDINGS_SETTINGS[BuildingsName.HEADQUARTERS])

    def updateProduction(self):
        pass

    def update(self):
        pass