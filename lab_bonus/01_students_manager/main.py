import csv
import sys

from sm_functions import print_menu

if __name__ == '__main__':
    print_menu() #Stampa il menù
    # Memorizza l'opzione
    while True:
        option = int(input(' >>> '))
        if option == 0:
            print('Arrivederci')
            sys.exit() # Termina il programma
        elif option == 1:
            with open('students.csv', 'r') as file:
                reader = csv.DictReader(file)
                students = list(reader)
                for student in students:
                    print((student))
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            pass
