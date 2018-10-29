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
        'cost': {ObjectCategory.CREDITS: [100, 150, 225, 350]},
        'produce': {},
        'consume': {},
        'stock': {ObjectCategory.ENERGY: [50, 130, 300, 500]},
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
        'cost': {ObjectCategory.CREDITS: [125, 180, 270, 400]},
        'produce': {ObjectCategory.HYDROGEN: [1, 2, 4, 8]},
        'consume': {ObjectCategory.ENERGY: [5, 10, 25, 50]},
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
        'cost': {ObjectCategory.CREDITS: [300, 450, 575, 800]},
        'produce': {ObjectCategory.DIHYDROGEN: [1, 2, 4, 8]},
        'consume': {ObjectCategory.ENERGY: [24, 48, 96, 192]},
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
        'cost': {ObjectCategory.CREDITS: [800, 1200, 2000, 3000]},
        'produce': {ObjectCategory.TRIHYDROGEN: [1, 2, 4, 8]},
        'consume': {ObjectCategory.ENERGY: [80, 120, 200, 300]},
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
        'cost': {ObjectCategory.CREDITS: [2000, 3000, 4500, 6000]},
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
        'cost': {ObjectCategory.CREDITS: [100, 150, 200, 300]},
        'produce': {ObjectCategory.ENERGY: [5, 8, 11, 15]},
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
        'cost': {ObjectCategory.CREDITS: [100, 3000, 5000, 12000]},
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
        'cost': {ObjectCategory.CREDITS: [125, 180, 270, 400]},
        'produce': {},
        'consume': {},
        'stock': {ObjectCategory.HYDROGEN: [50, 130, 300, 500]},
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
        'cost': {ObjectCategory.CREDITS: [150, 225, 350, 500]},
        'produce': {ObjectCategory.ENERGY: [12, 28, 64, 144]},
        'consume': {ObjectCategory.HYDROGEN: [2, 4, 8, 16]},
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
        'cost': {ObjectCategory.CREDITS: [400, 600, 900, 1300]},
        'produce': {ObjectCategory.ENERGY: [40, 100, 240, 560]},
        'consume': {ObjectCategory.DIHYDROGEN: [2, 4, 8, 16]},
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
    BuildingsName.TRIHYDROGEN_PLANT: {
        'name': BuildingsName.TRIHYDROGEN_PLANT.value,
        'desc': 'Produce energy with trihydrogen.',
        'cost': {ObjectCategory.CREDITS: [1000, 1500, 2250, 3000]},
        'produce': {ObjectCategory.ENERGY: [100, 240, 560, 1600]},
        'consume': {ObjectCategory.TRIHYDROGEN: [2, 4, 8, 16]},
        'stock': {},
        'allowedSpot': None,
        'deletable': True,
        'constructable': True,
        'canLevelUp': True,
        'constructionTime': 0,
        'size': (1, 1),
        'uiImg': pygame.transform.scale(
            pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'TRIHYDROGEN_PLANT.png')),
            (64, 64)),
        'animImg': [
            pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'TRIHYDROGEN_PLANT.png'))
        ]
    },
    BuildingsName.TRIHELIUM_PLANT: {
        'name': BuildingsName.TRIHELIUM_PLANT.value,
        'desc': 'Produce energy with trihelium.',
        'cost': {ObjectCategory.CREDITS: [2500, 3750, 5000, 7500]},
        'produce': {ObjectCategory.ENERGY: [500, 1200, 3000, 8000]},
        'consume': {ObjectCategory.TRIHELIUM: [2, 4, 8, 16]},
        'stock': {},
        'allowedSpot': None,
        'deletable': True,
        'constructable': True,
        'canLevelUp': True,
        'constructionTime': 0,
        'size': (1, 1),
        'uiImg': pygame.transform.scale(
            pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'TRIHELIUM_PLANT.png')),
            (64, 64)),
        'animImg': [
            pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'TRIHELIUM_PLANT.png'))
        ]
    },
    BuildingsName.CONNECTOR: {
        'name': BuildingsName.CONNECTOR.value,
        'desc': 'Building connector.',
        'cost': {ObjectCategory.CREDITS: [25, 0, 0, 0]},
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
        'cost': {ObjectCategory.CREDITS: [10, 1000, 8000, 20000]},
        'produce': {},
        'consume': {ObjectCategory.ENERGY: [50, 300, 5000, 30000]},
        'stock': {},
        'allowedSpot': None,
        'deletable': False,
        'constructable': True,
        'canLevelUp': True,
        'constructionTime': 0,
        'transmitCapacity': {ObjectCategory.ENERGY: [25, 150, 2500, 25000]},
        'size': (1, 1),
        'uiImg': pygame.transform.scale(pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'TRANSMITTER.png')),
                                        (64, 64)),
        'animImg': [
            pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'TRANSMITTER.png'))
        ]
    },
    BuildingsName.HYDROGEN_COMBINER: {
        'name': BuildingsName.HYDROGEN_COMBINER.value,
        'desc': 'Use Hydrogen to create Dihydrogen',
        'cost': {ObjectCategory.CREDITS: [300, 450, 700, 1000]},
        'produce': {ObjectCategory.DIHYDROGEN: [1, 4, 8, 15]},
        'consume': {ObjectCategory.ENERGY: [30, 50, 100, 180], ObjectCategory.HYDROGEN: [2, 4, 6, 10]},
        'stock': {},
        'allowedSpot': None,
        'deletable': True,
        'constructable': True,
        'canLevelUp': True,
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
        'desc': 'Use Dihydrogen to create Trihydrogen.',
        'cost': {ObjectCategory.CREDITS: [800, 1200, 1800, 2600]},
        'produce': {ObjectCategory.TRIHYDROGEN: [1, 4, 8, 15]},
        'consume': {ObjectCategory.ENERGY: [80, 150, 225, 300], ObjectCategory.DIHYDROGEN: [2, 4, 6, 10]},
        'stock': {},
        'allowedSpot': None,
        'deletable': True,
        'constructable': True,
        'canLevelUp': True,
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
        'cost': {ObjectCategory.CREDITS: [200, 300, 450, 650]},
        'produce': {},
        'consume': {},
        'stock': {ObjectCategory.DIHYDROGEN: [50, 130, 300, 500]},
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
        'cost': {ObjectCategory.CREDITS: [500, 750, 1250, 2000]},
        'produce': {},
        'consume': {},
        'stock': {ObjectCategory.TRIHYDROGEN: [50, 130, 300, 500]},
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
        'cost': {ObjectCategory.CREDITS: [800, 1200, 2000, 3000]},
        'produce': {},
        'consume': {},
        'stock': {ObjectCategory.TRIHELIUM: [50, 130, 300, 500]},
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
