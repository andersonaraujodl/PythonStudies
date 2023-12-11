'''
Write a program that receives the speed of a car and prints a message saying if the car is over the speed limit
of 80km/h.

In positive case, provide the total amount of fine they will have to pay, knowing that for each exceeded km
it costs $9.00
'''

SPEED_LIMIT = 80
COST_PER_KM = 9.00
speed = float(input("Type the speed of the car in km/h: "))

if speed > SPEED_LIMIT:
    fine = ( speed - SPEED_LIMIT ) * COST_PER_KM
    print("You exceeded the speed limit of {}km/h and you will be charged ${:.2f} for you excess".format(SPEED_LIMIT, fine))
else:
    print("Thank you for respecting the speed limit of {}km/h. Keep driving safe!".format(SPEED_LIMIT))