"""
Title: earthFrame File
Desc: UIEarthFrame class
Creation Date:  26/10/18
LastMod Date: 26/10/18
TODO:
"""

import pygame
from settings import settings
from settings.enums import Colors
from objects.UI.button import UIButton

class UIEarthFrame(object):
    def __init__(self, size, pos, font, guiManager, earth):
        self._size = size
        self._pos = pos
        self._font = font
        self._rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self._surface = None
        self._exitButton = None
        self._guiManager = guiManager
        self.earth = earth
        self.createMainSurf(size)
        #self.createContent(size)

    def createMainSurf(self, size):
        # put setting Border ?
        self._surface = pygame.Surface(self._size)
        self._surface.fill(Colors.GREEN.value)
        pygame.draw.rect(self._surface, Colors.BLACK.value, pygame.Rect(0, 0, size[0] - 1, size[1] - 1), 2)
        self.topBar = pygame.Surface((size[0] - 4, size[1] * 0.1))
        text = self._font.render('Earth', 1, Colors.BLACK.value)
        self.topBar.fill(Colors.GREY.value)
        self.topBar.blit(text, (int((size[0] - text.get_width()) / 2), int((self.topBar.get_height() - text.get_height()) / 2)))
        self._surface.blit(self.topBar, (2, 2))
        self._exitButton = UIButton('Close', (int(size[0] * 0.1), self.topBar.get_height()),
                                    (self._pos[0], self._pos[1]), self._font, self._guiManager.closeCentralFrame)

        self._earthSurface = pygame.Surface((size[0] - 4, size[1] * 0.9))
        self._earthSurface.fill(Colors.BLUE.value)
        #self._surface.blit(self._earthSurface, (2, self._pos[1]))

    def createContent(self, size):
        self._earthSurface = pygame.Surface((size[0] - 4, size[1] * 0.9))
        self._earthSurface.fill(Colors.BLUE.value)
        self._surface.blit(self._earthSurface, (2, 5))

    def display(self, screen):
        screen.blit(self._surface, self._pos)

        x, y = self._pos[0] + 4 * 1.10, self._pos[1] + self.topBar.get_height() * 1.10
        for town, data in self.earth.towns.items():
            townText = self._font.render('Ville: ' + town.value, 1, Colors.BLACK.value)
            screen.blit(townText, (x, y))
            y += 20 * 1.10

            statusText = self._font.render('Statut: ' + data['status'].value, 1, Colors.BLACK.value)
            screen.blit(statusText, (x, y))
            y += 20 * 2.00

        self._exitButton.draw(screen)

    def isOn(self, mPos):
        return self._rect.collidepoint(mPos[0], mPos[1])

    def checkMousePressed(self, pressed, mPos):
        self._exitButton.checkMousePressed(pressed, mPos)

    def checkHover(self, mPos):
        self._exitButton.checkHover(mPos)

    def update(self):
        pass