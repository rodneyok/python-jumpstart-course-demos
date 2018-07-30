import random

print('----------------------------------')
print('          Guess the number')
print('----------------------------------')

the_number = random.randint(0,100)

guess = -1

while guess != the_number:
    guess_text = input('Please guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print(f'Sorry, your guess of {guess} was too low.  Try again.')
    elif guess > the_number:
        print(f'Sorry, your guess of {guess} was too high.  Try again.')
    else:
        print(f'Great job!  You guessed the number {guess}!')

