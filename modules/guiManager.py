"""
Title: guiManager File
Desc: GuiManager class
Creation Date:  22/10/18
LastMod Date: 22/10/18
TODO:
"""

from settings import settings
from settings.enums import Colors
import pygame
import os

class GuiManager(object):
    def __init__(self):
        self._fonts = []
        self._currentFont = 0
        self._topBar = None

    def init(self):
        pygame.font.init()
        self._fonts.append(pygame.font.Font(os.path.join(settings.FONT_PATH, 'VCR_OSD.ttf'), 15))
        self._topBar = pygame.Surface((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT * settings.UI_TOP_BAR))

    def displayGui(self, screen, player):
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

        screen.blit(self._topBar, (0, 0))

guiManager = GuiManager()