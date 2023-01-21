import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
from pylab import *
 
# Create axis
axes = [5, 5, 5]
 
# Create Data
data = np.ones(axes, dtype=np.bool_)
 
# Control Transparency
alpha = 0.9
 
# Control colour
colors = np.empty(axes + [4], dtype=np.float32)
 
colors[:] = [1, 1, 1, alpha]  # white
 
# Plot figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.random.randint(low=10,high=50,size=(100,))
y = np.random.randint(low=20,high=50,size=(100,))
z = np.random.randint(low=30,high=50,size=(100,))
colo = np.random.randn(1,10)*1000

color_map= cm.ScalarMappable(cmap=cm.gray)
color_map.set_array(colo)

img = ax.scatter(x,y,z , marker = 'o', s=10, color='black')
plt.colorbar(color_map)
 
# Voxels is used to customizations of the
# sizes, positions and colors.
#ax.voxels(data, facecolors=colors)



plt.show()