from salesperson import Salesperson

class SalespersonTeamLeader(Salesperson):
    def __init__(self, *args, salespersons = []):
        super().__init__(args)
        self.salespersons = salespersons

    def add_salesperson(self, salesperson:Salesperson):
        self.salespersons.append(salesperson)

    def return_salesperson(self, index: int):
        return self.salespersons[index]

    def delete_salesperson(self, index: int):
        del self.salespersons[index]

    def thirteenth_month_salary(self):
        return self.salary * 2