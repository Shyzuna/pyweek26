"""
Title: researchFrame File
Desc: UIResearchFrame class
Creation Date:  26/10/18
LastMod Date: 26/10/18
TODO:
    - Add level of hq
    - Remove white slice at the bottom
"""

import pygame
from settings.enums import Colors, TooltipType
from objects.UI.button import UIButton
from objects.UI.progressBar import UIProgressBar
import modules.researchManager
from settings.researchSettings import ALL_RESEARCH
import modules.guiManager


class UIResearchFrame(object):
    def __init__(self, size, pos, font, guiManager):
        self._size = size
        self._pos = pos
        self._font = font
        self._rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self._surface = None
        self._exitButton = None
        self._progressBar = None
        self._guiManager = guiManager
        self._researchByLine = 5
        self._maxLine = 2
        self._researchButton = {}
        self.createMainSurf(size)

    def createMainSurf(self, size):
        # put setting Border ?
        # put factor in param ?
        self._surface = pygame.Surface(self._size)
        self._surface.fill(Colors.WHITE.value)
        pygame.draw.rect(self._surface, Colors.BLACK.value, pygame.Rect(0, 0, size[0] - 1, size[1] - 1), 2)
        topBar = pygame.Surface((size[0] - 4, size[1] * 0.1))
        text = self._font.render('Research', 1, Colors.BLACK.value)
        topBar.fill(Colors.WHITE.value)
        topBar.blit(text, (int((size[0] - text.get_width()) / 2), int((topBar.get_height() - text.get_height()) / 2)))
        self._surface.blit(topBar, (2, 2))
        self._exitButton = UIButton('Close', (int(size[0] * 0.1), topBar.get_height()),
                                    (self._pos[0], self._pos[1]), self._font, self._guiManager.closeCentralFrame)
        self._progressBar = UIProgressBar((self._size[0] * 0.5, self._size[1] * 0.05),
                                          (int((self._size[0] - (self._size[0] * 0.5)) / 2 + self._pos[0]),
                                          topBar.get_height() + self._pos[1]), self._font, Colors.BLUE.value)
        colorList = [(42, 80, 169), (0, 163, 64), (130, 0, 35), (166, 88, 0)]
        blockSize = (self._size[0], int((self._size[1] * 0.84) / 4))
        startH = int(self._size[1] * 0.16)
        for idx, c in enumerate(colorList):
            text = self._font.render('Level ' + str(idx), 1, Colors.BLACK.value)
            surface = pygame.Surface(blockSize)
            surface.fill(c)
            pygame.draw.rect(surface, Colors.BLACK.value, pygame.Rect(0, 0, blockSize[0] - 1, blockSize[1] - 1), 2)
            surface.blit(text, (blockSize[0] * 0.05, int((blockSize[1] - text.get_height()) / 2)))
            self._surface.blit(surface, (0, startH))

            localButtonList = []
            line = 0
            elemNumber = 0
            buttonSize = (int((blockSize[0] - (blockSize[0] * 0.1 + text.get_width() + (blockSize[1] * 0.05 * self._researchByLine))) / self._researchByLine),
                          int((blockSize[1] - blockSize[1] * 0.1) / self._maxLine))
            posX = self._pos[0] + blockSize[0] * 0.1 + text.get_width()
            posY = startH + self._pos[1] + blockSize[1] * 0.05
            hqLevel = modules.researchManager.researchManager.getHqLevel()
            print(hqLevel < (idx + 1))
            for research in ALL_RESEARCH[str(idx + 1)]:
                button = UIButton(research['name'], buttonSize,
                                  (posX + elemNumber * (buttonSize[0] + blockSize[1] * 0.05),
                                   posY + line * buttonSize[1]), self._font, self.clickStartResearch,
                                  disabled=(hqLevel < (idx + 1)),
                                  researchInfo=[str(idx + 1), elemNumber + (line * self._researchByLine)],
                                  tooltipType=TooltipType.RESEARCH_TIP)
                localButtonList.append(button)
                elemNumber += 1
                if elemNumber >= self._researchByLine:
                    elemNumber = 0
                    line += 1
            self._researchButton[str(idx + 1)] = localButtonList
            startH += blockSize[1]


    def display(self, screen):
        screen.blit(self._surface, self._pos)
        self._exitButton.draw(screen)
        self._progressBar.draw(screen)
        for level, l in self._researchButton.items():
            for b in l:
                b.draw(screen)

    def isOn(self, mPos):
        return self._rect.collidepoint(mPos[0], mPos[1])

    def checkHover(self, mPos):
        hoveredElem = False
        hoveredElem = hoveredElem or self._exitButton.checkHover(mPos)
        for level, l in self._researchButton.items():
            for b in l:
                hoveredElem = hoveredElem or b.checkHover(mPos)
                if b.isNewHover():
                    modules.guiManager.guiManager.createTooltipUIElem(b)
        return hoveredElem

    def checkMousePressed(self, pressed, mPos):
        self._exitButton.checkMousePressed(pressed, mPos)
        for level, l in self._researchButton.items():
            for b in l:
                b.checkMousePressed(pressed, mPos)

    def update(self):
        if modules.researchManager.researchManager.isSearching():
            maxT, currentT = modules.researchManager.researchManager.getTimers()
            self._progressBar.setMaxValue(maxT)
            self._progressBar.setCurrentValue(maxT - currentT)
            self._progressBar.update()

    def setResearchCompleted(self, lvl, number):
        self._researchButton[lvl][number].setCompleted(True)
        self._progressBar.setMaxValue(0)
        self.update()

    def clickStartResearch(self, *arg):
        modules.researchManager.researchManager.startResearch(arg[3][0], arg[3][1])

    def unlockResearchLevel(self, level):
        for b in self._researchButton[level]:
            b.setDisabled(False)

    def startResearch(self, lvl, number):
        self._researchButton[lvl][number].setRunning(True)