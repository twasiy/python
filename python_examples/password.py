from hashlib import *
from getpass import *
def get_hashed_text(text:str):
    return sha256((text.encode())).hexdigest()
while True:
    password = getpass('enter password:')
    if get_hashed_text(password) != "78ea9e1ed915bd269ac15a70525b5242e88fd9dee56a42e9a5ef3a0bed6750a3":
        print(f'your given key is incorrect..\n')
    else:
        break
print('You got it .')