"""
Title: researchManger File
Desc: ResearchManager class
Creation Date:  26/10/18
LastMod Date: 26/10/18
TODO:
"""

from settings.researchSettings import ALL_RESEARCH


class ResearchManager(object):
    def __init__(self):
        self._currentLevel = 0
        self._currentResearch = None
        self._currentTimer = 0
        self._maxTimer = 0

    def init(self):
        self.startResearch('1', 0)

    def completeResearch(self):
        ALL_RESEARCH[self._currentLevel][self._currentResearch]['done'] = True
        self._currentResearch = None

    def startResearch(self, lvl, number):
        if self._currentResearch is None and 'done' not in ALL_RESEARCH[lvl][number]:
            self._currentLevel = lvl
            self._currentResearch = number
            self._maxTimer = ALL_RESEARCH[lvl][number]['time'] * 1000
            self._currentTimer = self._maxTimer

    def update(self, dTime):
        if self._currentResearch is not None:
            self._currentTimer -= dTime
            if self._currentTimer <= 0:
                self.completeResearch()

    def getTimers(self):
        return self._maxTimer, self._currentTimer

    def isSearching(self):
        return self._currentResearch is not None

researchManager = ResearchManager()