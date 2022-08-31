class Product:
    def __init__(self, code:str, name:str, description: str, price:float):
        self.code = code
        self.name = name
        self.description = description
        self.price = price

    def __repr__(self):
        return f'Product({self.code}, {self.name}, {self.description}, {self.price})'