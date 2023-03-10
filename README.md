# Personal-Projects

My name is Mudit Agrawal and I am a current student at Duke University studying Mechanical Engineering, Energy and the Environment and I&E.
This repository includes some of my personal projects that I have worked on so far! 

# Energy Model
This is a model of an Electric Water Heater that I created. The code defines a function called water_heater_power that takes in an array of water usage data, represented in liters per second. The function first initializes two arrays: T_array, which will store the water temperature in the heater over time, and heater_power, which will store the power output of the water heater at each time step. The initial value of T_array is set to the thermostat temperature.

The function then iterates through the water usage data, using a series of equations to calculate the temperature and power output of the water heater at each time step. The power output is constrained to a maximum value of 3000 W, and the water temperature is constrained to not exceed the thermostat temperature. The final values of the two arrays are then returned in a dictionary.

To view the visuals, see the heaterpower.png and temperature.png graphs on the main page! These show the graphs produced for the heater power required over time over a 24 hour interval given some water usage array, and the temperature over time of the water coming out of the water heater over a 24 hour interval.

# Clustering Algorithm using K_Means

The code begins by importing several libraries, including numpy, matplotlib, and sklearn.cluster. It then defines a number of variables and lists, including the number of points per cluster (n), the number of clusters (n_clusters), the coordinates for the centers of the clusters (xlist and ylist), and the standard deviation of the Gaussian distribution (sigma).

Next, the code generates a set of points by sampling from the Gaussian distribution centered at each of the coordinates in xlist and ylist. These points are stored in a 2D array called point_coords, along with their corresponding original cluster labels in the array orig_cluster.

The K-Means model is then fit to the set of points in point_coords. The model is used to predict the cluster labels for the points [0, 0] and [12, 3], which are stored in the variable Y. The centers of the clusters found by the model are also computed and stored in the variable Z.

The predicted cluster labels for each point are then plotted on a graph using matplotlib, with each point colored according to its predicted cluster label. The original and predicted cluster labels are also printed for comparison.
