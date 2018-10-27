from settings.enums import LinkStatus, Towns
from settings.townSettings import ALL_TOWN

class Earth:

    def __init__(self):
        self.towns = {}

        for town in Towns:
            self.towns.update({
                town: {
                    'settings': ALL_TOWN[town],
                    'energy': 0,
                    'status': LinkStatus.OFFLINE
                }
            })
        self.currentHour = 0
        self.changeHour()

    def sendEnergy(self, town, amount):
        self.towns[town] += amount

    def getEnergy(self, town):
        return self.towns[town]

    def getCurrentTowns(self):
        towns = []
        for town, data in self.towns:
            if self.currentHour in data['settings']['hours']:
                towns.append(town)
        return towns

    def getCurrentHour(self):
        return self.currentHour

    def changeHour(self):
        self.currentHour = (self.currentHour + 1) % 23
        print("Changement d'heure ", self.currentHour)

        for town, data in self.towns.items():
            if self.currentHour in data['settings']['hours']:
                data['status'] = LinkStatus.ONLINE
            else:
                data['status'] = LinkStatus.OFFLINE
