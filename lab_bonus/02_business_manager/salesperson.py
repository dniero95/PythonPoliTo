from person import Person

class Salesperson(Person):
    def __init__(self, *args, trade: str):
        super().__init__(*args)
        self.trade = trade

    def thirteenth_month_salary(self):
        return self.salary + self.salary * 0.91

    def __repr__(self):
        return f'Salesperson({self.name}, {self.surname}, {self.salary}, {self.trade})'