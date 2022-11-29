# Personal-Projects

My name is Mudit Agrawal and I am a current student at Duke University studying Mechanical Engineering, Energy and the Environment and I&E.
This repository includes some of my personal projects that I have worked on so far! 

# Energy Model
This is a model of an Electric Water Heater that I created that shows two outputs -- temperature over time as a result of desired flow rate, and power required to provide this flow rate to the user. There are a couple of assumptions that I have taken into account with this model that help with the simplification without a detriment to the accuracy as a whole. I incorporated thermodynamic equations and the general premise revolves around the heat balance equation as well as heat equilibrium. The entire model is based around this heat balance equation and on a large level essentially states that Energy In = Energy Out with a lot of intermediate steps. The constants at the top allow the user to experiment with different power limits for the heating element. There is currently a default array corresponding to average or normal water usage over the course of a day in L/s. 

# Clustering Algorithm using K_Means

This is a project I worked on over the summer that takes an input of arrays and points and creates a clustering graph based off of user inputted locations and shapes. It utilizes libraries such as NumPy, matplotlib and others. Essentially, the user is able to input the noise level as a sigma value ranging from 0 - 1, as well as the shape that they want the clusters to take as coordinate values. The output of the code is a graph that shows the visual clusters as well as an array holding k-means values that are useful for clustering and analysis purposes. 
