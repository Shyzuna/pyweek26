import copy

class Network():

    def __init__(self):
        self.nodes = {}

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
        self.nodes[firstBuildingId].remove(secondBuildingId)

        if len(self.nodes[firstBuildingId]) < 1:
            self.nodes.pop(firstBuildingId)

    def splitNetworks(self):
        firstNodes = []
        secondNodes = []

        # Init
        listKeys = list(self.nodes.keys())
        if self.pathExistsRec(listKeys[0], listKeys[1]) is not None:
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
                if self.pathExistsRec(first, second) is not None:
                    if self.pathExistsRec(first, firstNodes[0]) is not None:
                        firstNodes.append(first)
                        firstNodes.append(second)
                    else:
                        secondNodes.append(first)
                        secondNodes.append(second)
                else:
                    if self.pathExistsRec(first, firstNodes[0]) is not None:
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
        return (self.pathExistsRec(firstBuilding.id, secondBuilding.id) is not None)

    def pathExistsRec(self, firstId, secondId, path=[]):
        path = path.append(firstId)
        if firstId == secondId:
            return path
        if firstId not in self.nodes:
            return None
        for node in self.nodes[firstId]:
            if path is None:
                return None
            if node not in path:
                newpath = self.pathExistsRec(node, secondId, path)
                if newpath:
                    return newpath
        return None
