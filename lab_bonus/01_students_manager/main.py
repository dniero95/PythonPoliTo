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
            Student.filter_students_by_class(class_code)
        elif option == 3:
            first_char_surname = input('Cognome: ')
            Student.filter_students_by_surname(first_char_surname)
        elif option == 4:
            Student.sort_students_by_class()
        elif option == 5:
            with open('studenti-quarta.txt', 'w') as file:
                file.writelines(str([student for student in Student.all if int(student.school_class[0]) == 4]).replace(',', '\n')[1:-2])
        elif option == 6:
            os.system('clear')
            print_menu()
        else:
            print('Errore! Opzione non disponibile!')
