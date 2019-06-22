###########################################
# Book "Python Crash course" - Eric Matthes
# Chapter 10: Files and Exceptions
###########################################

###########################################
# Remember user, greet user or ask for name
# refactoring: creating 3 single functions
# write/read json file
# try except else block 

import json

def get_stored_username():
    """Get stored username if available."""
    filename = "username.json"
    try:
        with open (filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Promt for a new username."""
    username = input ("What is your name?")
    filename = "username.json"
    with open (filename,"w") as f_obj:
        json.dump(username,f_obj)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print ("Welcome back, " + username + "!")
    else: 
        username = get_new_username()
        print ("We'll remember you, when you come back, " + username + "!")

greet_user()
