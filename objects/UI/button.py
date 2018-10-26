"""
Title: button File
Desc: UIButton class
Creation Date:  22/10/18
LastMod Date: 25/10/18
TODO:
"""

import pygame
from settings.enums import Colors
from objects.UI.hoverable import UIHoverable


class UIButton(UIHoverable):
    def __init__(self, title, size, pos, font, clickFct=None, img=None, building=None, prevContext='', tooltipType=None):
        super().__init__(pos, size, tooltipType)
        self._title = title
        self._building = building
        self._tmpBuild = None
        if building is not None:
            self._tmpBuild = building((-1, -1))
            self._img = self._tmpBuild.buildingData['uiImg']
        else:
            self._img = img
        self._clickFct = clickFct
        self._prevContext = prevContext
        self._baseSurface = pygame.Surface(size)
        self._baseSurface.fill(Colors.WHITE.value)
        pygame.draw.rect(self._baseSurface, Colors.BLACK.value, self._baseSurface.get_rect(), 2)
        self._pressedSurface = pygame.Surface(size)
        self._pressedSurface.fill(Colors.GREY.value)
        pygame.draw.rect(self._pressedSurface, Colors.BLACK.value, self._pressedSurface.get_rect(), 2)
        self._hoverSurface = pygame.Surface(size)
        self._hoverSurface.fill(Colors.LIGHT_GREY.value)
        pygame.draw.rect(self._hoverSurface, Colors.BLACK.value, self._hoverSurface.get_rect(), 2)
        self._text = font.render(title, 1, Colors.BLACK.value)
        if self._img is not None:
            self._baseSurface.blit(self._img, ((size[0] - self._img.get_width()) / 2,
                                                (size[1] - self._img.get_height()) / 2))
            self._hoverSurface.blit(self._img, ((size[0] - self._img.get_width()) / 2,
                                                (size[1] - self._img.get_height()) / 2))
            self._pressedSurface.blit(self._img, ((size[0] - self._img.get_width()) / 2,
                                                (size[1] - self._img.get_height()) / 2))
        else:
            self._baseSurface.blit(self._text, ((size[0] - self._text.get_width()) / 2,
                                                (size[1] - self._text.get_height()) / 2))
            self._hoverSurface.blit(self._text, ((size[0] - self._text.get_width()) / 2,
                                                (size[1] - self._text.get_height()) / 2))
            self._pressedSurface.blit(self._text, ((size[0] - self._text.get_width()) / 2,
                                                (size[1] - self._text.get_height()) / 2))

    def getBuildingData(self):
        if self._tmpBuild:
            return self._tmpBuild.buildingData
        else:
            return None

    def draw(self, screen, offset=(0,0)):
        surface = self._pressedSurface if self._pressed else self._hoverSurface if self._hover else self._baseSurface
        screen.blit(surface, (self._pos[0] + offset[0], self._pos[1] + offset[1]))


    def checkMousePressed(self, pressed, mPos):
        isInside = self._rect.collidepoint(mPos[0], mPos[1])
        if not pressed and self._pressed and isInside:
            self.onClick()
            self._pressed = False
        elif pressed and isInside:
            self._pressed = True

    def onClick(self):
        print("Click on " + self._title)
        if self._clickFct is not None:
            self._clickFct(self._title, self._building, self._prevContext)
