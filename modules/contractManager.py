import pygame
import os
import numpy
import modules.gameManager

from settings import settings
from settings.enums import Colors
from settings.enums import Towns
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

        self.contracts = []
        self.runningContractIndex = None

        for i in range(settings.MAX_AVAILABLE_CONTRACTS):
            self.generateContract()

        # GUI
        self.contour = 2

        # Whole contracts window
        self.popupTopLeft = framePos
        self.popup = pygame.Rect(self.contour,
                                 self.contour,
                                 self.CONTRACTS_WINDOW_WIDTH,
                                 self.CONTRACTS_WINDOW_HEIGHT)
        self.popupContour = pygame.Surface((self.CONTRACTS_WINDOW_WIDTH + 2 * self.contour,
                                            self.CONTRACTS_WINDOW_HEIGHT + 2 * self.contour))

        # Top bar
        self.topBarTopLeft = self.popupTopLeft
        self.topBarHeight = self.CONTRACTS_WINDOW_HEIGHT / 10
        self.topBar = pygame.Rect(self.contour, self.contour,
                                  self.CONTRACTS_WINDOW_WIDTH, self.topBarHeight)
        self.topBarContour = pygame.Surface((self.CONTRACTS_WINDOW_WIDTH + 2 * self.contour,
                                             self.CONTRACTS_WINDOW_HEIGHT / 10 + 2 * self.contour))


        # Quit button
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

        self.pressed = False

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
        i = 0
        for contract in self.contracts:
            color = Colors.RED.value if i == self.runningContractIndex else Colors.BLACK.value
            contract.display(screen, self.contractWindowContour, self.contractWindow, (x, y), self.fonts, color)
            y += (self.CONTRACTS_WINDOW_HEIGHT - self.topBarHeight) / settings.MAX_AVAILABLE_CONTRACTS
            i += 1

    def isOn(self, mPos):
        rect = pygame.Rect(self.popupTopLeft, self.popup.size)
        return rect.collidepoint(mPos[0], mPos[1])

    def onClick(self, contractIndex):
        # Check if any contract is running
        if self.runningContractIndex is None:
            self.contracts[contractIndex].current = True
            self.runningContractIndex = contractIndex


    def checkHover(self, mPos):
        self.exitButton.checkHover(mPos)

    def checkMousePressed(self, pressed, mPos):
        # Check click on exit
        self.exitButton.checkMousePressed(pressed, mPos)

        # Check click on contract
        x = self.popupTopLeft[0]
        y = self.popupTopLeft[1] + self.topBarHeight
        i = 0
        for contract in self.contracts:
            rect = pygame.Rect((x, y), self.contractWindow.size)
            y += (self.CONTRACTS_WINDOW_HEIGHT - self.topBarHeight) / settings.MAX_AVAILABLE_CONTRACTS
            isInside = rect.collidepoint(mPos[0], mPos[1])
            if not pressed and self.pressed and isInside:
                self.onClick(contractIndex=i)
                self.pressed = False
            elif pressed and isInside:
                self.pressed = True
            i += 1

    def updateRunningContract(self, town, energySent):
        # Check if any contract is running
        if self.runningContractIndex is not None:
            runningContract = self.contracts[self.runningContractIndex]
            # Confirm town equality
            if runningContract.town == town:
                runningContract.update(energySent)

    def updateContracts(self, town, energySent):
        # Update running contract
        self.updateRunningContract(town, energySent)
        print(town)
        # Is the running contract complete?
        if self.runningContractIndex is not None:
            runningContract = self.contracts[self.runningContractIndex]
            if runningContract.left <= 0:
                # Delete it, send the reward and generate a new one
                modules.gameManager.gameManager.getPlayer().addCredits(runningContract.reward)
                del self.contracts[self.runningContractIndex]
                self.runningContractIndex = None
                self.generateContract()

    def update(self):
        pass

    def generateContract(self):
        factor = modules.gameManager.gameManager.getInstantProd()
        maxSeed = 10
        seed = numpy.random.randint(1, maxSeed + 1)
        rewardFactors = [1, 1.2, 1.5]
        town = numpy.random.choice(list(Towns)).value
        objective = int((factor + 1) * seed)
        if seed <= int(maxSeed/3):
            reward = int(objective * 100 * rewardFactors[0])
        elif seed <= int(2 * maxSeed / 3):
            reward = int(objective * 100 * rewardFactors[1])
        else:
            reward = int(objective * 100 * rewardFactors[2])

        self.contracts.append(Contract(town, reward, objective))


contractManager = ContractManager()
