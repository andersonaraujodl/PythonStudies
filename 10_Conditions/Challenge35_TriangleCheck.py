'''
Write a program that receives the length of 3 lines and check if we can make a triangle with them.

Info not given:
By the Triangle Inequality Theorem:
a + b > c
a + c > b
b + c > a
'''

a = float(input("What's the first side length? "))
b = float(input("What's the second side length? "))
c = float(input("What's the third side length? "))

if a + b > c and a + c > b and b + c > a:
    print("We can make a triangle with sides {:.2}, {:.2} and {:.2}".format(a, b, c))
else:
    print("We can not make a triangle with sides {:.2}, {:.2} and {:.2}".format(a, b, c))