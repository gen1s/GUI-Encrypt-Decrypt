from cryptography.fernet import Fernet
import os, getpass

def cargar_key():

    return open(cwd + '\\keys\\example.key', 'rb').read()


def decrypt(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        
        with open(item, 'wb') as file:
            file.write(decrypted_data)

cwd = os.getcwd()

if __name__ == '__main__':
    
    path_to_encript = cwd + '\\encryptme'

    items = os.listdir(path_to_encript)
    full_path = [path_to_encript + '\\' + item for item in items]

    key = cargar_key()

    decrypt(full_path, key)
