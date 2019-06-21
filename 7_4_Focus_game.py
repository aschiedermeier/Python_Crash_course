###########################################
# Book "Python Crash course" - Eric Matthes
# Chapter 7: User input and while loops
###########################################


###########################################
# Focus game: repeat the given number
# program stores success rate in list
# flag, list, number formating

import random as rn
active = True
rate = []
while active:
    a = rn.randint(1,2)
    tag = input ("Repeat this number: 'q' to quit\n" + str(a))
    if tag == "q":
        active = False
    else:
        tag = int (tag)
        if tag == a:
            rate.append(1)
        else:
            rate.append(0)
        
success_rate = sum(rate)/len(rate) *100
print("After " + str(len(rate)) + " tries, you have a " + '{0:.0f}'.format(success_rate) + "% success rate!\n")


