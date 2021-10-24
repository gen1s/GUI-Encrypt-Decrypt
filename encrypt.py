from cryptography.fernet import Fernet
import os, getpass
import datetime

def cargar_key():

    return open(cwd + '\\keys\\example.key', 'rb').read()

def generar_key():
    key = Fernet.generate_key()
    try:
        os.mkdir(cwd + "\\keys")
    except OSError:
        pass
    with open(cwd + "\\keys\\example.key", 'wb') as key_file:
        key_file.write(key) 

def encrypt(items, key):
    f = Fernet(key)
    for item in items:
        print(item)
        with open(item, 'rb') as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)

        with open(item, 'wb') as file:
            file.write(encrypted_data)

cwd = os.getcwd()

if __name__ == '__main__':
    d = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    
    path_to_encript = cwd + '\\encryptme'


    items = os.listdir(path_to_encript)
    full_path = [path_to_encript + '\\' + item for item in items]

    generar_key()

    key = cargar_key()

    encrypt(full_path, key)