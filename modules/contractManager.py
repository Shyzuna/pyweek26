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
        self.contracts = [
            Contract(contractor="New York", reward=1000, objective=10),
            Contract(contractor="Shanghai", reward=100, objective=2),
            Contract(contractor="Paris", reward=400, objective=5)
        ]

        self.current_contract = None
        self.showGui = False
        self.contour = 5
        self.popupTopLeft = (settings.TILE_WIDTH * 3, settings.TILE_HEIGHT * 2)
        self.popup = pygame.Rect(self.contour,
                                 self.contour,
                                 settings.CONTRACTS_WINDOW_WIDTH,
                                 settings.CONTRACTS_WINDOW_HEIGHT)
        self.popupContour = pygame.Surface((settings.CONTRACTS_WINDOW_WIDTH + 2 * self.contour,
                                            settings.CONTRACTS_WINDOW_HEIGHT + 2 * self.contour))
        self.fonts = {
            'small': pygame.font.Font(os.path.join(settings.FONT_PATH, 'VCR_OSD.ttf'), 12),
            'medium': pygame.font.Font(os.path.join(settings.FONT_PATH, 'VCR_OSD.ttf'), 15),
            'large': pygame.font.Font(os.path.join(settings.FONT_PATH, 'VCR_OSD.ttf'), 20)
        }

    def display(self, screen):
        self.popupContour.fill(Colors.BLACK.value)
        self.popupContour.fill(Colors.WHITE.value, self.popup)
        screen.blit(self.popupContour, self.popupTopLeft)
        text = self.fonts['large'].render('Contracts', 1, Colors.BLACK.value)
        screen.blit(text, (self.popupTopLeft[0] + settings.CONTRACTS_WINDOW_WIDTH / 2 - text.get_width() / 2,
                           self.popupTopLeft[1] + self.contour))
        # Display current contract
        if self.current_contract is None:
            pass
        else:
            x = self.popupTopLeft[0] + 0.5 * settings.TILE_WIDTH
            y = self.popupTopLeft[1] + settings.TILE_HEIGHT
            self.current_contract.display(screen, (x, y), self.fonts)

        # Display available contracts
        x = self.popupTopLeft[0]
        y = self.popupTopLeft[1] + 2 * settings.TILE_HEIGHT
        for contract in self.contracts:
            contract.display(screen, (x, y), self.fonts)
            # TODO: fix vertical drift in regard to max number of contracts
            y += settings.TILE_HEIGHT


contractManager = ContractManager()
