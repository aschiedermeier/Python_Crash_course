###########################################
# Book "Python Crash course" - Eric Matthes
# Chapter 10: Files and Exceptions
###########################################

###########################################
# create and write a file
filename = "test_write.txt"
with open(filename,"w") as file_object:
    file_object.write("File and text written anew every time!\n")
    file_object.write("Programming rocks!\n")

###########################################
# create and append to a file
filename = "test_append.txt"
with open(filename,"a") as file_object:
    file_object.write("Text added every time when exectued!\n")
    file_object.write("Programming rocks!\n")
