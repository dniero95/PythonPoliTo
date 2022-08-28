import csv
import os
import os
import sys
from student import Student

from sm_functions import print_menu

if __name__ == '__main__':

    # Create list of students

    Student.instantiate_from_csv('students.csv')

    print(f'{Student.students_number} studenti trovati...\n')
    print_menu() #Stampa il menù
    # Memorizza l'opzione
    while True:
        option = int(input(' >>> '))
        if option == 0:
            print('Arrivederci')
            sys.exit() # Termina il programma
        elif option == 1:
            Student.print_all_students()
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
        elif option == 6:
            os.system('clear')
            print_menu()
        else:
            print('Errore! Opzione non disponibile!')
