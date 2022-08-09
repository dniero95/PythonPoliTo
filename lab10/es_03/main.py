if __name__ == '__main__':
    files = input('files list: ').split(',')
    word = input('word to find: ')

    for file in files:
        try:
            fp = open(file.strip())
        except FileNotFoundError:
            print(f'Error! For {file.strip()} no such file was found!')
        except:
            print(f'Error! ')
        else:
            lines = fp.readlines()
            for line in lines:
                if line.lower().find(word.lower()) != -1:
                    print(f'{file.strip()}: {line.strip()}')
            fp.close()

