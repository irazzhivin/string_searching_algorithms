#Base cnsts
ASCII_TABLE_LENGTH = 128
RUSSIAN_TABLE_LENGTH = 64
ALPHABET_LENGTH = ASCII_TABLE_LENGTH + RUSSIAN_TABLE_LENGTH
ASCII_LAST_CODE = 127
RUSSIAN_ALPHABET_FIRST_CODE = 1040

def get_symbol_index(symbol):
    index = ord(symbol)
    if index > 127:
        index -= RUSSIAN_ALPHABET_FIRST_CODE - ASCII_LAST_CODE + 1
    return index

class State:
    def __init__(self, pattern=''):
        self.pattern = pattern
        self.links = [-1 for x in range(ALPHABET_LENGTH)]
        self.is_end = False
        self.fake_link = 0
        self.fake_link_is_end = False

    def __str__(self):
        return self.pattern


class Automata:
    root, size = None, 0
    
    def __init__(self):
        self.root = None
        self.size = 0
    
    def insert(self, val):
        if self.root is None:
            self.root = Node(num)
        else:
            self.insert_with_node(self.root, val)
    