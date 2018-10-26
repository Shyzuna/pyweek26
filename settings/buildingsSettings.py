"""
Title: buildingsSettings File
Desc: All building settings
Creation Date: 26/10/17
LastMod Date: 26/10/17
TODO:
*
"""

from settings.enums import BuildingsName, ObjectCategory
from settings import settings
import pygame
import os


ALL_BUILDINGS_SETTINGS = {
    BuildingsName.BATTERY: {
        'name': BuildingsName.BATTERY.value,
        'desc': 'Contains energy.',
        'cost': {ObjectCategory.CREDITS: 100},
        'produce': {},
        'consume': {},
        'capacity': {ObjectCategory.ENERGY: 50},
        'allowedSpot': None,
        'deletable': True,
        'constructable': True,
        'constructionTime': 0,
        'size': (1, 1),
        'uiImg': pygame.transform.scale(pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'BATTERY.png')),
                                        (64, 64)),
        'animImg': [
            pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'BATTERY.png'))
        ]
    },
    BuildingsName.DRILL: {
        'name': BuildingsName.DRILL.value,
        'desc': 'Collect Hydrogen in exchange of energy.',
        'cost': {ObjectCategory.CREDITS: 100},
        'produce': {ObjectCategory.HYDROGEN: 1},
        'consume': {ObjectCategory.ENERGY: 5},
        'capacity': {},
        'allowedSpot': [ObjectCategory.HYDROGEN],
        'deletable': True,
        'constructable': True,
        'constructionTime': 0,
        'size': (1, 1),
        'uiImg': pygame.transform.scale(pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'DRILL.png')),
                                        (64, 64)),
        'animImg': [
            pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'DRILL.png'))
        ]
    },
    BuildingsName.CRUSHER: {
        'name': BuildingsName.CRUSHER.value,
        'desc': 'Collect Helium3 in exchange of energy.',
        'cost': {ObjectCategory.CREDITS: 100},
        'produce': {ObjectCategory.TRIHELIUM: 1},
        'consume': {ObjectCategory.ENERGY: 1},
        'capacity': {},
        'allowedSpot': [ObjectCategory.TRIHELIUM],
        'deletable': True,
        'constructable': True,
        'constructionTime': 0,
        'size': (1, 1),
        'uiImg': pygame.transform.scale(pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'CRUSHER.png')),
                                        (64, 64)),
        'animImg': [
            pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'CRUSHER.png'))
        ]
    },
    BuildingsName.SOLARPANEL: {
        'name': BuildingsName.SOLARPANEL.value,
        'desc': 'Produce energy from sunlight.',
        'cost': {ObjectCategory.CREDITS: 100},
        'produce': {ObjectCategory.ENERGY: 10},
        'consume': {},
        'capacity': {},
        'allowedSpot': None,
        'deletable': True,
        'constructable': True,
        'constructionTime': 0,
        'size': (1, 1),
        'uiImg': pygame.transform.scale(pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'SOLARPANEL.png')),
                                        (64, 64)),
        'animImg': [
            pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'SOLARPANEL.png'))
        ]
    },
    BuildingsName.HEADQUARTERS: {
        'name': BuildingsName.HEADQUARTERS.value,
        'desc': 'Main building for research and command base.',
        'cost': {ObjectCategory.CREDITS: 100},
        'produce': {},
        'consume': {},
        'capacity': {},
        'allowedSpot': None,
        'deletable': False,
        'constructable': False,
        'constructionTime': 0,
        'size': (1, 1),
        'uiImg': pygame.transform.scale(pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'HEADQUARTERS.png')),
                                        (64, 64)),
        'animImg': [
            pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'HEADQUARTERS.png'))
        ]
    },
}