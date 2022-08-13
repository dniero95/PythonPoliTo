if __name__ == '__main__':
    word = input('Inserire una parola: ')

    print('Parola al contrario: ', end='')
    for count, char in enumerate(word):
        print(word[len(word)-1-count], end='')


    print('\nLettere maiuscole partendo dal fondo: ', end='')
    for char in word:
        if char.isupper():
            print(char, end='')


