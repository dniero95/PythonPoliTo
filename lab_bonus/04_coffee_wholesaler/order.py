class Coffe_order:
    all = []
    SACK_PRICE = 6.00
    BIG_BOX_SIZE = 20
    BIG_BOX_PRICE = 2.00
    MEDIUM_BOX_SIZE = 10
    MEDIUM_BOX_PRICE = 1.5
    SMALL_BOX_SIZE = 5
    SMALL_BOX_PRICE = 0.5
    def __init__(self, number_of_sacks:int):

        assert number_of_sacks > 0, f'Error! you need to order at lest one sack of coffee'
        self.number_of_sacks = number_of_sacks
        self.coffee_total_price = number_of_sacks * number_of_sacks
        self.number_big_box = number_of_sacks // self.BIG_BOX_SIZE
        self.big_box_total_price = self.number_big_box * self.BIG_BOX_PRICE
        number_of_sacks %= self.BIG_BOX_SIZE
        self.number_medium_box = number_of_sacks // self.MEDIUM_BOX_SIZE
        self.medium_box_total_price = self.number_medium_box * self.MEDIUM_BOX_PRICE
        number_of_sacks %= self.MEDIUM_BOX_SIZE
        self.number_small_box = number_of_sacks // self.SMALL_BOX_SIZE
        if number_of_sacks % self.SMALL_BOX_SIZE != 0:
            self.number_small_box += 1
        self.small_box_total_price = self.number_small_box * self.SMALL_BOX_PRICE
        Coffe_order.all.append(self)

    def calc_total_coffee_price(self):
        return self.coffee_total_price
    def calc_number_of_box(self):
        return f'Scatole grandi: {self.number_big_box}\nScatole medie: {self.number_medium_box}\nScatole piccole: {self.number_small_box}'
    def calc_total_order_price(self):
        return self.calc_total_coffee_price() +self.big_box_total_price + self.medium_box_total_price + self.small_box_total_price

    # todo:to improve