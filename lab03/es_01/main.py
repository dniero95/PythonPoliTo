if __name__ == '__main__':

    first_number = int(input('Inserisci il primo numero: '))
    second_number = int(input('Inserisci il secondo numero: '))
    third_number = int(input('Inserisci il terzo numero: '))

    if first_number < second_number and second_number < third_number:
        print('Increasing')
    elif first_number > second_number and second_number > third_number:
        print('decreasing')
    else:
        print('neither')