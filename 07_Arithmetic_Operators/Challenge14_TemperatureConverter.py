celcius = float(input("What's the temperature in ºC? " ))

def celcius_to_farenheit(c):
    return (c * 9 / 5) + 32

print("{}ºC is equals to {:.2f}ºF!".format(celcius, celcius_to_farenheit(celcius)))