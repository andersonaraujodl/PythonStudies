'''
Write a program that randomly picks a number between 0 and 5 and ask the user a number as input.
Print on the screen if the user correctly guessed the number.
'''
from random import randint

randNum = randint(0, 5)
guessedNum = int(input("In a range so narrow, a challenge to derive,\nPick a number, between one and five.\nA game of chance, let your guess arrive,\nWhat's the magic number? Take a dive:\n"))

if guessedNum == randNum:
    print("Congratulations, I have thought of {}!!!".format(randNum))
else:
    print("Better chance next time, I have thought of {}, but you guessed {} :(".format(randNum, guessedNum))