from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open('key', 'wb') as filekey:
    filekey.write(key)

fernet = Fernet(key)

with open('my_file.txt', 'rb') as file:
    original = file.read()

encrypted = fernet.encrypt(original)

with open('my_file_encrypted.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)