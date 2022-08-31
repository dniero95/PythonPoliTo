import datetime as dt
class Person:
    all = []
    def __init__(self, name:str, surname:str, gender:str, birth_date:dt.datetime, birth_place:str, fiscal_code:str ):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.birth_date = birth_date
        self.birth_place = birth_place
        self.fiscal_code = fiscal_code

        Person.all.append(self)

    @classmethod
    def instantiate_from_file(cls, path):
        with open(path, 'r') as file:
            persons = file.readlines()
            for person in persons:
                person.replace('\n', '')
                person = person.split(',')
                date = person[3].split('/')
                day = date[0]
                month = date[1]
                year = date[2]
                date =dt.datetime(int(year), int(month), int(day))
                Person(person[0], person[1], person[2], date, person[4], person[5])


    @classmethod
    def print_all_persons(cls):
        for person in Person.all:
            print(person)


    # string version of the obj
    def __str__(self):
        return f'{self.name},{self.surname},{self.gender},{self.birth_date},{self.birth_place},{self.fiscal_code}'

