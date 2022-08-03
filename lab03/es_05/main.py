if __name__ == '__main__':
    year = int(input('Anno = '))

    # if year > 1582:
    #     if year % 4 == 0:
    #         if year % 100 == 0:
    #             if year % 400 == 0:
    #                 print(f'Il {year} é un anno bisestile!')
    #             else:
    #                 print(f'Il {year} non é un anno bisestile!')
    #         else:
    #             print(f'Il {year} é un anno bisestile!')
    #

    # Versione con un unico if
    if year > 1582 and year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0):
        print(f'Il {year} é un anno bisestile!')
    else:
        print(f'Il {year} non é un anno bisestile!')


