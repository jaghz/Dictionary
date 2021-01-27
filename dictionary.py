import json 
import difflib
from difflib import get_close_matches
data = json.load(open("data.json"))

def define(word):
    if word not in data.keys():
        similar_match = get_close_matches(word, data.keys(), n=5)
        if len(similar_match) > 0:  
            verify = input( "Did you mean: " + similar_match[0] + ' [y/n]? ')
            if verify == 'y' or verify == 'Y':
                return data[similar_match[0]]
            print("Unknown word, please double check. List of suggested words: ")
            for word in similar_match:
                print(word)
            return ''
        return "Unknown word, please double check"
    return data[word]

word = input("Enter a word: ")

output = define(word.lower())

if type(output) is list:
    for definitions in output:
        print(definitions)
