
"""
Title: ressource File
Desc: Ressource class
Creation Date:  21/10/18
LastMod Date: 24/10/18
TODO:
"""

# May change inheritance

from settings import settings
from settings.enums import TooltipType


class Resource(object):
    def __init__(self, position, size, category, amount):
        """
        Init a resource
        :param position:
        :param size:
        :param category:
        :param amount:
        """
        self._position = position
        self._size = size
        self._category = category
        self._amount = int(amount)

        self.current_x = position[0] * settings.TILE_WIDTH
        self.current_y = position[1] * settings.TILE_HEIGHT

        self._tooltipType = TooltipType.TEXT_TIP

    def __str__(self):
        return "{} - {} -> {} ({})".format(self._position, self._size, self._category, self._amount)

    def getTooltipType(self):
        return self._tooltipType

    def getTooltipText(self):
        return "{} {}".format(self._amount, self._category.value)

    def getPos(self):
        return self._position

    def getCategory(self):
        return self._category

    def isEmpty(self):
        return self._amount <= 0

    def getAmount(self):
        return self._amount

    def setAmount(self, amount):
        self._amount = amount
