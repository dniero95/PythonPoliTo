if __name__ == '__main__':
    # todo: finish exercise
    number = int(input('Insert number: '))
    numbers = []
    numbers_matrix = []
    for i in range(number):
        numbers_matrix.append([])

    for i in range(pow(number, 2)):
        numbers.append(i + 1)

    for i in range(number):
        if i+1 % number == 0:

        for j in range(number):
            numbers_matrix[i].append(numbers[j])

    print(numbers)
    print(numbers_matrix)