import bcrypt
def set_master_password():
    password=input("Enter a password: ")
    pass_byte=password.encode('utf-8')
    salt=bcrypt.gensalt(rounds=12)
    pass_hash=bcrypt.hashpw(pass_byte,salt)
    with open("master.hash", "wb") as file:
        file.write(pass_hash)

def verify_master_password(password):
    with open("master.hash", "rb") as file:
        content=file.read()
        res = bcrypt.checkpw(password.encode('utf-8'), content)
        return res
        