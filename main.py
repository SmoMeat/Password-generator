from PyDictionary import PyDictionary
from english_words import get_english_words_set
from random import random
import math


def generate_password():
    dictionary = PyDictionary()
    meaning = None

    while not meaning:
        lowerset = get_english_words_set(['web2'], lower=True)
        random_word = list(lowerset)[math.floor(random() * len(lowerset))]
        meaning = dictionary.meaning('Day')
    
    print(meaning)


if __name__ == '__main__':
    generate_password()


