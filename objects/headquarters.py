from objects.building import Building


class HeadQuarters(Building):

    def __init__(self, position, uid):

        self.position = position
        self.uid = uid
        self.size = [1, 1]
        self.connections = {'inputs': {'Electricity': False},
                            'outputs': None}

        Building.__init__(self, self.position, self.size, self.connections, self.uid)
