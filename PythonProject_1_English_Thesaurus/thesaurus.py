import json
import difflib 
from difflib import SequenceMatcher, get_close_matches
data = json.load(open("data.json","r"))

word = input("Pick a word: ")

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        alternative = input("Did you mean %s instead? Enter Y or N: " % get_close_matches(word, data.keys())[0])
        if alternative == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif alternative == 'N':
            return "The word doesn't exist. Please double check"
        else:
            return "Please enter 'Y' for Yes and 'N' for No."
    else:
        return "The word could not be found"

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
     