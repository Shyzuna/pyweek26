"""
Title: guiManager File
Desc: GuiManager class
Creation Date:  22/10/18
LastMod Date: 22/10/18
TODO:
"""

from settings import settings
from settings.enums import Colors
from objects.UI.button import UIButton
import pygame
import os

class GuiManager(object):
    def __init__(self):
        self._buildingsList = []
        self._fonts = []
        self._currentFont = 0
        self._topBar = None
        self._sideButtons = {}
        self._currentSideMenu = 'base'

    def init(self, buildList):
        pygame.font.init()
        self._fonts.append(pygame.font.Font(os.path.join(settings.FONT_PATH, 'VCR_OSD.ttf'), 15))
        self._topBar = pygame.Surface((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT * settings.UI_TOP_BAR))
        self._buildingsList = buildList
        self.createSideButton()

    def updateTopBar(self, player):
        self._topBar.fill(Colors.WHITE.value)
        allTexts = []  # May generate text only when change
        totalSize = 0
        textH = 0
        for res, amount in player.getResources().items():
            if player.getResourcesVisible()[res]:
                text = self._fonts[self._currentFont].render('{} : {}/{}'.format(
                    res.value,
                    str(amount),
                    str(player.getResourcesCap()[res])
                ), 1, Colors.BLACK.value)
                allTexts.append(text)
                totalSize += text.get_width()
                textH = text.get_height()

        widthSpaceByElem = (settings.SCREEN_WIDTH - totalSize) / (len(allTexts) + 1)
        topSpace = (settings.SCREEN_HEIGHT * settings.UI_TOP_BAR - textH) / 2

        lastLeft = widthSpaceByElem
        for idx, t in enumerate(allTexts):
            self._topBar.blit(t, (lastLeft, topSpace))
            lastLeft += (t.get_width() + widthSpaceByElem)

    def createSideButton(self):
        buttonList = []
        buttonSize = (settings.SCREEN_WIDTH * settings.UI_SIDE_BAR,
                      (settings.SCREEN_HEIGHT - self._topBar.get_height()) / len(self._buildingsList))
        buttonH = self._topBar.get_height()
        for cat, l in self._buildingsList.items():
            buttonList.append(UIButton(cat.value, buttonSize, (0, buttonH),
                                              self._fonts[self._currentFont], self.changeMenu))
            buttonH += buttonSize[1]

            localButtonH = self._topBar.get_height()
            localButtonList = []
            localButtonSize = (settings.SCREEN_WIDTH * settings.UI_SIDE_BAR,
                      (settings.SCREEN_HEIGHT - self._topBar.get_height()) / (len(l) + 1))
            for e in l:
                name,obj = e
                localButtonList.append(UIButton(name.value, localButtonSize, (0, localButtonH),
                                              self._fonts[self._currentFont], self.selectBuilding))
                localButtonH += localButtonSize[1]
            localButtonList.append(UIButton('back', localButtonSize, (0, localButtonH),
                                            self._fonts[self._currentFont], self.resetMenu))
            self._sideButtons[cat.value] = localButtonList
        self._sideButtons['base'] = buttonList


    def displayGui(self, screen, player):
        self.updateTopBar(player)
        screen.blit(self._topBar, (0, 0))
        for b in self._sideButtons[self._currentSideMenu]:
            b.draw(screen)

    def checkMousePosition(self, mPos):
        for b in self._sideButtons[self._currentSideMenu]:
            b.checkHover(mPos)

    def handleMouseButton(self, pressed, mPos):
        for b in self._sideButtons[self._currentSideMenu]:
            b.checkMousePressed(pressed, mPos)

    def resetMenu(self, *arg):
        self._currentSideMenu = 'base'

    def changeMenu(self, *arg):
        self._currentSideMenu = arg[0]

    def selectBuilding(self, *arg):
        print("Building {} selected".format(arg[0]))

guiManager = GuiManager()