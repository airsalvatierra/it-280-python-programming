file_name = 'random_file_lab53.txt'


with open(file_name, 'r') as file:
    # read all file lines
    lines = file.readlines()
    modified_lines = []

    for index, line in enumerate(lines, start=1):
        # updated new lines
        modified_lines.append(
            f'{str(index)}. {line.strip()} Sample\n'
        )

    # Loop 20 times
    with open(f'{file_name[:-4]}_2.txt', 'w') as file:
        # write new file
        file.writelines(modified_lines)
