import csv
import sys
from student import Student

from sm_functions import print_menu

if __name__ == '__main__':

    # Create list of students
    with open('students.csv', 'r') as file:
        students = file.readlines()
        for student in students:
            Student(student[0], student[1], student[2], student[3], student[4])
    print_menu() #Stampa il menù
    # Memorizza l'opzione
    while True:
        option = int(input(' >>> '))
        if option == 0:
            print('Arrivederci')
            sys.exit() # Termina il programma
        elif option == 1:
            for student in Student.all:
                print(student)
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            pass
