percentageDisc = float(input("What's the discount you would like to apply? (in %) "))
price = float(input("What's the original price of the product? "))
finalPrice = price - price*(percentageDisc/100)

print("The final price of the product after {}% off is {}!".format(percentageDisc, finalPrice))