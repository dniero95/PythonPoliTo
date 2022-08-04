if __name__ == '__main__':
    # Prendo in input il reddito

    while True:
        income = float(input('Inserire reddito: '))
        if income < 0:
            print('Reddito non valido! Inserire un valore positivo o nullo!')
        else:
            break

    # Converto lo stato civile in un valore booleano
    marital_status = input('Inserire stato civile\n 1 - Non coniugato\n 2 - Coniugato\n >>> ')

    while True:
        if marital_status == '1':
            marital_status = False
            break
        elif marital_status == '2':
            marital_status = True
            break
        else:
            print('Stato non valido inserire nuovamente lo stato civile')
            marital_status = input('Inserire stato civile\n 1 - Non coniugato\n 2 - Coniugato\n >>> ')


    # Calcolo le tasse
    if marital_status:
        if 0 <= income <16000:
           tax = income * 0.1  # 10% del totale
        elif 16000 <= income < 64000:
            tax = 1600 + 0.15 * (income - 16000) # 1600 + il 15% della somma oltre 16000
        elif 64000 <= income:
            tax = 8800 + 0.25 * (income - 64000) # 8800 + il 25% della somma oltre 64000
    else:
        if 0 <= income <8000:
           tax = income * 0.1  # 10% del totale
        elif 8000 <= income < 32000:
            tax = 800 + 0.15 * (income - 8000)
        elif 32000 <= income:
            tax = 4400 + 0.25 * (income - 32000)


    print(f'Tasse da pagare {tax} $')