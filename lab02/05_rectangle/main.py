from math import sqrt

if __name__ == '__main__':
    print('Rettangolo')
    base = float(input('Inserire la base: '))
    heigh = float(input('Inserire l\'altezza: '))

    print(f'Area = {base * heigh}\nPerimetro = {(base + heigh) * 2}\nDiagonale: {sqrt(pow(base, 2) + pow(heigh, 2))}')
