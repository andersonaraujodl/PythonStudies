import math

n = float(input("Type a decimal number: "))

print("The integer part of {} is TRUNC {}; CEIL {}; FLOOR {}; ROUND {}.".format(n, math.trunc(n),
                                                                               math.ceil(n),
                                                                               math.floor(n),
                                                                               round(n))) #Explain different between Trunc, Floor, Ceil and Round / or cast directly with int()