"""
Title: hoverable File
Desc: UIHoverable class
Creation Date:  26/10/18
LastMod Date: 26/10/18
TODO:
"""

import pygame

class UIHoverable(object):
    def __init__(self, pos, size, tooltipType, disabled):
        self._lastHover = False
        self._hover = False
        self._pressed = False
        self._disabled = disabled
        self._completed = False  # Research only
        self._running = False  # Research only
        self._pos = pos
        self._tooltipType = tooltipType
        self._rect = pygame.Rect(pos[0], pos[1], size[0], size[1])

    def checkHover(self, mPos):
        self._lastHover = self._hover
        self._hover = self._rect.collidepoint(mPos[0], mPos[1])
        if not self._hover:
            self._pressed = False
        return self._hover

    def isNewHover(self):
        return self._hover and not self._lastHover

    def getTooltipType(self):
        return self._tooltipType

    def setDisabled(self, val):
        self._disabled = val

    def setCompleted(self, val):
        self._completed = val
        if self._completed:
            self._disabled = True
            self._running = False

    def setRunning(self, val):
        self._running = val
