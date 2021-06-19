#Base cnsts
ASCII_TABLE_LENGTH = 128
RUSSIAN_TABLE_LENGTH = 64
ALPHABET_LENGTH = ASCII_TABLE_LENGTH + RUSSIAN_TABLE_LENGTH
ASCII_LAST_CODE = 127
RUSSIAN_ALPHABET_FIRST_CODE = 1040


class State:
    childs = []
    parent = None
    data = str()
    
    def __init__(self, key):
        self.childs = []
        self.parent = None
        self.data = key



    