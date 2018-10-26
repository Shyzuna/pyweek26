"""
Title: mapGenerator File
Desc: Procedural generation of a map (ressources)
Creation Date:  21/10/18
LastMod Date: 25/10/18
TODO:
    - Make a better distribution fct
    - Remove hq init pos from spawn
"""

import numpy

from objects.resource import Resource
from settings import settings

class MapGenerator(object):

    def __init__(self):
        if settings.SEED is not None:
            self._seed = settings.SEED
        else:
            self._seed = self.generateSeed()

    def generateSeed(self):
        return int(numpy.power(10, settings.SEED_POWER) * numpy.random.rand(1))

    def setSeed(self, seed):
        self._seed = seed

    def getRandomDelta(self, number, delta):
        d1 = numpy.ceil(number * delta)
        spotMin = 1 if number - d1 <= 0 else number - 1
        return numpy.random.randint(spotMin, number + d1 + 1)

    def generateMap(self, size, resources, spots, repartition, totalRes, delta):
        totalSize = size[0] * size[1]
        cases = list(range(0, totalSize))
        numpy.random.seed(self._seed)
        resList = []
        for i, res in enumerate(resources):
            # compute spot number
            spotNumber = self.getRandomDelta(totalSize * spots[i], delta)
            amountBySpot = self.getRandomDelta(totalRes * repartition[i], delta) / spotNumber  # uniform distribution
            print(amountBySpot)
            for j in range(0, spotNumber):
                position = numpy.random.choice(cases, 1)
                cases.remove(position)
                resList.append(Resource((int(position/size[1]) + settings.BORDER_TILES_NUM,
                                         int(position % size[1]) + settings.BORDER_TILES_NUM),
                                        (1, 1), res, amountBySpot))
        return resList


    def generateSettingsMap(self):
        return self.generateMap((settings.TILES_NUM_WIDTH, settings.TILES_NUM_HEIGHT),
                                settings.RESOURCES, settings.SPOT_NUMBERS, settings.REPARTITION_NUMBERS,
                                settings.TOTAL_RES, settings.DELTA_PERCENT)
