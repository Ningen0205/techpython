import nfc
import binascii
import os

path = f"{os.getcwd()}/allowCardLists.txt"
#cards = "010101129d16451b"

with open(path) as f:
    cards = f.readlines()
    cards = [i.replace('\n','') for i in cards]
    print(type(cards))
    print(cards)

def connected(tag):
    idm = binascii.hexlify(tag.idm).decode('utf-8')
    for card in cards:
        card.encode('utf-8')
        print(card == idm)
    return False

clf = nfc.ContactlessFrontend('usb')
clf.connect(rdwr={'on-connect': connected})
clf.close()