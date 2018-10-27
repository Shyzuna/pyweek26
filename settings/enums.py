"""
Title: colors File
Desc: Colors enumeration
Creation Date: 22/10/17
LastMod Date: 25/10/17
TODO:
*
"""

from enum import Enum
import pygame

class Colors(Enum):
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    YELLOW = (255,255,0)
    BLUE = (0,0,255)
    RED = (255, 0, 0)
    GREY = (125, 125, 125)
    LIGHT_GREY = (200, 200, 200)
    LIGHT_CYAN = (14, 174, 204)
    GREEN = (0, 255, 0)
    BLUE_OCEAN = (9, 127, 217)

class ObjectCategory(Enum):
    """
    Enum for object names
    """
    HYDROGEN = 'HYDROGEN'
    DIHYDROGEN = 'DIHYDROGEN'
    TRIHYDROGEN = 'TRIHYDROGEN'
    TRIHELIUM = 'TRIHELIUM'
    ENERGY = 'ENERGY'
    CREDITS = 'CREDITS'


class BuildingShortcuts(Enum):
    """
    Enum for building shortcuts
    """
    BATTERY = pygame.K_1
    SOLARPANEL = pygame.K_2
    DRILL = pygame.K_3
    CRUSHER = pygame.K_4

class BuildingsName(Enum):
    """
    Enum for all buildings
    """
    BATTERY = "Battery"
    SOLARPANEL = "Solar panel"
    DRILL = "Drill"
    CRUSHER = "Crusher"
    HEADQUARTERS = 'Head Quarters'
    WAREHOUSE_HYDROGEN = 'Warehouse Hydrogen'
    HYDROGEN_PLANT = 'Hydrogen Plant'
    DIHYDROGEN_PLANT = 'Dihydrogen Plant'
    CONNECTOR = 'Connector'
    TRANSMITTER = 'Transmitter'
    HYDROGEN_COMBINER = 'Hydrogen Combiner'
    WAREHOUSE_DIHYDROGEN = 'Warehouse Dihydrogen'

class BuildingTypes(Enum):
    """
    Enum for the several buildings types
    """
    GENERAL = 'General'
    GATHERER = 'Gatherer'
    REFINER = 'Refiner'
    PRODUCER = 'Producer'
    CAPACITOR = 'Capacitor'
    CONNECTOR = 'Connector'

class BuildingStates(Enum):
    """
    Enum for the several buildings states
    """
    ON = 'ON'
    OFF = 'OFF'

class TooltipType(Enum):
    """
    Enum for tooltip type
    """
    TEXT_TIP = 0
    GUI_BUILDING = 1
    IG_BUILDING = 2
    RESEARCH_TIP = 3

class ResearchType(Enum):
    """
    Enum for research Type
    """
    UNLOCK = 0
    UPGRADE = 1

class Towns(Enum):
    """
    Enum for towns
    """
    MOSCOW = 'Moscow'
    NEW_YORK = 'New York'
    SHANGAI = 'Shangai'
    PARIS = 'Paris'
    SYDNEY = 'Sydney'

class LinkStatus(Enum):
    """"
    Enum for link status
    """
    OFFLINE = 'Offline'
    ONLINE = 'Online'