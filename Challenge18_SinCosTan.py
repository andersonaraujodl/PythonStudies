import math

a = float(input("Type one angle in degrees: "))
rad = math.radians(a)

print("The Sine of {} is {}\nThe Cosine of {} is {}\nThe Tangent of {} is {}".format(a, round(math.sin(rad), 4), a, round(math.cos(rad), 4), a, round( math.tan(rad), 4) ))