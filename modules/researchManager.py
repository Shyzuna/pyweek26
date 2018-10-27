"""
Title: researchManger File
Desc: ResearchManager class
Creation Date:  26/10/18
LastMod Date: 26/10/18
TODO:
"""

from settings.researchSettings import ALL_RESEARCH
import modules.guiManager
import modules.gameManager
from settings.enums import ResearchType


class ResearchManager(object):
    def __init__(self):
        self._currentLevel = 0
        self._currentResearch = None
        self._currentTimer = 0
        self._maxTimer = 0
        self._hq = None

    def init(self, hq):
        self._hq = hq

    def unlockNewLevel(self, level):
        modules.guiManager.guiManager.getFrameMenu('Research').unlockLevel(level)

    def completeResearch(self):
        ALL_RESEARCH[self._currentLevel][self._currentResearch]['done'] = True
        modules.guiManager.guiManager.getFrameMenu('Research').setResearchCompleted(self._currentLevel, self._currentResearch)
        research = ALL_RESEARCH[self._currentLevel][self._currentResearch]
        if research['type'] == ResearchType.UPGRADE:
            modules.gameManager.gameManager.upgradeBuildings(research['element'], research['param'], research['value'])
        elif research['type'] == ResearchType.UNLOCK:
            modules.gameManager.gameManager.unlockBuildings(research['unlocked'])
            modules.gameManager.gameManager.unlockRes(research['resUnlocked'])
        self._currentResearch = None

    def startResearch(self, lvl, number):
        if self._currentResearch is None and 'done' not in ALL_RESEARCH[lvl][number]:
            if modules.gameManager.gameManager.getPlayer().tryPay(ALL_RESEARCH[lvl][number]['cost']):
                modules.guiManager.guiManager.getFrameMenu('Research').startResearch(lvl, number)
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

    def getHqLevel(self):
        return self._hq.level + 1

researchManager = ResearchManager()