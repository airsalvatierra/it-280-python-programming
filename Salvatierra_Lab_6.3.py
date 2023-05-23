from random import randint


def remove_common_characters(text):
    text = text.replace('-', '')
    text = text.replace('.', '')
    text = text.replace('(', '')
    text = text.replace(')', '')
    return text


def is_zip_code(string_to_test):
    if len(string_to_test) == 10 and string_to_test[5] == '-'\
            and string_to_test[:5].isdigit() and string_to_test[6:].isdigit():
        return True

    return len(string_to_test) == 5 and string_to_test.isdigit()


def is_ssn_number(string_to_test):
    # Clean the string
    string_to_test = remove_common_characters(string_to_test)

    return len(string_to_test) == 9 and string_to_test.isdigit()


def is_phone_number(string_to_test):
    # Clean the string
    string_to_test = remove_common_characters(string_to_test)

    if len(string_to_test) == 11 and string_to_test[0] == '1':
        string_to_test = string_to_test[1:]

    return len(string_to_test) == 10 and string_to_test.isdigit()


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
