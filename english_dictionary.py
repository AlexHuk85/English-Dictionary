import json

data = json.load(open('data.json'))

user_input = input('Enter a word: ')
user_input = user_input.lower()

while user_input != 'quit_program':
    print(data[user_input])
    user_input = input('Enter a word: ')
    user_input = user_input.lower()

print('Program ended')
