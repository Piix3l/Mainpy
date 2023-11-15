import re


input_file_name = "mainpy.txt"
output_file_name = input("Ouput file name: ")


with open(input_file_name, 'r') as input_file, open(output_file_name, 'w') as output_file:
    content = input_file.read()
    prototypes = re.findall(r'Prototype: (.*?);', content)
    output_file.write("#ifndef FILE_MAIN" + '\n')
    output_file.write("#define FILE_MAIN" + '\n' + '\n')
    for prototype in prototypes:

        output_file.write(prototype + '\n')

    output_file.write('\n' + "#endif" + '\n')