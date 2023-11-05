h = float(input("What's the height of the wall to be painted? "))
w = float(input("What's the width of the wall to be painted? "))
paintAreaPerLiter = 2

a = h * w
litersNeeded = a / paintAreaPerLiter

print("You will need {} liters of paint to paint {} m2".format(litersNeeded, a))
