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
            'name': 'Unlock Hydrogen facilities',
            'type': ResearchType.UNLOCK,
            'cost': {ObjectCategory.CREDITS: 100},
            'time': 10,
            'unlocked': [BuildingsName.HYDROGEN_PLANT, BuildingsName.DRILL_HYDROGEN, BuildingsName.WAREHOUSE_HYDROGEN],
            'resUnlocked': ObjectCategory.HYDROGEN
        }
    ],
    '2': [
        {
            'name': 'Unlock Dihydrogen facilities',
            'type': ResearchType.UNLOCK,
            'cost': {ObjectCategory.CREDITS: 100},
            'time': 10,
            'unlocked': [BuildingsName.DIHYDROGEN_PLANT, BuildingsName.DRILL_DIHYDROGEN, BuildingsName.WAREHOUSE_DIHYDROGEN, BuildingsName.HYDROGEN_COMBINER],
            'resUnlocked': ObjectCategory.DIHYDROGEN
        }
    ],
    '3': [
        {
            'name': 'Unlock Trihydrogen facilities',
            'type': ResearchType.UNLOCK,
            'cost': {ObjectCategory.CREDITS: 100},
            'time': 10,
            'unlocked': [BuildingsName.TRIHYDROGEN_PLANT, BuildingsName.DRILL_TRIHYDROGEN, BuildingsName.WAREHOUSE_TRIHYDROGEN, BuildingsName.DIHYDROGEN_COMBINER],
            'resUnlocked': ObjectCategory.TRIHYDROGEN
        }
    ],
    '4': [
        {
            'name': 'Unlock Trihelium facilities',
            'type': ResearchType.UNLOCK,
            'cost': {ObjectCategory.CREDITS: 100},
            'time': 100,
            'unlocked': [BuildingsName.TRIHELIUM_PLANT, BuildingsName.WAREHOUSE_TRIHELIUM, BuildingsName.CRUSHER],
            'resUnlocked': ObjectCategory.TRIHELIUM
        }
    ]
}