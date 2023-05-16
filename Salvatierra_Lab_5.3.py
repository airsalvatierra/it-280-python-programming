import string
from random import choices, randint, uniform


file_name = 'random_file_lab53.txt'

# Open the file in write mode withing a context (which makes that file file
# will be closed after exiting the context)
with open(file_name, 'w') as file:
    lines = []

    # Loop 20 times
    for i in range(0, 20):
        # Generate random sets of characters or numbers
        four_characters = ''.join(
            choices(string.ascii_letters + string.punctuation, k=5)
        )
        integer = str(randint(0, 999)).zfill(4)
        three_characters = ''.join(choices(string.ascii_letters, k=3))
        floating = f'{round(uniform(0, 9999), 2):.2f}'.zfill(7)

        # Concatenate all strings
        line = f'{four_characters} {integer} {three_characters} {floating}\n'
        # Add string to list
        lines.append(line)

    file.writelines(lines)
