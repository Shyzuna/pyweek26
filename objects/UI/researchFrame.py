"""
Title: researchFrame File
Desc: UIResearchFrame class
Creation Date:  26/10/18
LastMod Date: 26/10/18
TODO:
"""

import pygame
from settings.enums import Colors


class UIResearchFrame(object):
    def __init__(self, size, pos):
        self._size = size
        self._pos = pos
        self._rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self._surface = pygame.Surface(self._size)
        self._surface.fill(Colors.WHITE.value)
        pygame.draw.rect(self._surface, Colors.BLACK.value, pygame.Rect(0, 0, size[0] - 1, size[1] - 1), 2)

    def display(self, screen):
        screen.blit(self._surface, self._pos)

    def isOn(self, mPos):
        return self._rect.collidepoint(mPos[0], mPos[1])

    def checkMousePressed(self, pressed, mPos):
        pass
