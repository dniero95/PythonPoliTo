if __name__ == '__main__':
    
    # In this list I save the theater place

    theater_place = [ [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
                      [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
                      [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
                      [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
                      [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
                      [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
                      [20, 20, 30, 30, 40, 40, 30, 30, 20, 20],
                      [20, 30, 30, 40, 50, 50, 40, 30, 30, 20],
                      [30, 40, 50, 50, 50, 50, 50, 50, 40, 30]
                    ]

    # Loop through the list until the user exit the program
    while True:

        # Show all the spots. Where is written zero the spot is already taken
        print('\nAvailable spots:\n')
        for line in theater_place:
            for spot in line:
                # For better formatting
                if spot / 10 < 1:
                    print(' ', end='')
                print(f'{spot}', end=' ')
            print()
        print('\n')


        try:
            option = int(input('Select 1 to choose the place.\nSelect 2 to choose the price.\nSelect 0 to exit.\n >>> '))
        except:
            print('Error! Select a number\n')
            continue


        if option == 0:
            print('Goodbye!\n')
            exit()
        elif option == 1:
            try:
                row = int(input('Choose the row: '))
                column = int(input('Choose the column: '))
            except:
                print('Error! Select a number\n')

            if 1 <= row <= len(theater_place) and 1 <= column <= len(theater_place[0]):
                theater_place[row - 1][column - 1] = 0
            else:
                print('Error! Index out of range!')
                continue
        elif option == 2:
            try:
                price = int(input('Insert the price: '))
            except:
                print('Error! Choose a integer!')

            for line in theater_place:
                if price in line:
                    line[line.index(price)] = 0
                    break
        else:
            print('Error! Select a number between 0 and 2\n')



