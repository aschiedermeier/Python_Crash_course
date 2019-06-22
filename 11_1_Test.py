###########################################
# Book "Python Crash course" - Eric Matthes
# Chapter 11: Testing your Code
###########################################

###########################################
# calling the name_function from another module
# name function also has a test function
from name_function import get_formatted_name

print ("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == "q":
        break
    last = input("\nPlease give me a last name: ")
    if last == "q":
        break
        
    formatted_name = get_formatted_name(first,last)
    print("\nNeatly formatted name: " + formatted_name + ".")