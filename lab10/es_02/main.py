if __name__ == '__main__':
    input_file_name = input('Input file name: ')
    output_file_name = input('Output file name: ')

    input_file = open(input_file_name, 'r')

    input_text = input_file.readlines()

    input_file.close()

    output_file = open(output_file_name, 'w')
    output_text = input_text.reverse()
    output_file.writelines(output_text)
    output_file.close()

    # TODO: fix traceback error