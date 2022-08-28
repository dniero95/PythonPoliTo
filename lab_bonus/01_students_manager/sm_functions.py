import re

# In this file are stored all the function of the project


# print on the console the options list
def print_menu():
    print('Scegli un opzione: ')
    print('''
     0 - esci dal programma
     1 - stampa dell'elenco degli studenti
     2 - stampa dell'elenco dei soli studenti di una certa classe (data in input)
     3 - visualizzare l'elenco degli studenti che hanno il cognome che inizia con una certa lettera data in input
     4 - raggruppare gli studenti per classe e visualizzare il risultato
     5 - creare un file di testo per stampare un elenco di studenti appartenenti a una classe data in input
     6 - pulisci lo schermo
    ''')

# This function check if a mail is in the correct format.
# The reference for the following code can be found at https://www.c-sharpcorner.com/article/how-to-validate-an-email-address-in-python/
def check_mail(email):

    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if (re.search(regex, email)):
        return True
    else:
        return True # todo: fix the check mail function

        # This function check if a class code is in the correct format
def check_class_code(class_code: str):
    class_code_numbers = [x for x in range(1, 6)]
    class_code_letters = [chr(char) for char in range(65, 91)]

    if int(class_code[0]) in class_code_numbers and class_code[1] in class_code_letters:
        return True
    else:
        return False