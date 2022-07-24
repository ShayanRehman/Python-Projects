# -*- coding: utf-8 -*-
"""
@author: sid
"""
import random


def is_int(guess):
    # condition to check for numeric
    return guess.isnumeric()


def visuals(title):
    # formatting the outputs (title and result)
    print(len(title)*'*')
    print(title)
    print(len(title)*'*')


def guess_game(guess, truth):
    while not is_int(guess):  # check if the number is numeric or not
        print('Enter correct integer!!\n')
        guess = input(f'Enter number again: ')
    tries = 1  # tracks the number of tries to reach the answer
    while True:

        if int(guess) < truth:
            tries += 1
            print('Too low!!\n')
            guess = int(input(f'Try: {tries} | Enter number again: '))

        elif int(guess) > truth:
            tries += 1
            print('Too High!!\n')
            guess = int(input(f'Try: {tries} | Enter number again: '))

        else:
            RESULT = f'* You guessed the correct answer ({truth}) in total {tries} tries ! *'
            print('\n')
            visuals(RESULT)
            break


TITLE = "* NUMBER GUESSING GAME *"
visuals(TITLE)

ANSWER = random.randint(1, 10)  # randomized truth value
GUESS = input('\nEnter any number: ')

guess_game(GUESS, ANSWER)
