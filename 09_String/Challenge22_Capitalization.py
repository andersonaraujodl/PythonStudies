'''
Create a program that reads the full name of a person and returns:
1. The full name in upper case.
2. The full name in lower case.
3. How many letters the name has (ignoring spaces).
4. How many letters their first name has.
'''

fullName = str(input("Type your full name: ")).strip()
print("1. Upper Case: {}".format(fullName.upper()))
print("2. Lower Case: {}".format(fullName.lower()))

spacelessName = fullName.replace(" ", "")
print("3. LetterCount: {}".format(len(spacelessName)))

#OR

Lettercount = len(fullName) - fullName.count(' ')
print("3. LetterCount: {}".format(Lettercount))

firstName = fullName.split(' ', 1)
print("4. First Name Lenght: {}".format(len(firstName[0])))

#OR

print("4. First Name Lenght: {}".format(fullName.find(' ')))
