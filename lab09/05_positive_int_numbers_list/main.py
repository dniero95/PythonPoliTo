def format_list(list):
    return ':'.join(str(list))

def del_max_min_from_list(list):
    l = list
    l.remove(max(list))
    l.remove(min(list))
    return l

def only_even_numbers(list):
    return [number for number in list if number % 2 == 0]

def only_two_digits_numbers(list):
    return [number for number in list if number > 9]

if __name__ == '__main__':
    string_list = input('Numbers: ')
    numbers = string_list.split(':')
    numbers = [int(num) for num in numbers]
    print(f'Same numbers without max and min:\n{format_list(del_max_min_from_list(numbers))}\nOnly even numbers:\n{format_list(only_even_numbers(numbers))}\nOnly two digits numbers:\n{format_list(only_two_digits_numbers(numbers))}')


# todo:fix everything