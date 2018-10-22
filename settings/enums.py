"""
Title: colors File
Desc: Colors enumeration
Creation Date: 15/10/17
LastMod Date: 15/10/17
TODO:
*
"""

from enum import Enum

class Colors(Enum):
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    YELLOW = (255,255,0)
    BLUE = (0,0,255)
    RED = (255, 0, 0)
    GREY = (125, 125, 125)
    LIGHT_GREY = (200, 200, 200)

class ObjectCategory(Enum):
    """
    Enum for object names
    """
    HYDROGEN = 'HYDROGEN'
    DIHYGROGEN = 'DIHYDROGEN'
    TRIHYGROGEN = 'TRIHYDROGEN'
    TRIHELIUM = 'TRIHELIUM'
    ENERGY = 'ENERGY'

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
