from random import shuffle

a = str(input("Enter the name of the first student: "))
b = str(input("Enter the name of the second student: "))
c = str(input("Enter the name of the third student: "))
d = str(input("Enter the name of the fourth student: "))

list = [a, b, c, d]
shuffle(list)

print("The order or presentation is: {}".format(list))