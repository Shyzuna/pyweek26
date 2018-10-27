import copy
from settings.enums import ObjectCategory, BuildingStates

class Network():

    def __init__(self):
        self.nodes = {}

        self.update()

    def addConnections(self, firstBuilding, secondBuilding):
        firstBuildingId = firstBuilding.id
        secondBuildingId = secondBuilding.id
        if firstBuildingId in self.nodes:
            self.nodes[firstBuildingId].append(secondBuildingId)
        else:
            self.nodes[firstBuildingId] = [secondBuildingId]

        if secondBuildingId in self.nodes:
            self.nodes[secondBuildingId].append(firstBuildingId)
        else:
            self.nodes[secondBuildingId] = [firstBuildingId]

    def mergeConnections(self, otherNetwork):
        for parentNode, childrenNode in otherNetwork.nodes.items():
            if parentNode in self.nodes.keys():
                self.nodes[parentNode].extend(copy.deepcopy(childrenNode))
            else:
                self.nodes.update({parentNode: copy.deepcopy(childrenNode)})

    def removeConnections(self, firstBuilding, secondBuilding):
        firstBuildingId = firstBuilding.id
        secondBuildingId = secondBuilding.id

        if secondBuildingId in self.nodes:
            self.nodes.pop(secondBuildingId)
        if secondBuildingId in self.nodes[firstBuildingId]:
            self.nodes[firstBuildingId].remove(secondBuildingId)

        if len(self.nodes[firstBuildingId]) < 1:
            self.nodes.pop(firstBuildingId)

    def splitNetworks(self):
        firstNodes = []
        secondNodes = []

        # Init
        listKeys = list(self.nodes.keys())

        if len(listKeys) < 2:
            return None

        if self.pathExistsRec(listKeys[0], listKeys[1], []) is not None:
            firstNodes.append(listKeys[0])
            firstNodes.append(listKeys[1])
        else:
            firstNodes.append(listKeys[0])
            secondNodes.append(listKeys[1])

        # Node repartition
        for i in range(2, len(listKeys) - 1):
            first = listKeys[i]
            for j in range(i + 1, len(listKeys)):
                second = listKeys[j]
                if self.pathExistsRec(first, second, []) is not None:
                    if self.pathExistsRec(first, firstNodes[0], []) is not None:
                        firstNodes.append(first)
                        firstNodes.append(second)
                    else:
                        secondNodes.append(first)
                        secondNodes.append(second)
                else:
                    if self.pathExistsRec(first, firstNodes[0], []) is not None:
                        firstNodes.append(first)
                        secondNodes.append(second)
                    else:
                        secondNodes.append(first)
                        firstNodes.append(second)

        # New graph computing
        firstNewNetwork = self.createNewNetwork(firstNodes, secondNodes)
        secondNewNetwork = self.createNewNetwork(secondNodes, firstNodes)

        # Replace current nodes
        self.nodes = firstNewNetwork

        return secondNewNetwork

    def createNewNetwork(self, newNodes, otherNodes):
        newNetwork = {}
        for node in newNodes:
            newNetwork[node] = copy.deepcopy(self.nodes[node])
            for otherNode in otherNodes:
                if otherNode in newNetwork[node]:
                    newNetwork[node].remove(otherNode)
        return newNetwork



    def pathExists(self, firstBuilding, secondBuilding):
        return (self.pathExistsRec(firstBuilding.id, secondBuilding.id, []) is not None)

    def pathExistsRec(self, firstId, secondId, path):
        path.append(firstId)
        if firstId == secondId:
            return path
        if firstId not in self.nodes:
            return None
        for node in self.nodes[firstId]:
            if node not in path:
                newpath = self.pathExistsRec(node, secondId, path)
                if newpath:
                    return newpath
        return None

    def update(self):
        self.instantProduction = {
            ObjectCategory.ENERGY: 0,
            ObjectCategory.HYDROGEN: 0,
            ObjectCategory.DIHYDROGEN: 0,
            ObjectCategory.TRIHYDROGEN: 0,
            ObjectCategory.TRIHELIUM: 0
        }
        self.instantStock = {
            ObjectCategory.ENERGY: 0,
            ObjectCategory.HYDROGEN: 0,
            ObjectCategory.DIHYDROGEN: 0,
            ObjectCategory.TRIHYDROGEN: 0,
            ObjectCategory.TRIHELIUM: 0
        }
        self.consumedStock = {
            ObjectCategory.ENERGY: 0,
            ObjectCategory.HYDROGEN: 0,
            ObjectCategory.DIHYDROGEN: 0,
            ObjectCategory.TRIHYDROGEN: 0,
            ObjectCategory.TRIHELIUM: 0
        }

    def produceResources(self, num, type):
        self.instantProduction[type] += num

    def produceStock(self, num, type):
        self.instantStock[type] += num

    def consumeResources(self, num, type, resource=None):
        state = BuildingStates.ON

        # Resource
        if resource is not None:
            if resource.isEmpty():
                state = BuildingStates.OFF
            elif num <= resource.getAmount():
                newResourceAmount = resource.getAmount() - num
            else:
                newResourceAmount = 0
                num = newResourceAmount

        # Production
        newInstantProduction = self.instantProduction[type]
        newConsumedStock = self.consumedStock[type]
        newInstantStock = self.instantStock[type]

        if state == BuildingStates.ON:
            if num <= self.instantProduction[type]:
                newInstantProduction = self.instantProduction[type] - num
            else:
                leftToConsume = num - self.instantProduction[type]
                if self.consumedStock[type] + leftToConsume <= self.instantStock[type]:
                    newConsumedStock = self.consumedStock[type] + leftToConsume
                    newInstantProduction = 0
                else:
                    state = BuildingStates.OFF

        if resource is not None:
            if state == BuildingStates.ON:
                resource.setAmount(newResourceAmount)
                self.instantProduction[type] = newInstantProduction
                self.consumedStock[type] = newConsumedStock
                self.instantStock[type] = newInstantStock
        else:
            self.instantProduction[type] = newInstantProduction
            self.consumedStock[type] = newConsumedStock
            self.instantStock[type] = newInstantStock

        return state

    def fillStock(self, warehouse, type):
        max_capacity = warehouse.buildingData['stock'][type][warehouse.level]
        print("stock", type)
        if self.instantProduction[type] > 0 and not warehouse.is_full():
            if warehouse.cur_capacity[type] + self.instantProduction[type] > max_capacity:
                toFill = max_capacity - warehouse.cur_capacity[type]
                warehouse.cur_capacity[type] += toFill
                self.instantProduction[type] -= toFill
                print("Recharge batterie", toFill)
            else:
                warehouse.cur_capacity[type] += self.instantProduction[type]
                print("Recharge batterie", self.instantProduction[type])
                self.instantProduction[type] = 0
        elif not warehouse.is_empty():
            if warehouse.cur_capacity[type] - self.consumedStock[type] > 0:
                warehouse.cur_capacity[type] -= self.consumedStock[type]
                print("Decharge batterie 1", self.consumedStock[type])
            else:
                self.consumedStock[type] -= warehouse.cur_capacity[type]
                print("Decharge batterie 2", warehouse.cur_capacity[type])
                warehouse.cur_capacity[type] = 0

