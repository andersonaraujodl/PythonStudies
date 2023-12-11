'''
Write a program that return if a person is due to their military enlistment based on their year of birth.

Knowing that:
1) If they are 18yo or if they will turn 18 this year, they should enlist this year.
2) If they are younger they should only enlist when they are 18yo.
3) If they are older, they should already have enlisted.

In cases 2 and 3 you should explicitly say how much time they still have before enlisting or how much time has passed from their limit (18yo).
'''
import datetime
#imports
from datetime import date

#consts
AGE_OF_ENLISTMENT = 18
CURR_YEAR = int(datetime.date.today().strftime("%Y"))

#inputs
yearOfBirth = int(input("Year of birth: "))

age = CURR_YEAR - yearOfBirth

if age == AGE_OF_ENLISTMENT:
    print("It's about time! You should enlist this year! :)")
elif age < AGE_OF_ENLISTMENT:
    print("You're too young! The minimum age of enlistment is {}. You still have {} more years to do so.".format(AGE_OF_ENLISTMENT, AGE_OF_ENLISTMENT-age))
else:
    print("You' ve missed the deadline! You should have enlisted when you were {} years old. You've already passed {} years.\nPlease plan an appointment as early as possible to avoid issues in the future".format(AGE_OF_ENLISTMENT, age-AGE_OF_ENLISTMENT))