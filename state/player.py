"""
Title: player File
Desc: Player class
Creation Date:  22/10/18
LastMod Date: 22/10/18
TODO:
"""

from settings.enums import ObjectCategory


class Player(object):
    def __init__(self):
        self._resources = {
            ObjectCategory.ENERGY: 0,
            ObjectCategory.HYDROGEN: 0,
            ObjectCategory.DIHYGROGEN: 0,
            ObjectCategory.TRIHYGROGEN: 0,
            ObjectCategory.TRIHELIUM: 0
        }
        self._resourcesCap = {
            ObjectCategory.ENERGY: 10,
            ObjectCategory.HYDROGEN: 10,
            ObjectCategory.DIHYGROGEN: 10,
            ObjectCategory.TRIHYGROGEN: 10,
            ObjectCategory.TRIHELIUM: 10
        }
        self._resourcesVisible = {
            ObjectCategory.ENERGY: True,
            ObjectCategory.HYDROGEN: True,
            ObjectCategory.DIHYGROGEN: True,
            ObjectCategory.TRIHYGROGEN: True,
            ObjectCategory.TRIHELIUM: True
        }

    def getResources(self):
        return self._resources

    def getResourcesCap(self):
        return self._resourcesCap

    def getResourcesVisible(self):
        return self._resourcesVisible

