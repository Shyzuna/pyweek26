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
        'cost': {ObjectCategory.CREDITS: [100, 150, 300, 400]},
        'produce': {},
        'consume': {},
        'stock': {ObjectCategory.ENERGY: [50, 75, 180, 250]},
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
    BuildingsName.DRILL_HYDROGEN: {
        'name': BuildingsName.DRILL_HYDROGEN.value,
        'desc': 'Collect Hydrogen in exchange of energy.',
        'cost': {ObjectCategory.CREDITS: [100, 110, 150, 250]},
        'produce': {ObjectCategory.HYDROGEN: [2, 5, 10, 25]},
        'consume': {ObjectCategory.ENERGY: [5, 10, 15, 25]},
        'stock': {},
        'allowedSpot': [ObjectCategory.HYDROGEN],
        'deletable': True,
        'constructable': True,
        'canLevelUp': True,
        'constructionTime': 0,
        'size': (1, 1),
        'uiImg': pygame.transform.scale(pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'DRILL_HYDROGEN.png')),
                                        (64, 64)),
        'animImg': [
            pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'DRILL_HYDROGEN.png'))
        ]
    },
    BuildingsName.DRILL_DIHYDROGEN: {
        'name': BuildingsName.DRILL_DIHYDROGEN.value,
        'desc': 'Collect Dihydrogen in exchange of energy.',
        'cost': {ObjectCategory.CREDITS: [100, 110, 150, 200]},
        'produce': {ObjectCategory.DIHYDROGEN: [2, 5, 10, 15]},
        'consume': {ObjectCategory.ENERGY: [5, 10, 15, 20]},
        'stock': {},
        'allowedSpot': [ObjectCategory.DIHYDROGEN],
        'deletable': True,
        'constructable': True,
        'canLevelUp': True,
        'constructionTime': 0,
        'size': (1, 1),
        'uiImg': pygame.transform.scale(pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'DRILL_DIHYDROGEN.png')),
                                        (64, 64)),
        'animImg': [
            pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'DRILL_DIHYDROGEN.png'))
        ]
    },
    BuildingsName.DRILL_TRIHYDROGEN: {
        'name': BuildingsName.DRILL_TRIHYDROGEN.value,
        'desc': 'Collect Trihydrogen in exchange of energy.',
        'cost': {ObjectCategory.CREDITS: [100, 110, 150, 200]},
        'produce': {ObjectCategory.TRIHYDROGEN: [2, 5, 10, 15]},
        'consume': {ObjectCategory.ENERGY: [5, 10, 15, 20]},
        'stock': {},
        'allowedSpot': [ObjectCategory.TRIHYDROGEN],
        'deletable': True,
        'constructable': True,
        'canLevelUp': True,
        'constructionTime': 0,
        'size': (1, 1),
        'uiImg': pygame.transform.scale(pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'DRILL_TRIHYDROGEN.png')),
                                        (64, 64)),
        'animImg': [
            pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'DRILL_TRIHYDROGEN.png'))
        ]
    },
    BuildingsName.CRUSHER: {
        'name': BuildingsName.CRUSHER.value,
        'desc': 'Collect Helium3 in exchange of energy.',
        'cost': {ObjectCategory.CREDITS: [100, 110, 150, 250]},
        'produce': {ObjectCategory.TRIHELIUM: [1, 2, 3, 4]},
        'consume': {ObjectCategory.ENERGY: [1, 2, 3, 4]},
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
        'cost': {ObjectCategory.CREDITS: [100, 110, 150, 250]},
        'produce': {ObjectCategory.ENERGY: [10, 20, 30, 50]},
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
        'cost': {ObjectCategory.CREDITS: [100, 110, 150, 250]},
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
        'cost': {ObjectCategory.CREDITS: [150, 180, 250, 350]},
        'produce': {},
        'consume': {},
        'stock': {ObjectCategory.HYDROGEN: [50, 100, 150, 250]},
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
        'cost': {ObjectCategory.CREDITS: [200, 210, 250, 300]},
        'produce': {ObjectCategory.ENERGY: [15, 50, 120, 180]},
        'consume': {ObjectCategory.HYDROGEN: [5, 15, 20, 30]},
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
    BuildingsName.DIHYDROGEN_PLANT: {
        'name': BuildingsName.DIHYDROGEN_PLANT.value,
        'desc': 'Produce energy with dihydrogen.',
        'cost': {ObjectCategory.CREDITS: [200, 210, 250, 300]},
        'produce': {ObjectCategory.ENERGY: [30, 50, 120, 180]},
        'consume': {ObjectCategory.DIHYDROGEN: [5, 15, 20, 30]},
        'stock': {},
        'allowedSpot': None,
        'deletable': True,
        'constructable': True,
        'canLevelUp': True,
        'constructionTime': 0,
        'size': (1, 1),
        'uiImg': pygame.transform.scale(pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'DIHYDROGEN_PLANT.png')),
                                        (64, 64)),
        'animImg': [
            pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'DIHYDROGEN_PLANT.png'))
        ]
    },
    BuildingsName.CONNECTOR: {
        'name': BuildingsName.CONNECTOR.value,
        'desc': 'Building connector.',
        'cost': {ObjectCategory.CREDITS: [10, 0, 0, 0]},
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
        'cost': {ObjectCategory.CREDITS: [10, 0, 0, 0]},
        'produce': {},
        'consume': {ObjectCategory.ENERGY: [10, 10, 10, 10]},
        'stock': {},
        'allowedSpot': None,
        'deletable': False,
        'constructable': True,
        'canLevelUp': True,
        'constructionTime': 0,
        'transmitCapacity': [5, 10, 10, 10],
        'size': (1, 1),
        'uiImg': pygame.transform.scale(pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'TRANSMITTER.png')),
                                        (64, 64)),
        'animImg': [
            pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'TRANSMITTER.png'))
        ]
    },
    BuildingsName.HYDROGEN_COMBINER: {
        'name': BuildingsName.HYDROGEN_COMBINER.value,
        'desc': 'Building connector.',
        'cost': {ObjectCategory.CREDITS: [180, 200, 280, 360]},
        'produce': {ObjectCategory.DIHYDROGEN: [1, 2, 3, 15]},
        'consume': {ObjectCategory.ENERGY: [10, 14, 18, 26], ObjectCategory.HYDROGEN: [2, 4, 6, 10]},
        'stock': {},
        'allowedSpot': None,
        'deletable': True,
        'constructable': True,
        'canLevelUp': False,
        'constructionTime': 0,
        'size': (1, 1),
        'uiImg': pygame.transform.scale(pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'HYDROGEN_COMBINER.png')),
                                        (64, 64)),
        'animImg': [
            pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'HYDROGEN_COMBINER.png'))
        ]
    },
    BuildingsName.DIHYDROGEN_COMBINER: {
        'name': BuildingsName.DIHYDROGEN_COMBINER.value,
        'desc': 'Building connector.',
        'cost': {ObjectCategory.CREDITS: [180, 200, 280, 360]},
        'produce': {ObjectCategory.TRIHYDROGEN: [1, 2, 3, 15]},
        'consume': {ObjectCategory.ENERGY: [10, 14, 18, 26], ObjectCategory.DIHYDROGEN: [2, 4, 6, 10]},
        'stock': {},
        'allowedSpot': None,
        'deletable': True,
        'constructable': True,
        'canLevelUp': False,
        'constructionTime': 0,
        'size': (1, 1),
        'uiImg': pygame.transform.scale(pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'DIHYDROGEN_COMBINER.png')),
                                        (64, 64)),
        'animImg': [
            pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'DIHYDROGEN_COMBINER.png'))
        ]
    },
    BuildingsName.WAREHOUSE_DIHYDROGEN: {
        'name': BuildingsName.WAREHOUSE_DIHYDROGEN.value,
        'desc': 'Contains dihydrogen.',
        'cost': {ObjectCategory.CREDITS: [180, 200, 280, 360]},
        'produce': {},
        'consume': {},
        'stock': {ObjectCategory.DIHYDROGEN: [20, 50, 100, 200]},
        'allowedSpot': None,
        'deletable': True,
        'constructable': True,
        'canLevelUp': True,
        'constructionTime': 0,
        'size': (1, 1),
        'uiImg': pygame.transform.scale(pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'WAREHOUSE_DIHYDROGEN.png')),
                                        (64, 64)),
        'animImg': [
            pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'WAREHOUSE_DIHYDROGEN.png'))
        ]
    },
    BuildingsName.WAREHOUSE_TRIHYDROGEN: {
        'name': BuildingsName.WAREHOUSE_TRIHYDROGEN.value,
        'desc': 'Contains trihydrogen.',
        'cost': {ObjectCategory.CREDITS: [180, 200, 280, 350]},
        'produce': {},
        'consume': {},
        'stock': {ObjectCategory.TRIHYDROGEN: [20, 50, 100, 200]},
        'allowedSpot': None,
        'deletable': True,
        'constructable': True,
        'canLevelUp': True,
        'constructionTime': 0,
        'size': (1, 1),
        'uiImg': pygame.transform.scale(pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'WAREHOUSE_TRIHYDROGEN.png')),
                                        (64, 64)),
        'animImg': [
            pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'WAREHOUSE_TRIHYDROGEN.png'))
        ]
    },
    BuildingsName.WAREHOUSE_TRIHELIUM: {
        'name': BuildingsName.WAREHOUSE_TRIHELIUM.value,
        'desc': 'Contains trihelium.',
        'cost': {ObjectCategory.CREDITS: [180, 200, 280, 350]},
        'produce': {},
        'consume': {},
        'stock': {ObjectCategory.TRIHELIUM: [20, 50, 100, 150]},
        'allowedSpot': None,
        'deletable': True,
        'constructable': True,
        'canLevelUp': True,
        'constructionTime': 0,
        'size': (1, 1),
        'uiImg': pygame.transform.scale(pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'WAREHOUSE_TRIHELIUM.png')),
                                        (64, 64)),
        'animImg': [
            pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'WAREHOUSE_TRIHELIUM.png'))
        ]
    }
}
