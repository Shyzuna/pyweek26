"""
Title: guiManager File
Desc: GuiManager class
Creation Date:  22/10/18
LastMod Date: 25/10/18
TODO:
"""

from settings import settings
from settings.enums import Colors, ObjectCategory, TooltipType, BuildingsName, BuildingStates, ResearchType
from settings.buildingsSettings import ALL_BUILDINGS_SETTINGS
from objects.UI.button import UIButton
from objects.UI.buildingMouseSnap import UIBuildingMouseSnap
from objects.UI.buildingDestroySnap import UIBuildingDestroySnap
from objects.miningBuilding import MiningBuilding
from objects.UI.buildingUpgradeSnap import UIBuildingUpgradeSnap
from modules.contractManager import contractManager
from objects.UI.earthFrame import UIEarthFrame
from objects.UI.researchFrame import UIResearchFrame
import modules.gameManager
import pygame
import os
from objects.connector import Connector

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
        self._buildingDestroy = None
        self._buildingUpgrade = None
        self._onGui = False
        self._tooltipSurf = None
        self._tooltipPos = None
        self._menuList = {
            'Build': self.changeMenu,
            'Research': self.changeCentralFrame,
            'Contract': self.changeCentralFrame,
            'Earth': self.changeCentralFrame
        }
        self._centralFrame = None
        self._frameList = {
            'Research': None,
            'Contract': contractManager,
            'Earth': None
        }
        self._guiImg = {}

    def init(self, buildList, earth):
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

        self._guiImg['destructor'] = pygame.image.load(os.path.join(settings.GUI_PATH, 'destroy.png'))
        self._guiImg['destructorMini'] = pygame.transform.scale(self._guiImg['destructor'],
                                                               (int(self._guiImg['destructor'].get_width() / 2),
                                                                int(self._guiImg['destructor'].get_height() / 2)))

        self.createSideButton()

        frameSize = (
            int((settings.SCREEN_WIDTH - (settings.SCREEN_WIDTH * settings.UI_SIDE_BAR)) * settings.UI_CENTRAL_FRAME[0]),
            int((settings.SCREEN_HEIGHT - self._topBar.get_height()) * settings.UI_CENTRAL_FRAME[1])
        )

        framePos = (
            int(((settings.SCREEN_WIDTH - (settings.SCREEN_WIDTH * settings.UI_SIDE_BAR)) - frameSize[0]) / 2)
            + (settings.SCREEN_WIDTH * settings.UI_SIDE_BAR),
            int((settings.SCREEN_HEIGHT - self._topBar.get_height() - frameSize[1]) / 2) + self._topBar.get_height()
        )

        contractManager.init(frameSize, framePos, guiManager)
        self._frameList['Research'] = UIResearchFrame(frameSize, framePos, self._fonts[self._currentFont], self)
        self._frameList['Earth'] = UIEarthFrame(frameSize, framePos, self._fonts[self._currentFont], self, earth)

    def updateBatteryLevel(self, player):
        self._batteryLevel.fill(Colors.WHITE.value)
        batterySize = self._batteryLevel.get_size()
        energy = player.getResources()[ObjectCategory.ENERGY]
        maxEnergy = player.getResourcesCap()[ObjectCategory.ENERGY]
        if player.getResourcesCap()[ObjectCategory.ENERGY] != 0:
            ratioEnergy = player.getResources()[ObjectCategory.ENERGY] / player.getResourcesCap()[ObjectCategory.ENERGY]
        else:
            ratioEnergy = 0

        if ratioEnergy > 0:
            rect = pygame.Rect(0, batterySize[1] - int(batterySize[1] * ratioEnergy),
                               batterySize[0], int(batterySize[1] * ratioEnergy))
            pygame.draw.rect(self._batteryLevel, Colors.LIGHT_CYAN.value, rect)

        text = self._fonts[self._currentFont].render('{}/{}'.format(
            str(int(energy)),
            str(int(maxEnergy))), 1, Colors.BLACK.value)
        self._batteryLevel.blit(text, ((batterySize[0] - text.get_width()) / 2,
                                       (batterySize[1] - text.get_height()) / 2))

    def createTooltipUIElem(self, hoveredElem):
        tooltipT = hoveredElem.getTooltipType()
        if tooltipT is not None:
            self._tooltipSurf = pygame.Surface((300, 150))
            self._tooltipSurf.fill(Colors.WHITE.value)
            pygame.draw.rect(self._tooltipSurf, Colors.BLACK.value, pygame.Rect(0, 0, 299, 149), 2)
            if tooltipT == TooltipType.GUI_BUILDING:
                index = 1
                building = hoveredElem.getBuildingData()
                text = self._fonts[self._currentFont].render(building['name'], 1, Colors.BLACK.value)
                self._tooltipSurf.blit(text, (5, 5))
                index += 1

                for costType, data  in building['cost'].items():
                    text = self._fonts[self._currentFont].render(
                        "Cost {} {}".format(data[0], costType.value), 1, Colors.BLACK.value)
                    self._tooltipSurf.blit(text, (5, 5 + text.get_height() * index))
                    index += 1

                for consumeType, data in building['consume'].items():
                    text = self._fonts[self._currentFont].render(
                        "Consume {} {}".format(data[0], consumeType.value), 1, Colors.BLACK.value)
                    self._tooltipSurf.blit(text, (5, 5 + text.get_height() * index))
                    index += 1

                for produceType, data in building['produce'].items():
                    text = self._fonts[self._currentFont].render(
                        "Produce {} {}".format(data[0], produceType.value), 1, Colors.BLACK.value)
                    self._tooltipSurf.blit(text, (5, 5 + text.get_height() * index))
            elif tooltipT == TooltipType.IG_BUILDING:
                index = 1
                building = hoveredElem
                text = self._fonts[self._currentFont].render(building.buildingData['name'], 1, Colors.BLACK.value)
                self._tooltipSurf.blit(text, (5, 5))
                index += 1
                text = self._fonts[self._currentFont].render(
                    "Level {}".format(hoveredElem.getLevel() + 1), 1, Colors.BLACK.value)
                self._tooltipSurf.blit(text, (5, 5 + text.get_height()))
                index += 1

                if building.getStatus() == BuildingStates.ON:
                    color = Colors.GREEN.value
                else:
                    color = Colors.RED.value

                text = self._fonts[self._currentFont].render(
                    "Status {}".format(building.getStatus().value), 1, color)
                self._tooltipSurf.blit(text, (5, 5 + text.get_height() * index))
                index += 1

                if building.getLevel() < settings.BUILDING_MAX_LEVEL - 1:
                    for costType, data in building.buildingData['cost'].items():
                        text = self._fonts[self._currentFont].render(
                            "Upgrade cost {} {}".format(data[building.getLevel() + 1], costType.value), 1, Colors.BLACK.value)
                        self._tooltipSurf.blit(text, (5, 5 + text.get_height() * index))
                        index += 1
                else:
                    text = self._fonts[self._currentFont].render(
                        "No uprade available", 1, Colors.BLACK.value)
                    self._tooltipSurf.blit(text, (5, 5 + text.get_height() * index))
                    index += 1

                for consumeType, data in building.buildingData['consume'].items():
                    text = self._fonts[self._currentFont].render(
                        "Consume {} {}".format(data[building.getLevel()], consumeType.value), 1, Colors.BLACK.value)
                    self._tooltipSurf.blit(text, (5, 5 + text.get_height() * index))
                    index += 1

                for produceType, data in building.buildingData['produce'].items():
                    text = self._fonts[self._currentFont].render(
                        "Produce {} {}".format(data[building.getLevel()], produceType.value), 1, Colors.BLACK.value)
                    self._tooltipSurf.blit(text, (5, 5 + text.get_height() * index))
                    index += 1

                for capacityType, data in building.buildingData['stock'].items():
                    text = self._fonts[self._currentFont].render(
                        "Stock {}/{} {}".format(building.getCurrentCapacity(capacityType), data[building.getLevel()], capacityType.value), 1, Colors.BLACK.value)
                    self._tooltipSurf.blit(text, (5, 5 + text.get_height() * index))
                    index += 1

                if isinstance(hoveredElem, MiningBuilding):
                    text = self._fonts[self._currentFont].render(hoveredElem.getLinkedRes().getTooltipText(), 1, Colors.BLACK.value)
                    self._tooltipSurf.blit(text, (5, 5 + text.get_height() * index))
            elif tooltipT == TooltipType.RESEARCH_TIP:
                index = 1
                research = hoveredElem.getResearchData()
                text = self._fonts[self._currentFont].render(research['name'], 1, Colors.BLACK.value)
                self._tooltipSurf.blit(text, (5, 5))
                index += 1

                for costType, data  in research['cost'].items():
                    text = self._fonts[self._currentFont].render(
                        "Cost {} {}".format(data, costType.value), 1, Colors.BLACK.value)
                    self._tooltipSurf.blit(text, (5, 5 + text.get_height() * index))
                    index += 1

                if research['type'] == ResearchType.UPGRADE:
                    text = self._fonts[self._currentFont].render(
                        "Element {}".format(research['element'].value), 1, Colors.BLACK.value)
                    self._tooltipSurf.blit(text, (5, 5 + text.get_height() * index))
                    index += 1

                    for produceType, data in ALL_BUILDINGS_SETTINGS[research['element']]['produce'].items():
                        text = self._fonts[self._currentFont].render(
                            "Improve prod{} by {}".format(produceType.value, research['value']), 1, Colors.BLACK.value)
                        self._tooltipSurf.blit(text, (5, 5 + text.get_height() * index))
                        index += 1

                    for stockType, data in ALL_BUILDINGS_SETTINGS[research['element']]['stock'].items():
                        text = self._fonts[self._currentFont].render(
                            "Improve max cap {} by {}".format(stockType.value, research['value']), 1, Colors.BLACK.value)
                        self._tooltipSurf.blit(text, (5, 5 + text.get_height() * index))
                        index += 1

                elif research['type'] == ResearchType.UNLOCK:
                    for unlock in research['unlocked']:
                        text = self._fonts[self._currentFont].render(
                            "Unlock {}".format(unlock.value), 1, Colors.BLACK.value)
                        self._tooltipSurf.blit(text, (5, 5 + text.get_height() * index))
                        index += 1
                    if research['resUnlocked'] is not None:
                        text = self._fonts[self._currentFont].render(
                            "Unlock {}".format(research['resUnlocked'].value), 1, Colors.BLACK.value)
                        self._tooltipSurf.blit(text, (5, 5 + text.get_height() * index))

            elif tooltipT == TooltipType.TEXT_TIP:
                text = self._fonts[self._currentFont].render(hoveredElem.getTooltipText(), 1, Colors.BLACK.value)
                self._tooltipSurf.blit(text, (5, 5))
        else:
            self._tooltipSurf = None

    def updateTooltipPos(self, mPos):
        offsetX = 0
        offsetY = 0
        size = self._tooltipSurf.get_size()
        # width
        if (mPos[0] + size[0]) > settings.SCREEN_WIDTH:  # Left
            offsetX = -size[0] - 10
        else:  # Right
            offsetX = 10
        # height
        if (mPos[1] + size[1]) > settings.SCREEN_HEIGHT:  # Above
            offsetY = -size[1] - 10
        else:  # Bellow
            offsetY = 10
        self._tooltipPos = (mPos[0] + offsetX, mPos[1] + offsetY)

    def updateGui(self, player, mPos):
        self.updateTopBar(player)
        self.updateBatteryLevel(player)
        if self._buildingSelected is not None:
            self._buildingSelected.updatePosition(mPos)
        if self._buildingDestroy is not None:
            self._buildingDestroy.updatePosition(mPos)
        if self._buildingUpgrade is not None:
            self._buildingUpgrade.updatePosition(mPos)
        if self._tooltipSurf is not None:
            self.updateTooltipPos(mPos)
        if self._centralFrame is not None:
            self._frameList[self._centralFrame].update()

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

    def setBuildingList(self, bList):
        self._buildingsList = bList

    def createSideButton(self):
        # build menu and child
        buildButtonList = []
        buttonSize = (settings.SCREEN_WIDTH * settings.UI_SIDE_BAR,
                      (settings.SCREEN_HEIGHT - self._topBar.get_height()) / (len(self._buildingsList) + 4))
        buttonH = self._topBar.get_height()
        for cat, d in self._buildingsList.items():
            buildButtonList.append(UIButton(cat.value, buttonSize, (0, buttonH),
                                            self._fonts[self._currentFont], self.changeMenu))
            buttonH += buttonSize[1]

            size = 1
            for name, value in d.items():
                obj, available = value
                if available:
                    size += 1

            localButtonH = self._topBar.get_height()
            localButtonList = []
            localButtonSize = (settings.SCREEN_WIDTH * settings.UI_SIDE_BAR,
                      (settings.SCREEN_HEIGHT - self._topBar.get_height()) / size)
            for name, value in d.items():
                obj, available = value
                if available:
                    localButtonList.append(UIButton(name.value, localButtonSize, (0, localButtonH),
                                                    self._fonts[self._currentFont], self.selectBuilding, building=obj,
                                                    tooltipType=TooltipType.GUI_BUILDING))
                    localButtonH += localButtonSize[1]
            localButtonList.append(UIButton('Back', localButtonSize, (0, localButtonH),
                                            self._fonts[self._currentFont], self.resetMenu, prevContext='Build'))
            self._sideButtons[cat.value] = localButtonList

        buildButtonList.append(UIButton(BuildingsName.CONNECTOR.value, buttonSize, (0, buttonH),
                                        self._fonts[self._currentFont], self.selectBuilding, building=Connector,
                                        tooltipType=TooltipType.GUI_BUILDING))
        buttonH += buttonSize[1]
        buildButtonList.append(UIButton('Upgrade', buttonSize, (0, buttonH),
                                        self._fonts[self._currentFont], self.upgradeBuilding))
        buttonH += buttonSize[1]
        buildButtonList.append(UIButton('Remove', buttonSize, (0, buttonH),
                                        self._fonts[self._currentFont], self.destroyBuilding,
                                        img=self._guiImg['destructor']))
        buttonH += buttonSize[1]
        buildButtonList.append(UIButton('Back', buttonSize, (0, buttonH),
                                        self._fonts[self._currentFont], self.resetMenu, prevContext='base'))

        self._sideButtons['Build'] = buildButtonList

        # base menu
        baseButtonList = []
        buttonSize = (settings.SCREEN_WIDTH * settings.UI_SIDE_BAR,
                      (settings.SCREEN_HEIGHT - self._topBar.get_height()) / len(self._menuList))
        buttonH = self._topBar.get_height()
        for menu, fct in self._menuList.items():
            baseButtonList.append(UIButton(menu, buttonSize, (0, buttonH), self._fonts[self._currentFont], fct))
            buttonH += buttonSize[1]

        self._sideButtons['base'] = baseButtonList


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

        if self._buildingDestroy is not None:
            self._buildingDestroy.display(screen)

        if self._buildingUpgrade is not None:
            self._buildingUpgrade.display(screen)

        if self._centralFrame is not None:
            self._frameList[self._centralFrame].display(screen)

        if self._tooltipSurf is not None:
            screen.blit(self._tooltipSurf, self._tooltipPos)

    def isOnGui(self):
        return self._onGui

    def checkMousePosition(self, mPos, ):
        onGui = False
        hoveredElem = False

        # Check central frame
        if self._centralFrame is not None:
            onGui = onGui or self._frameList[self._centralFrame].isOn(mPos)
            if self._frameList[self._centralFrame].checkHover(mPos):
                hoveredElem = True

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
            if b.checkHover(mPos):
                hoveredElem = True
                onGui = True
                if b.isNewHover():
                    self.createTooltipUIElem(b)

        if not hoveredElem:
            self._tooltipSurf = None

        self._onGui = onGui

        # Check game board
        if not onGui:
            element = modules.gameManager.gameManager.checkElementAt(mPos)
            if element is not None:
                self.createTooltipUIElem(element)


    def handleMouseButton(self, pressed, mPos, button):
        if button == 1:
            if self._onGui:
                for b in self._sideButtons[self._currentSideMenu]:
                    b.checkMousePressed(pressed, mPos)
                if self._centralFrame is not None:
                    self._frameList[self._centralFrame].checkMousePressed(pressed, mPos)
            elif not pressed and self._buildingSelected is not None:
                self._buildingSelected.tryBuild()
            elif not pressed and self._buildingDestroy is not None:
                self._buildingDestroy.tryDestroy()
            elif not pressed and self._buildingUpgrade is not None:
                self._buildingUpgrade.tryUpgrade()

        elif button == 3:
            pygame.mouse.set_visible(True)
            self._buildingSelected = None
            self._buildingDestroy = None
            self._buildingUpgrade = None

    def resetMenu(self, *arg):
        self._currentSideMenu = arg[2]

    def changeMenu(self, *arg):
        self._currentSideMenu = arg[0]

    def upgradeBuilding(self, *arg):
        pygame.mouse.set_visible(True)
        self._buildingUpgrade = UIBuildingUpgradeSnap(None, self)
        self._buildingSelected = None
        self._buildingDestroy = None

    def destroyBuilding(self, *arg):
        pygame.mouse.set_visible(False)
        self._buildingDestroy = UIBuildingDestroySnap(self._guiImg['destructorMini'], self)
        self._buildingSelected = None
        self._buildingUpgrade = None

    def selectBuilding(self, *arg):
        print("Building {} selected".format(arg[0]))
        if arg[1] is not None:
            pygame.mouse.set_visible(True)
            self._buildingSelected = UIBuildingMouseSnap(arg[1]((-1, -1)), self)
            self._buildingDestroy = None
            self._buildingUpgrade = None

    def changeCentralFrame(self, *arg):
        self._centralFrame = arg[0]

    def closeCentralFrame(self, *arg):
        self._centralFrame = None

    def getFrameMenu(self, name):
        return self._frameList[name]

guiManager = GuiManager()