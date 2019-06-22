###########################################
# Book "Python Crash course" - Eric Matthes
# Chapter 10: Files and Exceptions
###########################################

###########################################
# read from json file
import json

filename = "numbers.json"
with open (filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)