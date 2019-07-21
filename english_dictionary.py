import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yes_no = input('Did you mean %s instead? Y if yes, or N if no: ' % get_close_matches(w, data.keys())[0])
        if yes_no == 'Y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yes_no == 'N':
            return "The word doesn't exist. Please check and try again."
        else:
            return 'We cannot understand this word.'
    else:
        return "The word doesn't exist. Please check and try again."

user_input = input('Enter a word: ')

print(translate(user_input))
