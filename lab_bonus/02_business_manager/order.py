import datetime
from salesperson import Salesperson

class Order:
    all = [] #store all orders
    def __init__(self, order_id:int, date:datetime, salesperson: Salesperson, products_list = []):
        self.order_id = order_id
        self.date = date
        self.products_list = products_list
        self.salesperson = salesperson

        Order.all.append(self)

    def no_products(self):
        return len(self.products_list)

    def total(self):
        tot = 0
        for product in self.products_list:
            tot += product.price
        return tot

    # todo finish methods
    def receipt(self):
        pass

    def __repr__(self):
        return f'Order()'

