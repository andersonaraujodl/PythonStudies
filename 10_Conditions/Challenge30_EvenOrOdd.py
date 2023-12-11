'''
Writer a program that receives an int number and says if it's even or odd.
'''

num = int(input("Give me an int number: "))

print("{} is even".format(num) if num % 2 == 0 else "{} is odd".format(num))