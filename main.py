from ctypes import alignment
from cryptography.fernet import Fernet
import os, getpass
import datetime
import tkinter as tk
from tkinter import Button, ttk
from PIL import Image, ImageTk
from tkinter.filedialog import askdirectory, askopenfile
import os



def generar_key(name):
    key = Fernet.generate_key()
    cwd = os.getcwd()
    try:
        os.mkdir(cwd + "\\keys")
    except OSError:
        pass
    with open(cwd + "\\keys\\{}.key".format(name), 'wb') as key_file:
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

def get_key(keypath):
    return open(keypath, 'rb').read()


def decrypt(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        
        with open(item, 'wb') as file:
            file.write(decrypted_data)


def decrypt_gui(path_decrypt, key_path_encrypt):
    items = os.listdir(path_decrypt.get())
    full_path = [path_decrypt.get() + '\\' + item for item in items]

    key = get_key(key_path_encrypt.get())

    print(key)
    print(path_decrypt.get())

    decrypt(full_path, key)
    os._exit(0)


def encrypt_gui(key_path_encrypt, path_encrypt, var_generate_key):
    key = ""
    print(var_generate_key)
    if var_generate_key == "generate":
        cwd = os.getcwd()
        key = get_key(cwd + "\keys" + "\{}.key".format(d))

    elif var_generate_key == "existing":
        print("entra")
        print(key_path_encrypt.get())
        key = get_key(key_path_encrypt.get())
        print(key)

    print(path_encrypt.get())
    items = os.listdir(path_encrypt.get())
    full_path = [path_encrypt.get() + '\\' + item for item in items]
    encrypt(full_path, key)
    os._exit(0)


def enc_key(enc_combo, path_encrypt):
    key = ""
    key_path_encrypt = tk.Entry(root, textvariable= key_path_text)

    if enc_combo == "Generate new key":
        generar_key(d)
        print("generate")
        var_generate_key = "generate"

    elif enc_combo == "Use existing key":

        

        key_path_text.set("Key path")
        key_path_encrypt.grid(column = 1, row = 9)

        key_browse_button = Button(root, text = "Browse", command=lambda: browse_file(),width= 20)
        key_browse_button.grid(column = 1, row = 10 )

        var_generate_key = "existing"
        print("cargar")

    else:
        print("Error invalid option")
    
    encrypt_button = Button(root, text = "Encrypt", command=lambda: encrypt_gui(key_path_encrypt, path_encrypt, var_generate_key),width= 20)
    encrypt_button.grid(column = 1, row = 11 )
    


def select():
    state = combo.get() 
    
    if state == "Encrypt":
        encrypt_dir = tk.Label(root, text= "Browse the directory you want to encrypt: ", font= "Arial")
        encrypt_dir.grid(column= 1, row = 3)

        
        path_encrypt = tk.Entry(root, textvariable= path_text)

        path_text.set("Path")
        path_encrypt.grid(column = 1, row = 4)

        browse_button = Button(root, text = "Browse", command= browse_dir,width= 20)
        browse_button.grid(column = 1, row = 5 )

        enc_key_dir = tk.Label(root, text= "Generate key or use existing one", font= "Arial")
        enc_key_dir.grid(column= 1, row = 6)
        

        enc_combo = ttk.Combobox(root)
        enc_combo['values'] = ('Generate new key', 'Use existing key')
        enc_combo.current(0)
        enc_combo.grid(column= 1, row = 7)

        enc_button = Button(root, text = "Select", command=lambda: enc_key(enc_combo.get(), path_encrypt),width= 20)
        enc_button.grid(column= 1, row = 8 )


    if state == "Decrypt":
        decrypt_dir = tk.Label(root, text= "Browse the directory you want to encrypt: ", font= "Arial")
        decrypt_dir.grid(column= 1, row = 3)

        
        path_decrypt = tk.Entry(root, textvariable= path_text)

        path_text.set("Path")
        path_decrypt.grid(column = 1, row = 4)

        browse_decrypt_button = Button(root, text = "Browse", command= browse_dir,width= 20)
        browse_decrypt_button.grid(column = 1, row = 5 )

        dec_key_dir = tk.Label(root, text= "Browse the key", font= "Arial")
        dec_key_dir.grid(column= 1, row = 6)

        
        key_path_decrypt = tk.Entry(root, textvariable= key_path_text)

        key_path_text.set("Key path")
        key_path_decrypt.grid(column = 1, row = 9)

        key_browse_button = Button(root, text = "Browse", command=lambda: browse_file(),width= 20)
        key_browse_button.grid(column = 1, row = 10 )


        print("cargar")

        decrypt_button = Button(root, text = "Decrypt", command=lambda:decrypt_gui(path_decrypt, key_path_decrypt) ,width= 20)
        decrypt_button.grid(column = 1, row = 11 )
    


def browse_dir():
    path = askdirectory(parent = root, title = "Chose a file")
    path_text.set(path)

def browse_file():
    path = askopenfile(parent = root, mode = 'rb', title = "Chose the key to decrypt your files", filetypes=[("Key file", "*.key")])
    print(path)
    key_path_text.set(path)
    return path




d = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
root = tk.Tk()

path_text = tk.StringVar()
key_path_text = tk.StringVar()
key_path = ""

canvas = tk.Canvas(root, width= 400, height= 700)
canvas.grid(columnspan=30, rowspan= 100)

title = tk.Label(root, text= "Encrypt Or Decrypt Your Files", font= "Arial 24")
title.grid(column= 1, row = 0)

combo = ttk.Combobox(root)
combo['values'] = ('Encrypt', 'Decrypt')
combo.current(0)
combo.grid(column= 1, row = 1)

button = Button(root, text = "Select", command= select,width= 20)
button.grid(column= 1, row = 2 )


root.mainloop()