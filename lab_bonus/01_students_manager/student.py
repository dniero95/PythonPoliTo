import csv


class Student:
    # Store all students and how many there are here
    all = []
    students_number = 0
    # I define the constructor
    def __init__(self, registration_number: int, name: str, surname: str, email: str, school_class: str):
        assert 9999 < registration_number < 100000, f'Registration Number: {registration_number} must be of five digits'

        assert len(name) > 2, f'Name: {name} must be at least of two character.'
        assert len(surname) > 2, f'Name: {surname} must be at least of two character.'
        assert check_mail(email), f'e-mail: {email} is not in the correct format.'
        assert check_class_code(school_class), f'Class Code: {school_class} is not in the correct format.'


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
    @staticmethod
    def filter_students_by_surname(surname):
        digits = len(surname) # number of digits to compare
        for student in Student.all:
            if student.surname[0:digits] == surname:
                print(student)

    @staticmethod
    def sort_students_by_class():
        Student.all.sort(key=lambda student: student.school_class)
        for student in Student.all:
            print(student)


    @staticmethod
    def create_students_file(file_name: str, class_number: str):
        with open(file_name, 'w') as file:
            file.writelines(
                str([student for student in Student.all if student.school_class[0:len(class_number)] == class_number]).replace(',', '\n')[1:-2])

    # Represent student obj
    def __repr__(self):
        return f'{self.registration_number}; {self.name}; {self.surname}; {self.email}; {self.school_class}'