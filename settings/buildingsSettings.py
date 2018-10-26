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
        'stock': {ObjectCategory.ENERGY: 50},
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
        'produce': {ObjectCategory.HYDROGEN: 2},
        'consume': {ObjectCategory.ENERGY: 5},
        'stock': {},
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
        'stock': {},
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
        'stock': {},
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
        'stock': {},
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
    BuildingsName.WAREHOUSE_HYDROGEN: {
        'name': BuildingsName.WAREHOUSE_HYDROGEN.value,
        'desc': 'Contains hydrogen.',
        'cost': {ObjectCategory.CREDITS: 150},
        'produce': {},
        'consume': {},
        'stock': {ObjectCategory.HYDROGEN: 50},
        'allowedSpot': None,
        'deletable': True,
        'constructable': True,
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
        'cost': {ObjectCategory.CREDITS: 200},
        'produce': {ObjectCategory.ENERGY: 15},
        'consume': {ObjectCategory.HYDROGEN: 20},
        'stock': {},
        'allowedSpot': None,
        'deletable': True,
        'constructable': True,
        'constructionTime': 0,
        'size': (1, 1),
        'uiImg': pygame.transform.scale(pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'HYDROGEN_PLANT.png')),
                                        (64, 64)),
        'animImg': [
            pygame.image.load(os.path.join(settings.BUILDINGS_PATH, 'HYDROGEN_PLANT.png'))
        ]
    }
}