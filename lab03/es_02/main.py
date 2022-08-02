if __name__ == '__main__':

    letter_grade = input('Enter a letter grade: ')

    if letter_grade[0] == 'A':
        number_grade = 4
    elif letter_grade[0] == 'B':
        number_grade = 3
    elif letter_grade[0] == 'C':
        number_grade = 2
    elif letter_grade[0] == 'D':
        number_grade = '1'
    elif letter_grade[0] == 'F':
        number_grade = 0
    else:
        print('Invalid grade!')
        exit()

    if len(letter_grade) == 2:
        pass    # TODO: gestisci caso in cui ci sia un + o un -
    else:
        print(f'The numeric value is {number_grade}')

