###########################################
# Book "Python Crash course" - Eric Matthes
# Chapter 8: Functions
###########################################

###########################################
# print a greeting
# the str() is needed if someones's name is a number
def greeting(name):
    """ simple greeting """
    print ("Hi, "+ str(name).title())
    print ("Hi, "+ str(name.title()))
    print ("Hi, "+ name.title())    

greeting ("andi")


###########################################
# keyword arguments, default values
def pets (pet_name, pet_type = "dog"):
    """ returns pet name and type """
    print (pet_name.title() + " is my " + pet_type + ".")

pets ("Barko")
pets ("Hops", "hamster")
pets (pet_type = "hamster", pet_name = "Hops" )

###########################################
# return value
def calculate(a):
    """ calcualtion function """
    b = a
    c = a * a
    return b,c
    
print (calculate(5))

