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
        'cost': {ObjectCategory.CREDITS: [100, 150, 300]},
        'produce': {},
        'consume': {},
        'stock': {ObjectCategory.ENERGY: [50, 75, 180]},
        'allowedSpot': None,
        'deletable': True,
        'constructable': True,
        'canLevelUp': True,
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
        'cost': {ObjectCategory.CREDITS: [100, 110, 150]},
        'produce': {ObjectCategory.HYDROGEN: [2, 5, 10]},
        'consume': {ObjectCategory.ENERGY: [5, 10, 15]},
        'stock': {},
        'allowedSpot': [ObjectCategory.HYDROGEN],
        'deletable': True,
        'constructable': True,
        'canLevelUp': True,
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
        'cost': {ObjectCategory.CREDITS: [100, 110, 150]},
        'produce': {ObjectCategory.TRIHELIUM: [1, 2, 3]},
        'consume': {ObjectCategory.ENERGY: [1, 2, 3]},
        'stock': {},
        'allowedSpot': [ObjectCategory.TRIHELIUM],
        'deletable': True,
        'constructable': True,
        'canLevelUp': True,
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
        'cost': {ObjectCategory.CREDITS: [100, 110, 150]},
        'produce': {ObjectCategory.ENERGY: [2, 5, 10]},
        'consume': {},
        'stock': {},
        'allowedSpot': None,
        'deletable': True,
        'constructable': True,
        'canLevelUp': True,
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
        'cost': {ObjectCategory.CREDITS: [100, 110, 150]},
        'produce': {},
        'consume': {},
        'stock': {},
        'allowedSpot': None,
        'deletable': False,
        'constructable': False,
        'canLevelUp': True,
        'constructionTime': 0,
        'size': (1, 1),
        'uiImg': pygame.transform.scale(pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'HEADQUARTERS.png')),
                                        (64, 64)),
        'animImg': [
            pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'HEADQUARTERS.png'))
        ]
    },
    BuildingsName.WAREHOUSE_HYDROGEN: {
        'name': BuildingsName.WAREHOUSE_HYDROGEN.value,
        'desc': 'Contains hydrogen.',
        'cost': {ObjectCategory.CREDITS: [150, 180, 250]},
        'produce': {},
        'consume': {},
        'stock': {ObjectCategory.HYDROGEN: [50, 100, 150]},
        'allowedSpot': None,
        'deletable': True,
        'constructable': True,
        'canLevelUp': True,
        'constructionTime': 0,
        'size': (1, 1),
        'uiImg': pygame.transform.scale(pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'WAREHOUSE_HYDROGEN.png')),
                                        (64, 64)),
        'animImg': [
            pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'WAREHOUSE_HYDROGEN.png'))
        ]
    },
    BuildingsName.HYDROGEN_PLANT: {
        'name': BuildingsName.HYDROGEN_PLANT.value,
        'desc': 'Produce energy with hydrogen.',
        'cost': {ObjectCategory.CREDITS: [200, 210, 250]},
        'produce': {ObjectCategory.ENERGY: [15, 50, 120]},
        'consume': {ObjectCategory.HYDROGEN: [5, 15, 20]},
        'stock': {},
        'allowedSpot': None,
        'deletable': True,
        'constructable': True,
        'canLevelUp': True,
        'constructionTime': 0,
        'size': (1, 1),
        'uiImg': pygame.transform.scale(pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'HYDROGEN_PLANT.png')),
                                        (64, 64)),
        'animImg': [
            pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'HYDROGEN_PLANT.png'))
        ]
    },
    BuildingsName.CONNECTOR: {
        'name': BuildingsName.CONNECTOR.value,
        'desc': 'Building connector.',
        'cost': {ObjectCategory.CREDITS: [10, 0, 0]},
        'produce': {},
        'consume': {},
        'stock': {},
        'allowedSpot': None,
        'deletable': True,
        'constructable': True,
        'canLevelUp': False,
        'constructionTime': 0,
        'size': (1, 1),
        'uiImg': pygame.transform.scale(pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'CONNECTOR.png')),
                                        (64, 64)),
        'animImg': [
            pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'CONNECTOR.png'))
        ]
    },
    BuildingsName.TRANSMITTER: {
        'name': BuildingsName.TRANSMITTER.value,
        'desc': 'Building connector.',
        'cost': {ObjectCategory.CREDITS: [10, 0, 0]},
        'produce': {},
        'consume': {},
        'stock': {},
        'allowedSpot': None,
        'deletable': True,
        'constructable': True,
        'canLevelUp': True,
        'constructionTime': 0,
        'transmitCapacity': [5, 10, 10],
        'size': (1, 1),
        'uiImg': pygame.transform.scale(pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'TRANSMITTER.png')),
                                        (64, 64)),
        'animImg': [
            pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'TRANSMITTER.png'))
        ]
    }
}