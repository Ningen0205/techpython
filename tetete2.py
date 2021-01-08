import nfc
import binascii

cards = "010101129d16451b"

def connected(tag):
    idm = binascii.hexlify(tag.idm).decode('utf-8')
    print(idm)
    cards.encode('utf-8')
    print(cards == idm)
    return False

clf = nfc.ContactlessFrontend('usb')
clf.connect(rdwr={'on-connect': connected})
clf.close()
