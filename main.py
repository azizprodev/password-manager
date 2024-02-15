# module to encrypt and decrypt our text
from cryptography.fernet import Fernet

'''
use only once in program to generate key, if your key file is delete you again run it and then comment

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()
'''

# load key file that we generate using above function
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


# to add new account and password
def add():
    name = input("Type account name: ")
    user_password = input("Type account password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + " | " + fer.encrypt(user_password.encode()).decode() + "\n")


# to view our account details like (account name and password)
def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            name, password = data.split("|")
            print("Name:", name,"| Password:", fer.decrypt(password.encode()).decode())


# get input from user what he want(add new account or view all account details or quit)
while True:
    mode = input("Would you like to add new password or view password, Type(add or view) or q to quite: ").lower()

    if mode == "q":
        break

    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode!")
        continue
    