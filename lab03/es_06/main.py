if __name__ == '__main__':
    # Prendo in input il voto controllando che sia tra 0 e 4
    while True:
        grade = float(input('Voto numerico = '))
        if not (0 <= grade <= 4):
            print('Il voto deve essere compreso tra 0 e 4!\nInserisci un nuovo voto')
        else:
            break

    if grade < 0.7:
        alphabetic_grade = 'F'
    elif 0.7 <= grade < 0.85:
        alphabetic_grade = 'E-'
    elif 0.85 <= grade < 1.15:
        alphabetic_grade = 'E'
    elif 1.15 <= grade < 1.7:
        alphabetic_grade = 'E+'
    elif 1.7 <= grade < 1.85:
        alphabetic_grade = 'D-'
    elif 1.85 <= grade < 2.15:
        alphabetic_grade = 'D'
    elif 2.15<= grade < 2.7:
        alphabetic_grade = 'D+'
    elif 2.7 <= grade < 2.85:
        alphabetic_grade = 'B-'
    elif 2.85 <= grade < 3.15:
        alphabetic_grade = 'B'
    elif 3.15 <= grade < 3.7:
        alphabetic_grade = 'B+'
    elif 3.7 <= grade < 3.85:
        alphabetic_grade = 'A-'
    else:
        alphabetic_grade = 'A'


    print(f'Voto alfabetico = {alphabetic_grade}')