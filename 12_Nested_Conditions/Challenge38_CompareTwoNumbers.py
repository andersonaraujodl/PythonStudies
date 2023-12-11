'''
Write a program that compare two integer numbers given by the user, and tell which one is higher.
If they are equal, you should say "There's no higher number, they are equal.".
'''

higher = int(input("Type the first number to compare. "))
x = int(input("Type the second number to compare. "))

if higher == x:
    print("There's no higher number, they are equal.")
    exit()

if x > higher:
    higher = x

print("{} is the higher values.".format(higher))