import random
import string
adjectives = ['sleepy', 'slow', 'wet']
nouns = ['apple', 'ball', 'card']
adjective = random.choice(adjectives)
noun = random.choice(nouns)
number = random.randrange(0, 100)
goof = random.choice(string.punctuation)
print('Welcome to Password Picker!')
password = adjective + noun + str(number) + goof
print('Your new password is: %s' % password)
