import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
#def f(x):
    #return x**3       # sample function
n = 50 #num of points per cluster
n_clusters = 4
xlist = [2, 3, 4, 1]
ylist = [1, 2, 3, 0]
#pairs = [[x, y] for x, y in zip(xlist, ylist)]
#Modfied code version below on 4/26/21
xC_list = []
yC_list = []
sigma = .7
point_coords = np.zeros((n_clusters * n, 2))
orig_cluster = np.zeros(n_clusters * n)
for i in range (0, n_clusters):
    for j in range (0, n):
           k = i * n + j
           delta_x = (np.random.rand()*2 - 1) * sigma
           delta_y = (np.random.rand()*2 - 1) * sigma
           x = xlist[i]+delta_x
           y = ylist[i]+delta_y
           point_coords[k, 0] = x 
           point_coords[k, 1] = y
           xC_list = np.concatenate([xC_list,[x]])
           yC_list = np.concatenate([yC_list,[y]])
           orig_cluster[k] =  i      
X = point_coords
kmeans = KMeans(n_clusters=4, random_state=0).fit(X)
kmeans.fit(point_coords)
Y = kmeans.predict([[0, 0], [12, 3]])
Z = kmeans.cluster_centers_
print(Z)
print(Y)
fte_colors = {
    0: "#008fd5",
    1: "#fc4f30",
    2: "#FFE873",
    3: "#646464",
    }
km_colors = [fte_colors[label] for label in kmeans.labels_]
predict_cluster = kmeans.labels_ 
print(predict_cluster)
print(orig_cluster)

#if predict_cluster[0:3] == [3 3 3 3]:
    #print("true") 
    #else:
        #print("false")
    
    #if sum(predict_cluster[0:4]) / len(predict_cluster[0:4]) == 3:
        #print("true")
    #else:
        #print("false")

#create a loop that pulls from one array and checks against elements in another array 
#if, else statement

plt.scatter(xC_list, yC_list, c=km_colors)
plt.show()