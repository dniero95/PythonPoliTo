if __name__ == '__main__':
    string = input('Enter a string: ')

    print('Uppercase character:')
    for char in string:
        if char.isupper():
            print(char)

    print('a partire dalla seconda lettera della stringa, una lettera viene visualizzata e l’altra no, alternativamente')

    for i in range(1, len(string), 2):
        print(string[i])

    print('la stringa con tutte le vocali sostituita da un carattere di sottolineatura (underscore);')

    for char in string:
        if char.isupper():
            print('_', end='')
        else:
            print(char, end='')

    print('il numero di cifre presenti nella stringa;')

    count = 0
    for char in string:
        if char.isdigit():
           count += 1

    print(f'number of digit = {count}')

    print('le posizioni di tutte le vocali presenti nella stringa.')

    for char in string:
        if char.isupper():
            print(f'{char} pos = {string.find(char)}')

    # todo: code to imporve