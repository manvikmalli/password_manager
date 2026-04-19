from cryptography.fernet import Fernet
import os
import json
def load_key():
    if os.path.exists("cellar.py") and os.path.getsize("cellar.py")>0:
        with open("cellar.py","rb")as f:
            return f.read()
    else:
        key=Fernet.generate_key()
        with open("cellar.py","wb")as f:
            f.write(key)
        return key
def add_password(site, password):
    key = load_key()
    cipher_suite = Fernet(key)
    pass_byte = password.encode('utf-8')
    encrypted_password = cipher_suite.encrypt(pass_byte)
    if os.path.isfile("site.json"):
        with open("site.json","r")as file:
            vault=json.load(file)
    else:
        vault={}
    vault[site]=encrypted_password.decode()
    with open("site.json","w")as file:
        json.dump(vault,file)
def get_password(site):
    if os.path.isfile("site.json"):
        with open("site.json","r")as file:
            vault=json.load(file)
            encrypted_password=vault[site]
            encrypted_password_byte=encrypted_password.encode('utf-8')
            key=load_key()
            cipher_suite=Fernet(key)
            decrypted_pass = cipher_suite.decrypt(encrypted_password_byte).decode()
            return decrypted_pass
    else:
        return None

        

        


