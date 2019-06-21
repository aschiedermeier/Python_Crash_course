###########################################
# Book "Python Crash course" - Eric Matthes
# Chapter 8: Functions
###########################################

###########################################
# ask for name, format with function
# while loop, input, break to avoid infinite loop

def format_name(first_name,last_name):
    """ ask for name and greet that person """
    full_name = first_name + " " + last_name
    return full_name.title()

print(format_name("a","b"))

while True:
    print ("Who are you?")
    print ("Enter 'q' to quit.")
    
    f_name = input("First name: ")
    if f_name == "q":
        break
    l_name = input ("Last name: ")
    if f_name == "q":
        break
    
    print ("Hello, " + format_name(f_name,l_name) + " !\n")

###########################################
# print a greeting for a list
# function with list
def greet_users(names):
    """ print a greeting for each user"""
    for name in names:
        print ("Hi, "+ name.title())    

users = ["andi","berta","chris"]
greet_users (users)

###########################################
# print a greeting for arbitrary number of arguments
# function with *
# use * for arbitrary numbers of arguments 
# values go into tuple, same code as for list 

def greet_users(*names):
    """ print a greeting for each user"""
    for name in names:
        print ("Hi, "+ name.title())    

greet_users ("andi","berta","chris")

###########################################
# print a greeting for arbitrary number of arguments
# *args must be at end of function def
def greet_visitors(city, *names):
    """ greet several people from one city """
    print ("Hello to ")
    for name in names:
        print (name.title()+ ", ")    
    print ("from "+ city.title())

greet_visitors ("berlin","andi","berta","chris")