'''
Write a program to convert a number into Binary, Octal or hexadecimal.

The user will give you an integer number as input, and will choose which base they want to convert to.
'''

num = int(input("What number would you like to convert? "))

base = int(input('''What conversion base would you like to convert {} to?\n
1) BINARY\n
2) OCTAL \n
3) HEXADECIMAL\n'''.format(num)))

if base == 1:
    print("{} converted to binary is {}".format(num, bin(num)[2:]))
elif base == 2:
    print("{} converted to octal decimal is {}".format(num, oct(num)[2:]))
elif base == 3:
    print("{} converted to octal decimal is {}".format(num, hex(num)[2:]))
else:
    print("You have entered an invalid base to convert.")