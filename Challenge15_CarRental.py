km = float(input("Kilometers driven? "))
days = int(input("Days rented? "))
#pricing: $0.15 per km & $60 per day
pricePerKm = 0.15
pricePerDay = 60
finalPrice = (pricePerKm * km) + (pricePerDay * days)

print("The total price of a rental for {} days and {} km is: ${}".format(days, km, format(finalPrice, ".2f")))