# The aim of this exercise is to improve the previous 'guess the number' game to make it better and more intelligent! You will implement functions to make the game better by generating a random secret, providing hints (how far/close the guess is) to the user.

# In this lab, you will have the opportunity to practice writing functions in Python. 
# The problems you need to solve

# For this exercise, you will need to do the following:

#     1-Call the get_random_secret function that we implemented for you to get a random secret (instead of having a hard-coded one).

#     2-Write a function to check the validity of the user input. It should return True if the input is between 0 and 100 (inclusive) or False otherwise (negative number or greater than 100).

#     3-Write a function that will estimate how far the guess is from the secret and provide nice messages to the user to guide them.

import random

def get_random_secret():
    return random.randint(0, 100)


def is_guess_valid(guess):
    return guess >= 0 and guess <= 100

def how_off_is_the_guess(guess, secret):
    diff = abs(guess - secret)
    if diff < 10:
        print('Very hot!')
    elif diff > 10 and diff <= 20:
        print('Hot')
    elif diff > 20 and diff <= 50:
        print('Cold')
    else:
        print('Very cold')

secret = get_random_secret()
counter = 1

while True:
    guess = int(input('Please provide a guess: '))

    if is_guess_valid(guess):
        if guess == secret:
            print(f'Congrats! The secret was {secret}. You found the secret after {counter} attempts.')
            break
        else:
            how_off_is_the_guess(guess, secret)

        counter += 1
    else:
        print('Please provide a number within the range [0, 100].')
