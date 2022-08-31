from mechanic import Mechanic

class MechanicChief(Mechanic):
    def __init__(self, *args, orders = []):
        super().__init__(args)
        self.orders = orders
