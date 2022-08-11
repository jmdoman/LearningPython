print('hello, world!')
person = input('what is your name?')
print('hello, ', person)
age = 12
print(age)
x = 6
y = x * 7
print(y)
x = 10
print(y)
x = 10
y = x * 7
print(y)
name = 'Ally Alien'
print(name)
name = 'Ally Alien'
greeting = 'welcome to Earth, '
message = greeting + name
print(message)
len(message)
rockets_player_1 = 'Rory'
rockets_player_2 = 'Rav'
rockets_player_3 = 'Rachel'
planets_player_1 = 'Peter'
planets_player_2 = 'Pablo'
planets_player_3 = 'Polly'
rockets_players = ['Rory', 'Rav', 'Rachel', 'Renata', 'Ryan', 'Ruby']
planets_players = ['Pter', 'Pablo', 'Polly', 'Penny', 'Paula', 'Patrick']
rockets_players[0]
planets_players[5]
answer_one = True
answer_two = False
age = 10
if age == 10:
    print('You are ten years  old.')
pineapples = 5
zebras = 2
pineapples > zebras
zebras < pineapples
pineapples == zebras
pineapples != zebras
(pineapples == 3) and (zebras == 2)
(pineapples == 3) or (zebras == 2)
age = 10
height = 60
(age > 8) and ('height > 60 inches')
is_dark = input('Is it dark outside? y/n)')
if is_dark == 'y':
    print('Goodnight! Zzzzzzzzzzzzzzzz....')
tentacles = input('Do you have tentacles? (n/y)')
if tentacles  == 'y':
    print('I never knew ocopuses could type!')
else:
        print('Greeting,  human!')
weather = input('what is the forecast for today? (rain/snow/sun)')
if weather == 'rain':
    print('remember your umbrella!')
elif weather == 'snow':
    print('remember your wooly gloves!')
else:
    print('remember your sunglasses!')
for counter in range(1, 11):
    print('Emma\'s room - keep out!!!')
person = input('what is your name?')
print('hello, ', person)
hippos = 0
answer = 'y'
while answer == 'y':
    hippos = hippos + 1
    print(str(hippos) + ' balancing hippos!')
    answer = input('add anotheer hippo? (y/n)')
while True:
    answer = input('are you bored yet?  (y/n)')
    if answer == 'y':
        print('how rude!')
        break
for hooray_counter in range(1, 4):
    for hip_counter in range(1, 3):
        print('Hip')
    print('Hooray!')
def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Correct answer')
            score = score + 2 - attempt
            still_guessing = False
        else:
            if attempt < 1:
                guess = input('Sorry wrong answer. Try again. ')
            attempt = attempt + 1
    if attempt == 3:
        print('the correct answer is  ' + answer)
score = 0
print('guess the animal!')
guess1 = input('which bear lives at the North Pole? ')
check_guess(guess1, 'polar bear')
guess2 = input('which is the fastest land animal? ')
check_guess(guess2, 'cheetah')
guess3 = input('which is the lagest animal? ')
check_guess(guess3, 'blue whale')
guess4 = input('which one of these is a fish?\n \
A) whale\n B) dolphin\n C) shark\n D) squid\n \
type A, B, C, or D ')
check_guess(guess4, 'C')       
print('Your score is ' + str(score))
name = input('what is your name?')
greeting =  'Hello ' + name
print(greeting)
max(10, 16, 30, 25, 21, 28)


