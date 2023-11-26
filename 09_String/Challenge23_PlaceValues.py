'''
Create a program that reads a number from 0 to 9999 and show the place value of each digit individually.

i.e.:
1893
Ones: 4
Tens: 3
Hundreds: 8
Thousands: 1

Spoiler: I didn't use string for this one.
'''

MIN_NUM = 0
MAX_NUM = 9999

num = -1
test = isinstance(num, int)
while not isinstance(num, int) or num < MIN_NUM or num > MAX_NUM:
    num = int( input("Type a number between 0 and 9999: ") )

ones = num // 1 % 10
tens = num // 10 % 10
hundreds = num // 100 % 10
thousands = num // 1000 % 10

print("Ones: {}".format(ones))
print("Tens: {}".format(tens))
print("Hundreds: {}".format(hundreds))
print("Thousands: {}".format(thousands))