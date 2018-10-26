from settings.enums import BuildingsName
from settings.buildingsSettings import ALL_BUILDINGS_SETTINGS

from objects.building import Building


class HeadQuarters(Building):

    def __init__(self, position):

        self.position = position
        self.network = None

        Building.__init__(self, self.position, ALL_BUILDINGS_SETTINGS[BuildingsName.HEADQUARTERS])
