from os import fdopen


file_input = open('input.txt', 'r')

input_lines = file_input.readlines()

file_ouput = open('output.txt', 'w')

output_lines = []

for line in input_lines:
    output_lines.append(f'/*{input_lines.index(line)+1}*/{line}')

file_ouput.writelines(output_lines)