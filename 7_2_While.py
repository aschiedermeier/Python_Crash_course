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
# flag
import random as rn
active = True
while active:
    num = rn.randint(1,6)
    if num == 6:
        active = False
    else:
        print (num)

###########################################
# where have you been to?
# break statement to exit loop
while True:
    city = input("Which country have you been to? \n Enter 'quit' to finish\n")
    if city == "quit":
        break
    else:
        print (city.title() + " is awesome!")

###########################################
# list unven numbers
# if, continue statement to continue (go back up to continue loop) or stop (go down in code)
# continue is like bouncer
current = 0
while current < 10:
    current += 1
    if current%2 == 0:
    # if yes, go up (count +1)
    # if no, go down (print)
        continue
    print (current)