if __name__ == '__main__':

    telephone_number = input('Inserisci un numero di telefono: ')

    # Verifico che il numero di telefono abbia il corretto numero di cifre
    while(len(telephone_number) != 10):
        print('Devi inserire almeno 10 cifre!')
        telephone_number = input('Inserisci un altro numero di telefono: ')

    print(f'Numero di telefono formattato: ({telephone_number[:3]}) {telephone_number[3:6]}-{telephone_number[6:]}')