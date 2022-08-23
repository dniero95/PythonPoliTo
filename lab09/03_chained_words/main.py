import sys

if __name__ == '__main__':
    while True:
        option = int(input('Press 0 to end the program.\nPress 1 to start the game.\n >>> '))

        if option == 0:
            print('Goodbye!')
            sys.exit()
        elif option == 1:
            print('GAMESTART')

            chained_words = []

            while True:
                word = input('Insert next word: ')

                # Handle game over condition for not continuing
                if word == '*':
                    print('GAMEOVER')
                    break

                # Handle first word
                if len(chained_words) != 0:

                    # Handle game over for word repetition
                    if word in chained_words:
                        print('GAMEOVER')
                        break

                    # Handle game over for bad concatenation

                    if chained_words[-1][-2:] != word[:2]:
                        print('GAMEOVER')
                        break

                chained_words.append(word)


        else:
            print('Error! Option non available!')
