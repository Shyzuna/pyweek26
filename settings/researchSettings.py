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
            'cost': {ObjectCategory.CREDITS: 200},
            'time': 30,
            'element': BuildingsName.BATTERY,
            'value': 1.2,
            'param': 'stock'
        },
        {
            'name': 'Unlock Hydrogen facilities',
            'type': ResearchType.UNLOCK,
            'cost': {ObjectCategory.CREDITS: 100},
            'time': 20,
            'unlocked': [BuildingsName.HYDROGEN_PLANT, BuildingsName.DRILL_HYDROGEN, BuildingsName.WAREHOUSE_HYDROGEN],
            'resUnlocked': ObjectCategory.HYDROGEN
        },
        {
            'name': 'Hydrogen Drill Efficiency',
            'type': ResearchType.UPGRADE,
            'cost': {ObjectCategory.CREDITS: 500},
            'time': 60,
            'element': BuildingsName.DRILL_HYDROGEN,
            'value': 0.85,
            'param': 'consume'
        },
        {
            'name': 'Solar panel Efficiency',
            'type': ResearchType.UPGRADE,
            'cost': {ObjectCategory.CREDITS: 500},
            'time': 60,
            'element': BuildingsName.SOLARPANEL,
            'value': 1.2,
            'param': 'produce'
        },
        {
            'name': 'Upgrade hydrogen warehouse',
            'type': ResearchType.UPGRADE,
            'cost': {ObjectCategory.CREDITS: 300},
            'time': 45,
            'element': BuildingsName.WAREHOUSE_HYDROGEN,
            'value': 1.2,
            'param': 'stock'
        },
        {
            'name': 'Upgrade energy transmitter',
            'type': ResearchType.UPGRADE,
            'cost': {ObjectCategory.CREDITS: 1000},
            'time': 180,
            'element': BuildingsName.TRANSMITTER,
            'value': 1.2,
            'param': 'transmitCapacity'
        }
    ],
    '2': [
        {
            'name': 'Unlock Dihydrogen facilities',
            'type': ResearchType.UNLOCK,
            'cost': {ObjectCategory.CREDITS: 1000},
            'time': 90,
            'unlocked': [BuildingsName.DIHYDROGEN_PLANT, BuildingsName.DRILL_DIHYDROGEN, BuildingsName.WAREHOUSE_DIHYDROGEN, BuildingsName.HYDROGEN_COMBINER],
            'resUnlocked': ObjectCategory.DIHYDROGEN
        },
        {
            'name': 'Unlock Hydrogen combiner',
            'type': ResearchType.UNLOCK,
            'cost': {ObjectCategory.CREDITS: 2000},
            'time': 90,
            'unlocked': [BuildingsName.HYDROGEN_COMBINER],
            'resUnlocked': None
        },
        {
            'name': 'Upgrade battery',
            'type': ResearchType.UPGRADE,
            'cost': {ObjectCategory.CREDITS: 1000},
            'time': 60,
            'element': BuildingsName.BATTERY,
            'value': 1.3,
            'param': 'stock'
        },
        {
            'name': 'DiHydrogen Drill Efficiency',
            'type': ResearchType.UPGRADE,
            'cost': {ObjectCategory.CREDITS: 1500},
            'time': 60,
            'element': BuildingsName.DRILL_DIHYDROGEN,
            'value': 0.85,
            'param': 'consume'
        },
        {
            'name': 'Upgrade DiHydrogen warehouse',
            'type': ResearchType.UPGRADE,
            'cost': {ObjectCategory.CREDITS: 3000},
            'time': 60,
            'element': BuildingsName.WAREHOUSE_DIHYDROGEN,
            'value': 2,
            'param': 'stock'
        }
    ],
    '3': [
        {
            'name': 'Unlock Trihydrogen facilities',
            'type': ResearchType.UNLOCK,
            'cost': {ObjectCategory.CREDITS: 3000},
            'time': 90,
            'unlocked': [BuildingsName.TRIHYDROGEN_PLANT, BuildingsName.DRILL_TRIHYDROGEN, BuildingsName.WAREHOUSE_TRIHYDROGEN],
            'resUnlocked': ObjectCategory.TRIHYDROGEN
        },
        {
            'name': 'Unlock Dihydrogen combiner',
            'type': ResearchType.UNLOCK,
            'cost': {ObjectCategory.CREDITS: 5000},
            'time': 90,
            'unlocked': [BuildingsName.DIHYDROGEN_COMBINER],
            'resUnlocked': None
        },
        {
            'name': 'Upgrade battery',
            'type': ResearchType.UPGRADE,
            'cost': {ObjectCategory.CREDITS: 3000},
            'time': 60,
            'element': BuildingsName.BATTERY,
            'value': 1.5,
            'param': 'stock'
        },
        {
            'name': 'TriHydrogen Drill Efficiency',
            'type': ResearchType.UPGRADE,
            'cost': {ObjectCategory.CREDITS: 4000},
            'time': 60,
            'element': BuildingsName.DRILL_TRIHYDROGEN,
            'value': 0.85,
            'param': 'consume'
        },
        {
            'name': 'Upgrade TriHydrogen warehouse',
            'type': ResearchType.UPGRADE,
            'cost': {ObjectCategory.CREDITS: 6000},
            'time': 60,
            'element': BuildingsName.WAREHOUSE_TRIHYDROGEN,
            'value': 2,
            'param': 'stock'
        },
        {
            'name': 'Upgrade Hydrogen Combiner production',
            'type': ResearchType.UPGRADE,
            'cost': {ObjectCategory.CREDITS: 15000},
            'time': 60,
            'element': BuildingsName.DIHYDROGEN_COMBINER,
            'value': 2,
            'param': 'produce'
        }
    ],
    '4': [
        {
            'name': 'Unlock Trihelium facilities',
            'type': ResearchType.UNLOCK,
            'cost': {ObjectCategory.CREDITS: 10000},
            'time': 90,
            'unlocked': [BuildingsName.TRIHELIUM_PLANT, BuildingsName.WAREHOUSE_TRIHELIUM, BuildingsName.CRUSHER],
            'resUnlocked': ObjectCategory.TRIHELIUM
        },
        {
            'name': 'Upgrade battery',
            'type': ResearchType.UPGRADE,
            'cost': {ObjectCategory.CREDITS: 10000},
            'time': 60,
            'element': BuildingsName.BATTERY,
            'value': 2,
            'param': 'stock'
        },
        {
            'name': 'TriHelium Drill Efficiency',
            'type': ResearchType.UPGRADE,
            'cost': {ObjectCategory.CREDITS: 12000},
            'time': 60,
            'element': BuildingsName.CRUSHER,
            'value': 0.85,
            'param': 'consume'
        },
        {
            'name': 'Upgrade TriHelium warehouse',
            'type': ResearchType.UPGRADE,
            'cost': {ObjectCategory.CREDITS: 15000},
            'time': 60,
            'element': BuildingsName.WAREHOUSE_TRIHELIUM,
            'value': 2,
            'param': 'stock'
        },
        {
            'name': 'Upgrade DiHydrogen Combiner production',
            'type': ResearchType.UPGRADE,
            'cost': {ObjectCategory.CREDITS: 15000},
            'time': 60,
            'element': BuildingsName.DIHYDROGEN_COMBINER,
            'value': 2,
            'param': 'produce'
        },
        {
            'name': 'Upgrade energy transmitter',
            'type': ResearchType.UPGRADE,
            'cost': {ObjectCategory.CREDITS: 5000},
            'time': 180,
            'element': BuildingsName.TRANSMITTER,
            'value': 1.5,
            'param': 'transmitCapacity'
        },
    ]
}
