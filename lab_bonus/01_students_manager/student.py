import csv


class Student:
    # Store all students and how many there are here
    all = []
    students_number = 0
    # I define the constructor
    def __init__(self, registration_number: int, name: str, surname: str, email: str, school_class: str):
        self.registration_number = registration_number
        self.name = name
        self.surname = surname
        self.email = email
        self.school_class = school_class

        Student.all.append(self)
        Student.students_number += 1


    # Instantiete students from csv file

    @classmethod
    def instantiate_from_csv(cls, path: str):
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            students = list(reader)

            for student in students:
                Student(
                    registration_number=int(student.get('registration_number')),
                    name=student.get('name'),
                    surname=student.get('surname'),
                    email=student.get('email'),
                    school_class=student.get('school_class')
                )

    # Print all the students created
    @staticmethod
    def print_all_students():
        for student in Student.all:
            print(student)

    @staticmethod
    def filter_students_by_class(class_code):
        for student in Student.all:
            if student.school_class == class_code:
                print(student)
    # Represent student obj
    def __repr__(self):
        return f'{self.registration_number}; {self.name}; {self.surname}; {self.email}; {self.school_class}'