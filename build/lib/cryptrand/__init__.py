from random import choice, seed
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

ru_chars_lower = 'йцукеёнгшщзхъфывапролджэячсмитьбю'

ru_chars_upper = 'ЙЦУКЕЁНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'

all_strings = ascii_lowercase + \
    ascii_uppercase + \
    ru_chars_upper + \
    ru_chars_lower + \
    digits + \
    punctuation



def get_dict(key):
    seed(key)
    chars_dict = {}
    for text_char in all_strings:
            char = choice(all_strings)
            while char in chars_dict.values():
                char = choice(all_strings)
            chars_dict[text_char] = char
    return chars_dict


def encrypt(text, key):
    chars_dict = get_dict(key)
    res = ''
    try:
        for char in text:
            res += chars_dict[char]
    except NameError:
        return 'Invalid character'
    return res


def decrypt(text, key):
    chars_dict = get_dict(key)
    res = ''
    try:
        for char in text:
            for key, item in chars_dict.items():
                if item == char:
                    res += key
    except NameError:
        return 'Invalid character'
    return res
