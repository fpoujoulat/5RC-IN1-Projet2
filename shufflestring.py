import random

def shuffle(string):

    char_list = list(string)

    random.shuffle(char_list)

    return ''.join(char_list)