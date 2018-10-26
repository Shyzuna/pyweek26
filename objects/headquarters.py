from settings.enums import BuildingsName
from settings.buildingsSettings import ALL_BUILDINGS_SETTINGS

from objects.building import Building


class HeadQuarters(Building):

    def __init__(self, position):
        Building.__init__(self, position, ALL_BUILDINGS_SETTINGS[BuildingsName.HEADQUARTERS])
