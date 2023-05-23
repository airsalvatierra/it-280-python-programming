import re
from random import randint


def is_zip_code(string_to_test):
    pattern = r'^\d{5}(?:-\d{4})?$'
    return re.match(pattern, string_to_test) is not None


def is_ssn_number(string_to_test):
    pattern = r'^\d{3}[-\s.]?\d{2}[-\s.]?\d{4}$'
    return re.match(pattern, string_to_test) is not None


def is_phone_number(string_to_test):
    pattern = r'^\+?1?[-.\s]?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$'
    return re.match(pattern, string_to_test) is not None


social_security_numbers = []
phone_numbers = []
zip_codes = []
file_name = f'numbers{randint(1, 2)}.txt'
# uncomment next line for local testing purposes
# file_name = 'numbers3.txt'

print(f'{file_name} file will be evaluated!')

with open(file_name, 'r') as file:
    # read all file lines
    lines = file.readlines()

    for line in lines:
        line = line.strip()
        if is_zip_code(line):
            zip_codes.append(line)
        elif is_ssn_number(line):
            social_security_numbers.append(line)
        elif is_phone_number(line):
            phone_numbers.append(line)


print('These are the zip codes founded!')
print(', '.join(zip_codes))
print()
print('These are the SSNs founded!')
print(', '.join(social_security_numbers))
print()
print('These are the phones founded!')
print(', '.join(phone_numbers))
