# Exercise 2: While loops

# You are asked to implement a text-based 'guess the number' game in Python. This will be an interactive game between the computer and the user. There will be a secret number and the user will need to guess that number.
# The problems you need to solve

# Your program will enclose a secret number of your choice. Then, the user will be asked to guess the secret number, ideally with the least number of guesses. Your program will need to keep a counter to count the number of guesses until the user hits the secret.
# At the end, if the user finds the secret, it should print a congrats message to the user but also the number of guesses it took for the user to find the secret. Your program should keep asking the user for a guess until the secret is found.

secret = 7
counter = 0

while True:
    guess = int(input('Provide your guess: '))
    counter += 1

    if guess == secret:
        print(f'Congrats! The secret number is {secret}. You found the secret after {counter} attempts.')
        break
    else:
        print('Wrong input. Try again.')
