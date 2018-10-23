from objects.building import Building


class HeadQuarters(Building):

    def __init__(self, position):

        self.position = position
        self.size = [1, 1]
        self.connections = {'inputs': {'Electricity': False},
                            'outputs': None}

        self.networks = {
            'electric': None
        }

        Building.__init__(self, self.position, self.size, self.connections)
