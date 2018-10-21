
"""
Title: ressource File
Desc: Ressource class
Creation Date:  21/10/18
LastMod Date: 21/10/18
TODO:
"""

# May change inheritance


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

    def __str__(self):
        return "{} - {} -> {} ({})".format(self._position, self._size, self._category, self._amount)

