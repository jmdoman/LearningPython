import random
import string
import msvcrt as m
def wanit():
    m.getch()
adjectives = ['sleepy','slow','smelly','wet','fat','fluffy','white','proud','brave']
colors = ['red','orange','yellow','green','blue','purple']
nouns = ['apple','dinosaur','ball','toaster','goat','dragon','hammer','duck','panda','telephone','banana','teacher']
print('Welcome to the Password Picker!')

while True:
    for num in range(3):
        adjective = random.choice(adjectives)
        color = random.choice(colors)
        noun = random.choice(nouns)
        number = random.randrange(0, 100)
        special_char = random.choice(string.punctuation)
        password = adjective + color + noun + str(number) + special_char
        if num == 0:
            number = "first"
        elif num == 1:
            number = "second"
        elif num == 2:
            number = "third"
        print('Your ' + number + 'new password is ' + password)
    
    response = input('Would you like another password? Type y or n ')
    if response == 'n':
        break


# wait()
