'''
Write a program that given a year, tells if it is a leap year or not
'''

year = int(input("Type a year: "))

print("{} is a leap year.".format(year) if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else "{} is not a leap year.".format(year))