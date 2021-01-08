import nfc
import binascii
import os

path = f"{os.getcwd()}/allowCardLists.txt"

with open(path) as f:
    cards = f.readlines()
    cards = [i.replace('\n','') for i in cards]
    
def connected(tag):
    newflg = True
    idm = binascii.hexlify(tag.idm).decode('utf8')
    print(idm)
    for card in cards:
        card.encode('utf-8')
        if card == idm:
            newflg = False
        else:
            pass
    if newflg:
        print("new card!")
        with open(path, mode='a+') as f:
            f.write(f"\n{idm}")
    return False

clf = nfc.ContactlessFrontend('usb')
clf.connect(rdwr={'on-connect': connected})
clf.close()
