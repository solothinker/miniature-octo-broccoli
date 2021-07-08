#ref-https://www.programmersought.com/article/9522403804/
import matplotlib.pyplot as plt 
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
N = 100
H = 50
u = np.linspace(0,2*np.pi,N) 
h = np.linspace(-1,1,H) 
x = np.outer(np.sin(u), np.ones(len(h))) 
y = np.outer(np.cos(u),np.ones(len(h))) 
z = np.outer(np.ones(len(u)),h) 


ax.plot_wireframe(x, y, z)
 
plt.show()
