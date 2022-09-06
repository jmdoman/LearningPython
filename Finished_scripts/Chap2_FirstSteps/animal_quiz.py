def check_guess(guess,answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Correct!')
            score = score + 3 - attempt
            still_guessing = False
        else:
            if attempt < 2:
                guess = input('Sorry, wrong answer, try again. ')
            attempt = attempt + 1
    if attempt == 3:
        print('The correct answer is ' + answer + ', you silly goose!')
    print('----')
score = 0
questions = 4 #number of questions
perfect = (questions * 3)
print('Guess the animal!')
guess1 = input('Which bear lives at the north pole? ')
check_guess(guess1, 'polar bear')
guess2 = input('Which is the fastest land animal? ')
check_guess(guess2, 'cheetah')
guess3 = input('Which is the largest animal? ')
check_guess(guess3, 'blue whale')
guess4 = input('which one of these is a fish?\n \
A) Whale\n B) Dolphin\n C) Shark\n D) Squid\n \
Type A, B, C or D. ')
check_guess(guess4, 'C')
print('=========================')
print('your score is ' + str(score) + '/' + str(perfect))
# print('a perfect score would be ' + str(perfect))
if score == perfect:
    print('Perfect!')
elif score > (perfect - 3):
    print ('almost perfect!')
elif score >= (perfect - 3):
    print('not bad!')
elif score >= (perfect - 6):
    print('hmm.')
elif score >= (perfect - 9):
    print('kind of silly...')
elif score < questions: #no questions right at all
    print('Very silly!')

    


