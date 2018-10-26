import pygame
import os

from settings import settings
from settings.enums import Colors
from objects.contract import Contract


class ContractManager:

    def __init__(self):
        pass

    def init(self):

        pygame.font.init()

        self.CONTRACTS_WINDOW_WIDTH = settings.SCREEN_WIDTH - settings.TILE_WIDTH * settings.CONTRACTS_WINDOW_GAP_X
        self.CONTRACTS_WINDOW_HEIGHT = settings.SCREEN_HEIGHT - settings.TILE_HEIGHT * settings.CONTRACTS_WINDOW_GAP_Y

        self.contracts = [
            Contract(contractor="New York", reward=1000, objective=10),
            Contract(contractor="Shanghai", reward=100, objective=2),
            Contract(contractor="Paris", reward=400, objective=5)
        ]

        self.current_contract = Contract(contractor="Moscow", reward=1000, objective=10)
        self.showGui = False
        self.contour = 5
        self.popupTopLeft = (settings.TILE_WIDTH * 3, settings.TILE_HEIGHT * 2)
        self.popup = pygame.Rect(self.contour,
                                 self.contour,
                                 self.CONTRACTS_WINDOW_WIDTH,
                                 self.CONTRACTS_WINDOW_HEIGHT)
        self.popupContour = pygame.Surface((self.CONTRACTS_WINDOW_WIDTH + 2 * self.contour,
                                            self.CONTRACTS_WINDOW_HEIGHT + 2 * self.contour))

        self.QUIT_BUTTON_SIZE = 20
        self.quitButtonTopLeft = self.popupTopLeft
        self.quitButton = pygame.Rect(self.contour, self.contour,
                                      self.QUIT_BUTTON_SIZE, self.QUIT_BUTTON_SIZE)

        self.quitButtonContour = pygame.Surface((self.QUIT_BUTTON_SIZE + 2 * self.contour,
                                                 self.QUIT_BUTTON_SIZE + 2 * self.contour))

        self.fonts = {
            'small': pygame.font.Font(os.path.join(settings.FONT_PATH, 'VCR_OSD.ttf'), 12),
            'medium': pygame.font.Font(os.path.join(settings.FONT_PATH, 'VCR_OSD.ttf'), 15),
            'large': pygame.font.Font(os.path.join(settings.FONT_PATH, 'VCR_OSD.ttf'), 20)
        }

    def display(self, screen):
        # Display white background window with black edges
        self.popupContour.fill(Colors.BLACK.value)
        self.popupContour.fill(Colors.WHITE.value, self.popup)
        screen.blit(self.popupContour, self.popupTopLeft)

        # Display title
        text = self.fonts['large'].render('Contracts', 1, Colors.BLACK.value)
        screen.blit(text, (self.popupTopLeft[0] + self.CONTRACTS_WINDOW_WIDTH / 2 - text.get_width() / 2,
                           self.popupTopLeft[1] + self.contour))

        # Display quit button
        self.quitButtonContour.fill(Colors.BLACK.value)
        self.quitButtonContour.fill(Colors.RED.value, self.quitButton)
        screen.blit(self.quitButtonContour, self.quitButtonTopLeft)

        # Display available contracts
        x = self.popupTopLeft[0]
        y = self.popupTopLeft[1] + settings.TILE_HEIGHT
        for contract in self.contracts:
            y += (self.CONTRACTS_WINDOW_HEIGHT - 1 * settings.TILE_HEIGHT) / settings.MAX_AVAILABLE_CONTRACTS
            contract.display(screen, (x, y), self.fonts, Colors.BLACK.value)

        # Display current contract
        if self.current_contract is None:
            pass
        else:
            x = self.popupTopLeft[0]
            y = self.popupTopLeft[1] + settings.TILE_HEIGHT
            self.current_contract.display(screen, (x, y), self.fonts, Colors.RED.value)

    def isOn(self, mPos):
        return self.popup.collidepoint(mPos[0], mPos[1])

    def checkMousePressed(self, pressed, mPos):
        pass


contractManager = ContractManager()
