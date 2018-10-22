from objects.building import Building


class Crusher(Building):

    def __init__(self, position, uid):

        self.position = position
        self.uid = uid
        self.size = [1, 1]
        self.connections = {'inputs': {'helium_rock': False, 'Electricity': False},
                            'outputs': {'helium_gaz': False}}
        self.max_prod = 2
        self.cur_prod = 0
        self.ratio = 1
        self.consumption = 1

        self.networks = {
            'electric': None
        }

        Building.__init__(self, self.position, self.size, self.connections, self.uid)

    def update(self):
        # TODO: drain electricity from batteries and give ore if
        # TODO: all connections' conditions are satisfied
        pass