brlPrice = float(input("What's the current USD exchange rate to BRL? "))
usdPrice = 1 / brlPrice #brl to usd
currentBrl = float(input("How much Brazilian Reais do you have? "))

print("With R$ {} you can buy US$ {}".format(currentBrl, round(currentBrl*usdPrice,2)))