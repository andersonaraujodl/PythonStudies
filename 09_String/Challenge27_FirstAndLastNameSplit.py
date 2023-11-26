'''
Write a program that receives a full name of a person and shows first and last name individually.
'''

fullName = str(input("Type your full name: ")).strip()

splitName = fullName.split(' ')
print("Your first name is: {}".format(splitName[0]))
print("Your last name is: {}".format(splitName[len(splitName) - 1]))