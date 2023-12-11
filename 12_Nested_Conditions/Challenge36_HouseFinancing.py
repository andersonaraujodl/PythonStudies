'''
Write a program to simulate a mortgage.
It will receive from the user: the value of the house; their salary (yearly); in how many years they wish to finance.
Return the monthly payment knowing it can't exceed 30% of their salary, or the mortgage will be denied.
'''

#Consts
MONTHS_IN_A_YEAR = 12
LIMIT_YEARS_TO_PAY = 50
DEBIT_LIMIT = 0.3

#Inputs
housePrice = float(input("What's the price of the house you want to buy? "))
yearlySalary = float(input("What's your yearly annual income? "))
yearsToPay = int(input("In how many years you wish to pay? "))

while yearsToPay > LIMIT_YEARS_TO_PAY:
    print("You exceeded the limit of years to pay ({} years). Try again.".format(LIMIT_YEARS_TO_PAY))
    yearsToPay = int(input("In how many years you wish to pay? "))

monthlySalary = yearlySalary / MONTHS_IN_A_YEAR
monthlyDebitLimit = monthlySalary * DEBIT_LIMIT

monthlyPayment = housePrice / yearsToPay / MONTHS_IN_A_YEAR

if monthlyPayment > monthlyDebitLimit:
    print("You exceeded the monthly allowed debit according to your salary ({}%). You can try again after 6 months".format(DEBIT_LIMIT*100))
else:
    print("Congratulations, your mortgage request was approved! Your monthly balance will be: {:.2f}.".format(monthlyPayment))

