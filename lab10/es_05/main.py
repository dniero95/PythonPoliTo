if __name__ == '__main__':
    reverse_alphabet = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
    alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = input('Cipher key: ')

    # rimuovo caratteri bianchi
    key = key.strip().upper()

    # Rimuovo della chiave le doppie
    for char in key:
        pos = key.find(char)
        temp = key[pos+1:]
        while temp.find(char) != -1:
            temp = temp.replace(char, '')
        key = key[:pos+1] + temp

    # Rimuovo dall'alfabeto le lettere della chiave
    for char in key:
        reverse_alphabet = reverse_alphabet.replace(char, '')

    custom_alphabet = key + reverse_alphabet

    # Faccio scegliere all'utente se vuole criptare o decriptare il testo
    while True:
        option = int(input('Select mode:\n 1 - Encrypt\n 2 - Decode\n >>> '))
        if option == 1 or option == 2:
            break
        else:
            print('Error! Available options are 1 or 2')


    file_name = input('File name: ')

    file = open(file_name, 'r')
    for char in file.read():
        if char.upper() in alphabet:
            pass
    file.close()
    # todo: finish the exercise
    # TODO: add function to code, add comment, improve efficiency