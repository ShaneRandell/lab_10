import numpy
import matplotlib.pyplot as plt


plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])  #This line declares the range for the x and y axis
plt.ylabel('y')  #define the label for the y axis
plt.xlabel('x')  #define the label for the x axis
plt.axis([0, 4, 0, 16]) #this plots the coordinates of the data
plt.show() #thios is the run function for the graph
