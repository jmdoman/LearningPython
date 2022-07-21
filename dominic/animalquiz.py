def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower()  == answer.lower():
            print('correct')
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input ("try again...")
            attempt  = attempt + 1
    if attempt == 3:
        print('The right answer is ' + answer + ', silly!')
score = 0
print('guess the animal')
guess1  = input('which bear lives at the north pole? ')
check_guess(guess1, 'polar bear')
guess2 = input('which animal jumps the furthest? ')
check_guess(guess2, 'kangaroo')
guess3 = input('what is the largest land animal? ')
check_guess(guess3, 'elephant')
print('your score is ' + str(score))
    
