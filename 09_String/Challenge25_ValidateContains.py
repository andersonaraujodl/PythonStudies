'''
Check if the name of a person contains a given name or last name.

i.e:
Anderson Lima
checks if contains: Lima.
'''

fullName = str(input("Type the full name: ")).strip()
nameToCheck = str(input("Check if the name contains what substring? ")).strip()

if fullName.lower().find(nameToCheck.lower()) >= 0:
    print("With Find: {} contains {}".format(fullName.title(), nameToCheck.title()))
else:
    print("With Find: {} doesn't contain {}".format(fullName.title(), nameToCheck.title()))

#OR

if nameToCheck.lower() in fullName.lower():
    print("With In: {} contains {}".format(fullName.title(), nameToCheck.title()))
else:
    print("With In: {} doesn't contain {}".format(fullName.title(), nameToCheck.title()))