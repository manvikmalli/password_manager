from generate_password import generate_password, check_strength
from auth import set_master_password, verify_master_password
from vault import add_password, get_password
import os
if os.path.isfile("master.hash"):
    password = input("Enter master password: ")
    if not verify_master_password(password):
        print("Wrong password!")
        exit()
else:
    set_master_password()

while True:
    print("\n-----Main Menu-----")
    print("1.)Add a Password")
    print("2.)Get a Password")
    print("3.)Generate Password")
    print("4.)Check Strength")
    print("5.)Exit")
    choice=input("Enter a choice from 1-5: ")
    if choice=='1':
        add_password()
    elif choice=='2':
        site=input("Please eneter a site: ")
        result = get_password(site)
        print(f"Password: {result}")
    elif choice=='3':
        print(generate_password())
    elif choice=='4':
        pwd = input("Enter a password to check: ")
        print(check_strength(pwd))
    elif choice=='5':
        exit()
    else:
        print("invalid choice")
