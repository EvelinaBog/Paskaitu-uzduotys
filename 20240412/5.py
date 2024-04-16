import random

lucky_number = random.randint(1, 10)
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    your_guess = int(input('Enter your guess: '))
    guess_count += 1
    if your_guess == lucky_number:
        print('You won!')
        break
    elif not guess_count == guess_limit and your_guess > lucky_number or your_guess < lucky_number:
        print('Try again!')
if guess_limit == guess_count:
    print('Sorry, you lost')
