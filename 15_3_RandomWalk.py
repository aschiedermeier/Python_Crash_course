###########################################
# Book "Python Crash course" - Eric Matthes
# Chapter 15: Generating Data
###########################################

###########################################
# Random walk

from random import choice

class RandomWalk():
    """ A class to generate random walks. """
    
    def __init__(self,num_points=5000):
        """Initialize attributes of a walk"""
        self.num_points=num_points

        # All walks start at (0,0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far to go in that direction.
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance
            
            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)



import matplotlib.pyplot as plt

# from random_walk import RandomWalk # if class is in other module

# Make a random walk and plot the points
rw= RandomWalk(50000)
rw.fill_walk()

point_numbers=list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values,c=point_numbers, cmap=plt.cm.Blues,edgecolor="none", s=1)

# Emphasize the first and last points.
plt.scatter (0,0,c="green", edgecolors ="none", s = 10)
plt.scatter (rw.x_values[-1],rw.y_values[-1], c="red", edgecolors ="none", s = 10)

# Remove the axis.
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()

##########################################
"""
simple scatter graph using matplotlib
import matplotlib.pyplot as plt
x_values=list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,c="red", edgecolor="none",s=40)
plt.scatter(x_values,y_values,c=(0,0,0.8), edgecolor="none",s=40) # RGB colors
plt.scatter(x_values,y_values,c=y_values, cmap=plt.cm.Blues, edgecolor="none",s=40) # colormap

Set chart title and label axes.
plt.title("Square Numbers",fontsize = 24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value", fontsize = 14)

Set size of tick labels.
plt.tick_params(axis='both', which = "major", labelsize=14)

Set the range for each axis.
plt.axis([0,1100,0,1100000])
plt.savefig("squares_plot.png",bbox_inches="tight") # save plot to file
plt.show()
"""