from cryptography.fernet import Fernet

# Read the Fernet key from the file
with open('filekey1.key', 'rb') as key_file:
    key = key_file.read()

# Read the encrypted message from the file
with open('message1', 'rb') as message_file:
    encrypted_message = message_file.read()

# Decrypt the message and print the results
cipher = Fernet(key)
decrypted_message = cipher.decrypt(encrypted_message)
decrypted_message = decrypted_message.decode('ascii')
print('The decrypted Message is:', decrypted_message)
