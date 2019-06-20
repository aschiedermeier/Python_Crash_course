###########################################
# Book "Python Crash course" - Eric Matthes
# Chapter 7: User input and while loops
###########################################

###########################################
# name and age input
# name input
name = input("What's your name?\n")
print("Hi, "+ str(name.title()))
# age input
age = input("What's your age?\n")
# transform input from string to integer
age = int(age)
if age >= 18:
    print ("ok")
else:
    print ("too young")

###########################################
# simple while loop to count to 5
current_numer = 1
while current_numer <=5:
    print (current_numer)
    current_numer += 1

###########################################
# parrot: repeating until user types "quit"
# while loop and input
message=""
while message != "quit":
    # prompt must be in while loop, otherwise program repeats message infinitely
    message = input("I'm a parrot and repeat what you say, until you say 'quit'!\n")
    # only print, if input is not "quit", otherwise i repeat "quit" before stopping
    if message != "quit":
        print (message)
