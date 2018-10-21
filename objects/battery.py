from objects.building import Building


class Battery(Building):

    def __init__(self, position):

        self.position = position
        self.size = [1, 1]
        self.connections = {'inputs': {'Electricity': False},
                            'outputs': {'Electricity': False}}
        self.max_capacity = 10
        self.cur_capacity = 0

        Building.__init__(self, self.position, self.size, self.connections)

    def update_capacity(self, value):
        if self.max_capacity >= self.cur_capacity + value >= 0:
            self.cur_capacity += value

    def is_full(self):
        if self.cur_capacity == self.max_capacity:
            return True
        else:
            return False

    def is_empty(self):
        if self.cur_capacity == 0:
            return True
        else:
            return False

    def fill(self):
        self.cur_capacity = self.max_capacity

    def empty(self):
        self.cur_capacity = 0
