
"""
Title: ressource File
Desc: Ressource class
Creation Date:  21/10/18
LastMod Date: 24/10/18
TODO:
"""

# May change inheritance

from settings import settings


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
        self._amount = amount

        self.current_x = position[0] * settings.TILE_WIDTH
        self.current_y = position[1] * settings.TILE_HEIGHT

    def __str__(self):
        return "{} - {} -> {} ({})".format(self._position, self._size, self._category, self._amount)

    def getPos(self):
        return self._position