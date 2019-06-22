###########################################
# Book "Python Crash course" - Eric Matthes
# Chapter 10: Files and Exceptions
###########################################

###########################################
# open file and print file
filename = "pi_digits.txt"
with open(filename) as file_object:
    contents = file_object.read()
    print (contents.rstrip())

###########################################
# open file and print file line by line
filename = "pi_digits.txt"
with open(filename) as file_object:
    for line in file_object:
        print (line.rstrip())

###########################################
# open file, store each line in list and print list
filename = "pi_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print (line.rstrip())

###########################################
# open file, store each line in list and print list
filename = "pi_million_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()
#print 100 digits
print (pi_string[:100])
print(len(pi_string))


###########################################
# is your birthday in pi?
filename = "pi_million_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print ("Your birthday appears in the first million digits of pi.")
else:
    print ("Your birthday does not appear in the first million digits of pi.")


