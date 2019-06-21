###########################################
# Book "Python Crash course" - Eric Matthes
# Chapter 8: Functions
###########################################

###########################################
# print a greeting
# not sure when i need str()
def greeting(name):
    print ("Hi, "+ str(name).title())
    print ("Hi, "+ str(name.title()))
    print ("Hi, "+ name.title())    

greeting ("andi")


###########################################
# keyword arguments, default values
def pets (pet_name, pet_type = "dog"):
    print (pet_name.title() + " is my " + pet_type + ".")

pets ("Barko")
pets ("Hops", "hamster")
pets (pet_type = "hamster", pet_name = "Hops" )

###########################################
# return value
def calculate(a):
    b = a
    c = a * a
    return b,c
    
print (calculate(5))

