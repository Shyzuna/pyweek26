import pygame
import os

from settings import settings
from settings.enums import Colors
from objects.UI.button import UIButton
from objects.contract import Contract


class ContractManager:

    def __init__(self):
        pass

    def init(self, frameSize, framePos, guiManager):

        pygame.font.init()

        self.fonts = {
            'small': pygame.font.Font(os.path.join(settings.FONT_PATH, 'VCR_OSD.ttf'), 12),
            'medium': pygame.font.Font(os.path.join(settings.FONT_PATH, 'VCR_OSD.ttf'), 15),
            'large': pygame.font.Font(os.path.join(settings.FONT_PATH, 'VCR_OSD.ttf'), 20)
        }

        self.CONTRACTS_WINDOW_WIDTH = frameSize[0]
        self.CONTRACTS_WINDOW_HEIGHT = frameSize[1]

        self.contracts = [
            Contract(contractor="New York", reward=1000, objective=10),
            Contract(contractor="Shanghai", reward=100, objective=2),
            Contract(contractor="Paris", reward=400, objective=5)
        ]

        self.current_contract = Contract(contractor="Moscow", reward=1000, objective=10)
        self.showGui = False
        self.contour = 2
        self.popupTopLeft = framePos
        self.popup = pygame.Rect(self.contour,
                                 self.contour,
                                 self.CONTRACTS_WINDOW_WIDTH,
                                 self.CONTRACTS_WINDOW_HEIGHT)
        self.popupContour = pygame.Surface((self.CONTRACTS_WINDOW_WIDTH + 2 * self.contour,
                                            self.CONTRACTS_WINDOW_HEIGHT + 2 * self.contour))

        self.topBarTopLeft = self.popupTopLeft
        self.topBarHeight = self.CONTRACTS_WINDOW_HEIGHT / 10
        self.topBar = pygame.Rect(self.contour, self.contour,
                                  self.CONTRACTS_WINDOW_WIDTH, self.topBarHeight)
        self.topBarContour = pygame.Surface((self.CONTRACTS_WINDOW_WIDTH + 2 * self.contour,
                                             self.CONTRACTS_WINDOW_HEIGHT / 10 + 2 * self.contour))

        self.QUIT_BUTTON_SIZE = (self.CONTRACTS_WINDOW_WIDTH / 10, self.topBarHeight)
        self.quitButtonTopLeft = self.popupTopLeft
        self.quitButton = pygame.Rect(self.contour, self.contour,
                                      self.QUIT_BUTTON_SIZE[0], self.QUIT_BUTTON_SIZE[1])

        self.quitButtonContour = pygame.Surface((self.QUIT_BUTTON_SIZE[0] + 2 * self.contour,
                                                 self.QUIT_BUTTON_SIZE[1] + 2 * self.contour))

        self.exitButton = UIButton('Close', (int(self.CONTRACTS_WINDOW_WIDTH / 10), int(self.topBarHeight)),
                                   self.popupTopLeft, self.fonts['medium'], guiManager.closeCentralFrame)

        self.contractWindow = \
            pygame.Rect(self.contour,
                        self.contour,
                        self.CONTRACTS_WINDOW_WIDTH,
                        (self.CONTRACTS_WINDOW_HEIGHT - self.topBarHeight) / settings.MAX_AVAILABLE_CONTRACTS)
        self.contractWindowContour = \
            pygame.Surface((self.CONTRACTS_WINDOW_WIDTH + 2 * self.contour,
                            (self.CONTRACTS_WINDOW_HEIGHT - self.topBarHeight) / settings.MAX_AVAILABLE_CONTRACTS + 2 * self.contour
            )
        )

    def display(self, screen):
        # Display white background window with black edges
        self.popupContour.fill(Colors.BLACK.value)
        self.popupContour.fill(Colors.WHITE.value, self.popup)
        screen.blit(self.popupContour, self.popupTopLeft)

        # Display topbar
        self.topBarContour.fill(Colors.BLACK.value)
        self.topBarContour.fill(Colors.WHITE.value, self.topBar)
        screen.blit(self.topBarContour, self.popupTopLeft)

        # Display title
        text = self.fonts['large'].render('Contracts', 1, Colors.BLACK.value)
        screen.blit(text, (self.popupTopLeft[0] + self.CONTRACTS_WINDOW_WIDTH / 2 - text.get_width() / 2,
                           self.popupTopLeft[1] + self.topBarHeight / 2 - text.get_height() / 2))

        # Display quit button
        self.exitButton.draw(screen)

        # Display available contracts
        x = self.popupTopLeft[0]
        y = self.popupTopLeft[1] + self.topBarHeight
        for contract in self.contracts:
            y += (self.CONTRACTS_WINDOW_HEIGHT - self.topBarHeight) / settings.MAX_AVAILABLE_CONTRACTS
            contract.display(screen, self.contractWindowContour, self.contractWindow, (x, y), self.fonts, Colors.BLACK.value)

        # Display current contract
        if self.current_contract is None:
            pass
        else:
            x = self.popupTopLeft[0]
            y = self.popupTopLeft[1] + self.topBarHeight
            self.current_contract.display(screen, self.contractWindowContour, self.contractWindow, (x, y), self.fonts, Colors.RED.value)

    def isOn(self, mPos):
        return self.popup.collidepoint(mPos[0], mPos[1])

    def checkHover(self, mPos):
        self.exitButton.checkHover(mPos)

    def checkMousePressed(self, pressed, mPos):
        self.exitButton.checkMousePressed(pressed, mPos)

    def update(self):
        pass

contractManager = ContractManager()
