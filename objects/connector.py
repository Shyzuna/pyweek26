from objects.building import Building
from settings.enums import BuildingsName
import modules.gameManager
from settings.buildingsSettings import ALL_BUILDINGS_SETTINGS


class Connector(Building):

    def __init__(self, position):

        self.position = position
        self.network = None
        self.linkedRes = modules.gameManager.gameManager.getResourceAt(self.position)

        Building.__init__(self, self.position, ALL_BUILDINGS_SETTINGS[BuildingsName.CONNECTOR])
