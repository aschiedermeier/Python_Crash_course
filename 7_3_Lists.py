###########################################
# Book "Python Crash course" - Eric Matthes
# Chapter 7: User input and while loops
###########################################

###########################################
# move from one list to another
# pop, append
unconfirmed = ["a","b","c"]
print (unconfirmed)
confirmed =[]
while unconfirmed:
    current = unconfirmed.pop()
    print ("Verifying: " + current.title())
    confirmed.append(current)

for user in confirmed:
    print ("Verified user: " + user.title())

###########################################
# fill dictionary with user input
# flag, input, 
cities = {}
active = True
while active:
    name = input("Who are you?\n")
    city = input("where do you live?\n")
    # here the list gets filled
    cities[name]=city
    repeat = input("Anyone else? y/n\n")
    if repeat == "n":
        active = False
for name,city in cities.items():
    print (name.title() + " from " + city.title())