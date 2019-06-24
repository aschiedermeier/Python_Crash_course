###########################################
# Book "Python Crash course" - Eric Matthes
# Chapter 15: Generating Data
###########################################

###########################################
# super simple scatter graph using matplotlib
# import matplotlib.pyplot as plt
# plt.scatter(2,4)
# plt.show()

# ###########################################
# # simple scatter graph using matplotlib
# import matplotlib.pyplot as plt
# x_values=[1,2,3,4,5]
# y_values = [1,4,9,16,25]
# plt.scatter(x_values,y_values,s=50)

# # Set chart title and label axes.
# plt.title("Square Numbers",fontsize = 24)
# plt.xlabel("Value",fontsize=14)
# plt.ylabel("Square of Value", fontsize = 14)

# # Set size of tick labels.
# plt.tick_params(axis='both', which = "major", labelsize=14)

# plt.show()

###########################################
# simple scatter graph using matplotlib
import matplotlib.pyplot as plt
x_values=list(range(1,1001))
y_values = [x**2 for x in x_values]
# plt.scatter(x_values,y_values,c="red", edgecolor="none",s=40)
# plt.scatter(x_values,y_values,c=(0,0,0.8), edgecolor="none",s=40) # RGB colors
plt.scatter(x_values,y_values,c=y_values, cmap=plt.cm.Blues, edgecolor="none",s=40) # colormap

# Set chart title and label axes.
plt.title("Square Numbers",fontsize = 24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value", fontsize = 14)

# Set size of tick labels.
plt.tick_params(axis='both', which = "major", labelsize=14)

# Set the range for each axis.
plt.axis([0,1100,0,1100000])
# plt.savefig("squares_plot.png",bbox_inches="tight") # save plot to file
plt.show()