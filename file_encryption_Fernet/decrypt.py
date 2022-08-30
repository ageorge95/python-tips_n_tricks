from cryptography.fernet import Fernet

with open('key', 'rb') as filekey:
    key = filekey.read()

fernet = Fernet(key)

with open('my_file_encrypted.txt', 'rb') as enc_file:
    encrypted = enc_file.read()

decrypted = fernet.decrypt(encrypted)

with open('my_file_decrypted.txt', 'wb') as dec_file:
    dec_file.write(decrypted)