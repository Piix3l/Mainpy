def main_c(input_file, starting_word, ending_word):
    copying = False
    section_count = 0
    i = 0

    with open(input_file, 'r') as infile:
        for line_number, line in enumerate(infile, 1):
            if starting_word in line:
                copying = True
                line = line[line.find(starting_word):]
                output_file_name = f"{section_count}-main.c"
                with open(output_file_name, 'w') as outfile:
                    outfile.write(line)
            elif copying:
                with open(output_file_name, 'a') as outfile:
                    outfile.write(line)
            if ending_word in line:
                copying = False
                with open(output_file_name, 'a') as outfile:
                    outfile.write("}\n")  
                section_count += 1
                i += 1

if __name__ == "__main__":
    input_file_path = 'mainpy.txt'  
    starting_word = input('Please type the first line in the x-main.c file: ') 
    ending_word = 'return (0);' 

    main_c(input_file_path, starting_word, ending_word)

    print("Done")
