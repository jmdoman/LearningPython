import random
import string
print('Welcome to Password Picker!')
while True:
    adjectives = ['sleepy', 'slow', 'wet', 'bad', 'fast', 'quick', 'little']
    nouns = ['apple', 'ball', 'card', 'cat', 'goat', 'book', 'frog', 'dinosaur']
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    goof = random.choice(string.punctuation)
    password = adjective + noun + str(number) + goof
    print('Your new password is: %s' % password)
    response = input('would you like a new password? y/n ')
    if response == 'n':
        break
