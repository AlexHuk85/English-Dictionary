import json

data = json.load(open('data.json'))

def translate(word):
    return data[word]

word = input('Enter a word: ')
word = word.lower()

while word != 'quit_program':
    if word not in data:
        print('Please check your word again')
        word = input('Enter a word: ')
        word = word.lower()
        continue
    else:
        print(translate(word))
        word = input('Enter a word: ')
        word = word.lower()
print('Program ended')
