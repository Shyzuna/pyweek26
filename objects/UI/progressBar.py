"""
Title: progressBar File
Desc: UIProgressBar class
Creation Date:  27/10/18
LastMod Date: 27/10/18
TODO:
"""

import pygame
from settings.enums import Colors


class UIProgressBar(object):
    def __init__(self, size, pos, font, color):
        self._font = font
        self._size = size
        self._pos = pos
        self._color = color
        self._maxValue = 0
        self._currentValue = 0
        self._lastCurrent = -1
        self._text = None
        self._mainBar = pygame.Surface(size)
        self._mainBar.set_colorkey(Colors.WHITE.value)
        self._mainBar.fill(Colors.WHITE.value)
        pygame.draw.rect(self._mainBar, Colors.BLACK.value, pygame.Rect(0, 0, size[0] - 2, size[1] - 2), 4)
        self._subBar = None
        self.update()

    def setMaxValue(self, val):
        self._maxValue = val

    def setCurrentValue(self, val):
        self._currentValue = val

    def update(self):
        if self._lastCurrent != self._currentValue:
            if self._maxValue != 0:
                ratio = self._currentValue / self._maxValue
                self._text = self._font.render(str(int(ratio * 100)) + '%', 1, Colors.BLACK.value)
                self._subBar = pygame.Surface((int(self._size[0] * ratio), self._size[1]))
                self._subBar.fill(self._color)
            else:
                self._text = self._font.render('-', 1, Colors.BLACK.value)
                self._subBar = pygame.Surface((self._size[0], self._size[1]))
                self._subBar.fill(Colors.WHITE.value)
        self._lastCurrent = self._currentValue

    def draw(self, screen):
        screen.blit(self._subBar, self._pos)
        screen.blit(self._mainBar, self._pos)
        screen.blit(self._text, (int((self._size[0] - self._text.get_width()) / 2) + self._pos[0],
                    int((self._size[1] - self._text.get_height()) / 2) + self._pos[1]))