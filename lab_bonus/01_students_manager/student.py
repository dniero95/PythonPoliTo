class Student:
    all = []

    # I define the constructor
    def __init__(self, registration_number: int, name: str, surname: str, email: str, school_class: str):
        self.registration_number = registration_number
        self.name = name
        self.surname = surname
        self.email = email
        self.school_class = school_class

        Student.all.append(self)

    # Represent student obj
    def __repr__(self):
        return f'{self.registration_number}; {self.name}; {self.surname}; {self.email}; {self.school_class}'