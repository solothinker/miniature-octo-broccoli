#https://math.stackexchange.com/questions/638225/understanding-the-equation-of-a-m%C3%B6bius-strip

import matplotlib.pyplot as plt 
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams["figure.figsize"] = (10,10)

N = 1000
H = 100
R = 10

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

t = np.linspace(0,2*np.pi,N).reshape(N,1) 
s = np.linspace(-1,1,H).reshape(H,1)
x = R*np.cos(t)+np.outer(np.sin(t/2)*np.cos(t),s)
y = R*np.sin(t)+np.outer(np.sin(t/2)*np.sin(t),s)
z = np.outer(np.cos(t/2),s)

ax.plot_surface(x, y, z, cmap=plt.get_cmap('rainbow'))
plt.title('Möbius Strip')
plt.show()
