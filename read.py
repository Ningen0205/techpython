import nfc
import binascii
import os

path = f"{os.getcwd()}/allowCardLists.txt"
print(path)

with open(path) as f:
    l = f.readlines()
    l = [i.replace('\n','') for i in l]
    print(type(l))
    print(l)