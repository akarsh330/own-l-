guess_count = 0
guess_limit = 5
correct_guess = 8
while guess_count < guess_limit :
    guess = int(input('guess = '))
    if guess == correct_guess :
        print('you made the right guesss')
        print('congrads')
        break
else :
    print('sorry you failed')

    
    
    
