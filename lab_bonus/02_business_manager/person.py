import abc
from abc import ABC, abstractmethod

class Person(ABC):

    all = []
    @abstractmethod
    def __init__(self, name:str, surname:str, salary:float):
        assert len(name) > 1, f'name: {name} must have at least two character'
        assert len(surname) > 1, f'surname: {surname} must have at least two character'
        assert salary > 0, f'salary must be strictly positive'

        self.name = name
        self.surname = surname
        self.salary = salary

        Person.all.append(self)

    @abstractmethod
    def thirteenth_month_salary(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass