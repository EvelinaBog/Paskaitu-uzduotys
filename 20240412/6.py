import random

lucky_number = random.randint(1, 3)
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    your_guess = int(input('Enter your guess: '))
    guess_count += 1
    if your_guess == lucky_number:
        print('You won!')
        break
    elif not guess_count == guess_limit and your_guess < lucky_number:
        print('Lucky number is higher')
    elif not guess_count == guess_limit and your_guess > lucky_number:
        print('Lucky number is lower')
    elif not your_guess == lucky_number and guess_limit == guess_count:
        print('Sorry, you lost')
