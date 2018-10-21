from objects.building import Building
from modules.gameManager import gameManager


class SolarPanel(Building):

    def __init__(self, position):

        self.position = position
        self.size = [1, 1]
        self.connections = {'inputs': None,
                            'outputs': {'Electricity': False}}
        self.max_prod = 2
        self.cur_prod = 0

        Building.__init__(self, self.position, self.size, self.connections)

    def update(self):
        # Update production
        if gameManager.is_night:
            self.cur_prod = 0
            # do nothing
        else:
            self.cur_prod = self.max_prod
            to_deliver = self.cur_prod
            # Giving away power to non full batteries in same network
            for battery in gameManager.get_batteries():
                cur_capacity = battery.cur_capacity
                max_capacity = battery.max_capacity
                if battery.is_full():
                    # go to next battery
                    pass
                elif cur_capacity + to_deliver <= max_capacity:
                    # this one can take everything
                    battery.update_capacity(to_deliver)
                    to_deliver = 0
                else:
                    # partial delivery
                    battery.fill()
                    to_deliver = to_deliver - (max_capacity - cur_capacity)

        # TODO Update connections array
