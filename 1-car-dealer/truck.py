from vehicle import Vehicle


class Truck(Vehicle):
    def __init__(self):
        super().__init__()
        self.carry_limit = 1000

        self.current_carriage_weight = None

    def attach_carriage(self, carriage):
        if carriage <= self.carry_limit:
            self.current_carriage_weight = carriage
            return True
        return False


    def detach_carriage(self):

        self.current_carriage_weight = None

    def has_carriage(self):
        if self.current_carriage_weight != None:
            return True
        return False
