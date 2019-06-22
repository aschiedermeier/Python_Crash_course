###########################################
# Book "Python Crash course" - Eric Matthes
# Chapter 10: Files and Exceptions
###########################################

###########################################
# write in json file
import json

numbers =[1,1,2,3,5,8,13,21]

filename = "numbers.json"
with open (filename,"w") as f_obj:
    json.dump(numbers,f_obj)