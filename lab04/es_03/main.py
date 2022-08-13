if __name__ == '__main__':
    try:
        number = int(input('Inserisci un numero intero: '))
        # Stampo il quadrato
        for i in range(number):
            for j in range(number):
                print('*', end='')
            print()

        print() # A capo per separare le figure

        # stampo il rettangolo
        for i in range(0, number):
                print(f'{" "*(number-i)}{"*"*i}{"*"*(i-1)}')

        for k in range(2, number):
            print(f'{" "*(k)}{"*"*(number-k)}{"*"*(len("*"*(number-k))-1)}') # todo: improve code
    except:
        print('Errore! Inserire un numero intero!')