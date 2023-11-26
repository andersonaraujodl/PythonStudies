from math import hypot

a = float(input("Type the first side of the triangle: "))
b = float(input("Type the second side of the triangle: "))
#h = math.sqrt( math.pow(a, 2) + math.pow(b, 2) ) // or use ** (1/2) instead of pow
h = hypot(a, b)

print("The hypotenuse of a triangle with side a = {} and side b = {} is {}".format(a, b, round(h, 2)))