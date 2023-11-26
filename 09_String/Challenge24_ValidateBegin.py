'''
Create a program that receives a city name as input, and validate if it starts with "Saint"
'''

cityName = str(input("Type a city name: ")).strip()

if cityName.lower().startswith('saint'):
    print("{} starts with \'Saint\'".format(cityName.title()))
else:
    print("{} doesn't start with \'Saint\'".format(cityName.title()))