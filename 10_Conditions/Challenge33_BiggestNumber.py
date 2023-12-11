'''
Write a program that receives 3 int numbers and prints the biggest and the smallest.
'''

a = int(input("Tell me the first number: "))
b = int(input("Tell me the second number: "))
c = int(input("Tell me the third number: "))

smallest = a
if b < smallest:
    smallest = b

if c < smallest:
    smallest = c

greatest = c
if a > greatest:
    greatest = a

if b > greatest:
    greatest = b


print("The smallest number is: {}".format(smallest))
print("The biggest number is: {}".format(greatest))