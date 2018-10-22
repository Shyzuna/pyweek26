"""
Title: button File
Desc: UIButton class
Creation Date:  22/10/18
LastMod Date: 22/10/18
TODO:
"""

import pygame
from settings.enums import Colors


class UIButton(object):
    def __init__(self, title, size, pos, font, clickFct=None, img=''):
        self._title = title
        self._img = img
        self._clickFct = clickFct
        self._hover = False
        self._pressed = False
        self._pos = pos
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
        self._baseSurface.blit(self._text, ((size[0] - self._text.get_width()) / 2,
                                            (size[1] - self._text.get_height()) / 2))
        self._hoverSurface.blit(self._text, ((size[0] - self._text.get_width()) / 2,
                                            (size[1] - self._text.get_height()) / 2))
        self._pressedSurface.blit(self._text, ((size[0] - self._text.get_width()) / 2,
                                            (size[1] - self._text.get_height()) / 2))
        self._rect = pygame.Rect(pos[0], pos[1], size[0], size[1])

    def draw(self, screen):
        surface = self._pressedSurface if self._pressed else self._hoverSurface if self._hover else self._baseSurface
        screen.blit(surface, self._pos)

    def checkHover(self, mPos):
        self._hover = self._rect.collidepoint(mPos[0], mPos[1])
        if not self._hover:
            self._pressed = False

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
            self._clickFct(self._title)
