# Going to be used to initialize the dictionary used in my Simple Scrabble project

import json

with open('words_dictionary.json', 'r') as infile:
    Scrabble_dict = json.load(infile)

