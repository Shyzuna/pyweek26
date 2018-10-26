from settings.enums import Colors, Towns

class Earth:

    def __init__(self):
        self.towns = {
            Towns.SYDNEY: {
                'hours': [0, 1, 2],
                'energy': 0
            },
            Towns.MOSCOW: {
                'hours': [3, 4, 5],
                'energy': 0
            },
            Towns.NEW_YORK: {
                'hours': [6, 7, 8],
                'energy': 0
            },
            Towns.SHANGAI: {
                'hours': [9, 10, 11],
                'energy': 0
            },
            Towns.PARIS: {
                'hours': [12, 13, 14],
                'energy': 0
            }
        }

        self.currentHour = 0

    def sendEnergy(self, town, amount):
        self.towns[town] += amount

    def getEnergy(self, town):
        return self.towns[town]

    def getCurrentTowns(self):
        towns = []
        for town, data in self.towns:
            if self.currentHour in data['hours']:
                towns.append(town)
        return towns

    def getCurrentHour(self):
        return self.currentHour

    def changeHour(self):
        self.currentHour = (self.currentHour + 1) % 23
        print("Changement d'heure ", self.currentHour)



