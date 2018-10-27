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
            ObjectCategory.ENERGY: 5,
            ObjectCategory.HYDROGEN: 0,
            ObjectCategory.DIHYDROGEN: 0,
            ObjectCategory.TRIHYDROGEN: 0,
            ObjectCategory.TRIHELIUM: 0,
            ObjectCategory.CREDITS: 1000
        }
        self._resourcesCap = {
            ObjectCategory.ENERGY: 0,
            ObjectCategory.HYDROGEN: 0,
            ObjectCategory.DIHYDROGEN: 0,
            ObjectCategory.TRIHYDROGEN: 0,
            ObjectCategory.TRIHELIUM: 0,
            ObjectCategory.CREDITS: None
        }
        self._resourcesVisible = {
            ObjectCategory.ENERGY: False,
            ObjectCategory.HYDROGEN: False,
            ObjectCategory.DIHYDROGEN: False,
            ObjectCategory.TRIHYDROGEN: False,
            ObjectCategory.TRIHELIUM: False,
            ObjectCategory.CREDITS: True
        }

    def getResources(self):
        return self._resources

    def getResourcesCap(self):
        return self._resourcesCap

    def getResourcesVisible(self):
        return self._resourcesVisible

    def upgradeResourceCapTo(self, resType, value):
        self._resourcesCap[resType] = value

    def unlockRes(self, res):
        self._resourcesVisible[res] = True

    def tryPay(self, resList):
        # check first
        for r, value in resList.items():
            if self._resources[r] < value:
                return False

        # then pay
        for r, value in resList.items():
            self._resources[r] -= value

        return True
