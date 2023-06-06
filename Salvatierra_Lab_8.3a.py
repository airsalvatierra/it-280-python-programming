from cryptography.fernet import Fernet

name = 'Salvatierra'
student_id = input('Enter your Student ID: ')
while student_id == '':
    student_id = input('Enter your Student ID: ')

# Generate Fernet key and save it to a binary file
print('Generating Fernet key saved to fernet_key.bin')
key = Fernet.generate_key()
with open('fernet_key.bin', 'wb') as key_file:
    key_file.write(key)
print('Generating Fernet key saved to fernet_key.bin... Done!')


# Encrypt name and student id
print('Encrypting name and student id')
cipher = Fernet(key)
encrypted_text = cipher.encrypt(f'{name} {student_id}'.encode())
with open('encrypted_token.bin', 'wb') as token_file:
    token_file.write(encrypted_text)
print('Name and student id encrypted and saved to encrypted_token.bin')

# Uncomment next lines to print the descrypted text
# decrypted_text = cipher.decrypt(encrypted_text)
# print(f'The decrypted text is: {decrypted_text.decode("ascii")}')
