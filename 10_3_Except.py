###########################################
# Book "Python Crash course" - Eric Matthes
# Chapter 10: Files and Exceptions
###########################################

###########################################
# try except block
try: 
    print (5/0)
except ZeroDivisionError:
    print ("You can't divide by zero!")

###########################################
# try except else block
try: 
    a = 5/0
except ZeroDivisionError:
    print ("You can't divide by zero!")
else:
    print(a)
