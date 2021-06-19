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
    def __init__(self, patterns):
        self.__root = State()
        self.__patterns = patterns
        self.__states = [self.__root]
        self.__size = 1
        self.__current_state_index = 0
        self.__report = None
        self.__compares = 0
        for pattern in patterns:
            self.__insert_pattern(pattern)
        for state in self.__states:
            suffix = state.pattern[1:]
            while suffix != '':
                suffix_index = self.__get_pattern_index(suffix)
                if suffix_index == -1:
                    suffix = suffix[1:]
                else:
                    state.fake_link = suffix_index
                    state.fake_link_is_end = self.__states[suffix_index].is_end
                    suffix = ''
    