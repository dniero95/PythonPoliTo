if __name__ == '__main__':
    year = int(input('Anno = '))

    if year > 1582:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print(f'Il {year} é un anno bisestile!')
                else:
                    print(f'Il {year} non é un anno bisestile!')
            else:
                print(f'Il {year} é un anno bisestile!')