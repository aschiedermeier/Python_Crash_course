###########################################
# Book "Python Crash course" - Eric Matthes
# Chapter 11: Testing your Code
###########################################

###########################################
# name_function
# is tested by test_name_function

def get_formatted_name(first,last,middle=""):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = first + " " + middle + " " + last
    else:
        full_name = first + " "  + last
    return full_name.title()
    