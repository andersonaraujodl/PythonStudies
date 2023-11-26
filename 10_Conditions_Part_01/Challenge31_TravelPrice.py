'''
Write a program that receives the distance (in Km) to travel to a destination
and calculate the price of the ticket knowing that:
1. The Km costs $0.50 for distances up to 200Km.
2. The Km costs $0.45 for longer distances.
'''

DIST_LIMIT = 200
SHORT_DIST_PRICE = 0.50
LONG_DIST_PRICE = 0.45

dist = float(input("What's the distance to your final destination? "))

if dist > DIST_LIMIT:
    finalPrice = dist * LONG_DIST_PRICE
else:
    finalPrice = dist * SHORT_DIST_PRICE

print("The cost of your ticket is ${:.2f}".format(finalPrice))