"""
Title: colors File
Desc: Colors enumeration
Creation Date: 15/10/17
LastMod Date: 15/10/17
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

class ObjectCategory(Enum):
    """
    Enum for object names
    """
    HYDROGEN = 'HYDROGEN'
    DIHYGROGEN = 'DIHYDROGEN'
    TRIHYGROGEN = 'TRIHYDROGEN'
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

class Buildings(Enum):
    """
    Enum for all buildings
    """
    BATTERY = "Battery"
    SOLARPANEL = "Solar panel"
    DRILL = "Drill"
    CRUSHER = "Crusher"

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
