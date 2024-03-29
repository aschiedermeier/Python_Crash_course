###########################################
# Book "Python Crash course" - Eric Matthes
# Chapter 15: Generating Data
###########################################

###########################################
# Rolling two  Dice and visualize with Pygal
# Histogram

from random import randint
import pygal 

class Die():
    """A class representing a single die."""

    def __init__(self,num_sides=6):
        """Assume a six-sided die."""
        self.num_sides=num_sides

    def roll(self):
        """Returning a random value between 1 and number of sides."""
        return randint(1,self.num_sides)

# from die import Die # if Die class in other module

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# Visualize the results.
hist = pygal.Bar()

hist.title ="Results of rolling two D6 1000 times."
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6',frequencies)
hist.render_to_file("die_visual.svg")
