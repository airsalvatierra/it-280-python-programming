file_name = 'random_file_lab53.txt'

# Open the file in write mode withing a context (which makes that file file
# will be closed after exiting the context)
with open(file_name, 'r') as file:
    lines = file.readlines()
    modified_lines = []

    for index, line in enumerate(lines, start=1):
        modified_lines.append(
            f'{str(index)}. {line.strip()} Sample\n'
        )

    # Loop 20 times
    with open(file_name, 'w') as file:
        file.writelines(modified_lines)
