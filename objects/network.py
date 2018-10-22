import copy

from objects.Building import Building


class Network(Building):

    def __init__(self, nodes={}):
        self.nodes = nodes

    def addConnections(self, firstBuilding, secondBuilding, networkType):
        id = firstBuilding.id
        if id in self.nodes:
            self.nodes[id].append(secondBuilding.id)
        else:
            self.nodes[id] = [secondBuilding.id]

        id = secondBuilding.id
        if id in self.nodes:
            self.nodes[id].append(firstBuilding.id)
        else:
            self.nodes[id] = [firstBuilding.id]

    def removeConnections(self, firstBuilding, secondBuilding):
        firstBuildingId = firstBuilding.id
        secondBuildingId = secondBuilding.id
        self.nodes.pop(secondBuildingId, None)
        self.nodes[firstBuildingId].remove(secondBuildingId)

    def splitNetworks(self):
        firstNodes = []
        secondNodes = []

        # Init
        if self.pathExistsRec(self.nodes[0], self.nodes[1]) is not None:
            firstNodes.append(self.nodes[0])
            firstNodes.append(self.nodes[1])
        else:
            firstNodes.append(self.nodes[0])
            secondNodes.append(self.nodes[1])

        # Node repartition
        for i in range(2, len(self.nodes.keys()) - 1):
            first = self.nodes[i]
            for j in range(i + 1, len(self.nodes.keys())):
                second = self.nodes[j]
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
                    newNetwork.remove(otherNode)
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
            if node not in path:
                newpath = self.pathExistsRec(node, secondId, path)
                if newpath:
                    return newpath
        return None
