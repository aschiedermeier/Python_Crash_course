###########################################
# Book "Python Crash course" - Eric Matthes
# Chapter 9: Classes
###########################################

###########################################
# Dog class 
# methods for initializing dog instances
# creating 2 dogs and calling theirs methods

class Dog():
    ''' A simple attempt to model a dog '''
    def __init__(self,name,age):
        '''initialize name and age attributes.'''
        self.name=name
        self.age=age
        
    def sit(self):
        '''simulate a dog sitting in response to a command.'''
        print (self.name.title() + " is now sitting.")
        
    def roll_over(self):
        """simulate rolling over in response to a command."""
        print (self.name.title() + " rolled over!")
        
my_dog = Dog("Rex",6)

print ("My dog is called " + my_dog.name + " and is " + str(my_dog.age) + " years old.")
my_dog.roll_over()

your_dog = Dog ("Tracy",3)
print ("\nYour dog is called " + your_dog.name + " and is " + str(your_dog.age) + " years old.")
your_dog.sit()