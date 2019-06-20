###########################################
# Book "Python Crash course" - Eric Matthes
# Chapter 7: User input and while loops
###########################################

###########################################
# parrot_2: repeating until user types "quit"
# flag "active", while loop, input

active = True
while active:
    message = input("I'm a flag parrot and repeat what you say, until you say 'quit'!\n")
    
    if message == "quit":
        active = False
    
    else:
        print (message)

###########################################
# print out random numbers, until i get 6
# random, flag
import random as rn
active = True
while active:
    num = rn.randint(1,6)
    if num == 6:
        active = False
    else:
        print (num)