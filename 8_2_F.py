###########################################
# Book "Python Crash course" - Eric Matthes
# Chapter 8: Functions
###########################################

###########################################
# ask for name, format with function
# while loop, input, break to avoid infinite loop

def format_name(first_name,last_name):
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
    
    print ("Hello, " + format_name(f_name,l_name) + " !")
