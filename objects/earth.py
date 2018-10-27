from settings.enums import LinkStatus, Towns
from settings.townSettings import ALL_TOWN
from modules.contractManager import contractManager

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
        self._displayedTime = "00:00"
        self.changeHour()
        self._isSending = False
        self._isTransmitterOn = False

    def sendEnergy(self, transmitter, batteries):
        if self.isSending():
            towns = self.getCurrentTowns()
            toSend = int(transmitter.buildingData['transmitCapacity'][transmitter.level] / (len(towns) + 1))
            leftToSend = toSend
            for town in towns:
                for battery in batteries:
                    leftToSend = battery.sendEnergy(leftToSend)

                    if leftToSend <= 0:
                        break
                print("Envoi d'énergie ", town.value, toSend - leftToSend)
                self.towns[town]['energy'] += toSend - leftToSend
                contractManager.updateContracts(town.value, toSend - leftToSend)

    def getEnergy(self, town):
        return self.towns[town]

    def getCurrentTowns(self):
        towns = []
        for town, data in self.towns.items():
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

    def isSending(self):
        return self._isSending

    def toggleSending(self, *arg):
        self._isSending = not self._isSending

    def isTransmitterOn(self):
        return self._isTransmitterOn

    def setTransmitterOn(self, transmitterOn):
        self._isTransmitterOn = transmitterOn

        if not transmitterOn:
            self._isSending = False

    def updateDisplayedHour(self, millis):
        minutes = int(millis / 1000 * 60 / 30)
        self._displayedTime = "{:02}:{:02}".format(self.currentHour, minutes)

    def getCurrentTime(self):
        return self._displayedTime

