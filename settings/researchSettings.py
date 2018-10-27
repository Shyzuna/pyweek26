"""
Title: researchSettings File
Desc: All research settings
Creation Date: 26/10/17
LastMod Date: 26/10/17
TODO:
*
"""

from settings.enums import ObjectCategory, ResearchType, BuildingsName


ALL_RESEARCH = {
    '1': [
        {
            'name': 'Upgrade battery',
            'type': ResearchType.UPGRADE,
            'cost': {ObjectCategory.CREDITS: 100},
            'time': 10,
            'element': BuildingsName.BATTERY,
            'value': 1.2,
            'param': 'stock'
        },
        {
            'name': 'Unlock Hydrogen stuff',
            'type': ResearchType.UNLOCK,
            'cost': {ObjectCategory.CREDITS: 100},
            'time': 10,
            'unlocked': [BuildingsName.HYDROGEN_PLANT, BuildingsName.DRILL_HYDROGEN, BuildingsName.WAREHOUSE_HYDROGEN],
            'resUnlocked': ObjectCategory.HYDROGEN
        },
        {
            'name': 'Upgrade battery',
            'type': ResearchType.UPGRADE,
            'cost': {ObjectCategory.CREDITS: 100},
            'time': 10,
            'element': BuildingsName.BATTERY,
            'value': 1.2,
            'param': 'stock'
        },
        {
            'name': 'Upgrade battery',
            'type': ResearchType.UPGRADE,
            'cost': {ObjectCategory.CREDITS: 100},
            'time': 10,
            'element': BuildingsName.BATTERY,
            'value': 1.2,
            'param': 'stock'
        }
    ],
    '2': [
        {
            'name': 'Upgrade battery',
            'type': ResearchType.UPGRADE,
            'cost': {ObjectCategory.CREDITS: 100},
            'time': 10,
            'element': BuildingsName.BATTERY,
            'value': 1.2
        },
        {
            'name': 'Unlock Dihydrogen stuff',
            'type': ResearchType.UNLOCK,
            'cost': {ObjectCategory.CREDITS: 100},
            'time': 10,
            'unlocked': [BuildingsName.DIHYDROGEN_PLANT, BuildingsName.DRILL_HYDROGEN, BuildingsName.WAREHOUSE_DIHYDROGEN],
            'resUnlocked': ObjectCategory.HYDROGEN
        }
    ],
    '3': [
        {
            'name': 'Upgrade battery',
            'type': ResearchType.UPGRADE,
            'cost': {ObjectCategory.CREDITS: 100},
            'time': 100,
            'element': BuildingsName.BATTERY,
            'value': 1.2
        }
    ],
    '4': [
        {
            'name': 'Upgrade battery',
            'type': ResearchType.UPGRADE,
            'cost': {ObjectCategory.CREDITS: 100},
            'time': 100,
            'element': BuildingsName.BATTERY,
            'value': 1.2
        }
    ]
}