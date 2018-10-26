"""
Title: researchFrame File
Desc: UIResearchFrame class
Creation Date:  26/10/18
LastMod Date: 26/10/18
TODO:
"""

import pygame
from settings.enums import Colors
from objects.UI.button import UIButton


class UIResearchFrame(object):
    def __init__(self, size, pos, font, guiManager):
        self._size = size
        self._pos = pos
        self._font = font
        self._rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self._surface = None
        self._exitButton = None
        self._guiManager = guiManager
        self.createMainSurf(size)

    def createMainSurf(self, size):
        # put setting Border ?
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

    def display(self, screen):
        screen.blit(self._surface, self._pos)
        self._exitButton.draw(screen)

    def isOn(self, mPos):
        return self._rect.collidepoint(mPos[0], mPos[1])

    def checkHover(self, mPos):
        self._exitButton.checkHover(mPos)

    def checkMousePressed(self, pressed, mPos):
        self._exitButton.checkMousePressed(pressed, mPos)
