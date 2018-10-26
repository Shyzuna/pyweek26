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
        self._timer = 0

    def init(self):
        pass

    def completeResearch(self):
        ALL_RESEARCH[self._currentLevel][self._currentResearch]['done'] = True
        self._currentResearch = False

    def startResearch(self, lvl, number):
        if self._currentResearch is not None and 'done' not in ALL_RESEARCH[lvl][number]:
            self._currentLevel = lvl
            self._currentResearch = number
            self._timer = ALL_RESEARCH[lvl][number]['time']

    def update(self, dTime):
        if self._currentResearch is not None:
            self._timer -= dTime
            if self._timer <= 0:
                self.completeResearch()

researchManager = ResearchManager()