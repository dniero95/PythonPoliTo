import csv
import sys
from student import Student

from sm_functions import print_menu

if __name__ == '__main__':

    # Create list of students
    with open('students.csv', 'r') as file:
        students = file.readlines()
        students.remove(students[0])
        for student in students:
            student = student.replace('\n', '')
            student = student.split((';'))
            Student(student[0], student[1], student[2], student[3], student[4])

        print(f'{Student.students_number} studenti trovati')
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
            class_code = input('Classe: ')
            for student in Student.all:
                if student.school_class == class_code:
                    print(student)
        elif option == 3:
            first_char_surname = input('Prima Lettera Cognome: ')
            for student in Student.all:
                if student.surname[0] == first_char_surname:
                    print(student)
        elif option == 4:
            Student.all.sort(key=lambda student: student.school_class)
            for student in Student.all:
                print(student)
        elif option == 5:
            with open('studenti-quarta.txt', 'w') as file:
                file.writelines(str([student for student in Student.all if int(student.school_class[0]) == 4]).replace(',', '\n')[1:-2])
