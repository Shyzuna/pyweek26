"""
Title: guiManager File
Desc: GuiManager class
Creation Date:  22/10/18
LastMod Date: 24/10/18
TODO:
"""

from settings import settings
from settings.enums import Colors, ObjectCategory
from objects.UI.button import UIButton
from objects.UI.buildingMouseSnap import UIBuildingMouseSnap
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
        self._battery = None
        self._batteryLevel = None  #44x28
        self._internBatteryPos = (10, 24)
        self._buildingSelected = None
        self._onGui = False

    def init(self, buildList):
        pygame.font.init()
        self._fonts.append(pygame.font.Font(os.path.join(settings.FONT_PATH, 'VCR_OSD.ttf'), 15))
        self._topBar = pygame.Surface((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT * settings.UI_TOP_BAR))

        factor = 2.5
        tmpImg = pygame.image.load(os.path.join(settings.GUI_PATH, 'GUIBattery.png'))
        self._battery = pygame.transform.scale(tmpImg, (int(tmpImg.get_width() * factor),
                                                        int(tmpImg.get_height() * factor)))
        self._batteryLevel = pygame.Surface((int(44 * factor), int(28 * factor)))
        self._internBatteryPos = (int(self._internBatteryPos[0] * factor), int(self._internBatteryPos[1] * factor))
        self._buildingsList = buildList
        self.createSideButton()

    def updateBatteryLevel(self, player):
        self._batteryLevel.fill(Colors.WHITE.value)
        batterySize = self._batteryLevel.get_size()
        energy = player.getResources()[ObjectCategory.ENERGY]
        maxEnergy = player.getResourcesCap()[ObjectCategory.ENERGY]
        ratioEnergy = player.getResources()[ObjectCategory.ENERGY] / player.getResourcesCap()[ObjectCategory.ENERGY]
        rect = pygame.Rect(0, int(batterySize[1] * ratioEnergy), batterySize[0], int(batterySize[1] * ratioEnergy))
        pygame.draw.rect(self._batteryLevel, Colors.LIGHT_CYAN.value, rect)
        text = self._fonts[self._currentFont].render('{}/{}'.format(
            str(energy),
            str(maxEnergy)), 1, Colors.BLACK.value)
        self._batteryLevel.blit(text, ((batterySize[0] - text.get_width()) / 2,
                                       (batterySize[1] - text.get_height()) / 2))
    def updateGui(self, player, mPos):
        self.updateTopBar(player)
        self.updateBatteryLevel(player)
        if self._buildingSelected is not None:
            self._buildingSelected.updatePosition(mPos)

    def updateTopBar(self,  player):
        self._topBar.fill(Colors.WHITE.value)
        allTexts = []  # May generate text only when change
        totalSize = 0
        textH = 0
        for res, amount in player.getResources().items():
            if player.getResourcesVisible()[res]:
                if player.getResourcesCap()[res] is not None:
                    strContent = '{} : {}/{}'.format(res.value, str(amount), str(player.getResourcesCap()[res]))
                else:
                    strContent = '{} : {}'.format(res.value, str(amount))
                text = self._fonts[self._currentFont].render(strContent, 1, Colors.BLACK.value)
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
                name, obj = e
                localButtonList.append(UIButton(name.value, localButtonSize, (0, localButtonH),
                                                self._fonts[self._currentFont], self.selectBuilding, building=obj))
                localButtonH += localButtonSize[1]
            localButtonList.append(UIButton('back', localButtonSize, (0, localButtonH),
                                            self._fonts[self._currentFont], self.resetMenu))
            self._sideButtons[cat.value] = localButtonList
        self._sideButtons['base'] = buttonList

    def displayGui(self, screen):
        screen.blit(self._topBar, (0, 0))
        for b in self._sideButtons[self._currentSideMenu]:
            b.draw(screen)

        batterySize = self._battery.get_size()
        screen.blit(self._batteryLevel, (settings.SCREEN_WIDTH - batterySize[0] - 10 + self._internBatteryPos[0],
                                         settings.SCREEN_HEIGHT - batterySize[1] - 10 + self._internBatteryPos[1]))
        screen.blit(self._battery, (settings.SCREEN_WIDTH - batterySize[0] - 10,
                                    settings.SCREEN_HEIGHT - batterySize[1] - 10))

        if self._buildingSelected is not None:
            self._buildingSelected.display(screen)

    def isOnGui(self):
        return self._onGui

    def checkMousePosition(self, mPos):
        onGui = False
        # Check battery
        batterySize = self._battery.get_size()
        rect = pygame.Rect(settings.SCREEN_WIDTH - batterySize[0] - 10,
                           settings.SCREEN_HEIGHT - batterySize[1] - 10, batterySize[0], batterySize[1])
        onGui = onGui or rect.collidepoint(mPos[0], mPos[1])
        # Check TopBar
        rect = pygame.Rect(0, 0, self._topBar.get_width(), self._topBar.get_height())
        onGui = onGui or rect.collidepoint(mPos[0], mPos[1])
        # Check button
        for b in self._sideButtons[self._currentSideMenu]:
            onGui = onGui or b.checkHover(mPos)
        self._onGui = onGui

    def handleMouseButton(self, pressed, mPos, button):
        if button == 1:
            if self._onGui:
                for b in self._sideButtons[self._currentSideMenu]:
                    b.checkMousePressed(pressed, mPos)
            elif not pressed and self._buildingSelected is not None:
                self._buildingSelected.tryBuild()

        elif button == 3:
            self._buildingSelected = None

    def resetMenu(self, *arg):
        self._currentSideMenu = 'base'

    def changeMenu(self, *arg):
        self._currentSideMenu = arg[0]

    def selectBuilding(self, *arg):
        print("Building {} selected".format(arg[0]))
        if arg[1] is not None:
            self._buildingSelected = UIBuildingMouseSnap(arg[1]((-1, -1)), self)


guiManager = GuiManager()