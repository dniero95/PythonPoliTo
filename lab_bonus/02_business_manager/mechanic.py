from person import Person

class Mechanic(Person):
    def __init__(self, *args, trade: str):
        super().__init__(*args)
        self.trade = trade

    def thirteenth_month_salary(self):
        return self.salary + self.salary * 0.93

    def __repr__(self):
        return f'Mechanic({self.name}, {self.surname}, {self.salary}, {self.trade})'