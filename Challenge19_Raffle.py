from random import choice
from emoji import emojize

a = str(input("Enter the name of the first person to enter the raft: "))
b = str(input("Enter the name of the second person to enter the raft: "))
c = str(input("Enter the name of the third person to enter the raft: "))
d = str(input("Enter the name of the fourth person to enter the raft: "))

print( emojize("The winner was: {}! Congratulations! :partying_face:".format( choice([a, b, c, d]))) )