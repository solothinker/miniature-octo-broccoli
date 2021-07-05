import numpy as np
import matplotlib.pyplot as plt

rr = np.linspace(2.8,4,5000).tolist()
x=0.4

def logiMap(x,r):
    return x*r*(1-x)

for r in rr:
    x=logiMap(x,r)
    plt.plot(r,x,'.',color='b',markersize=1)
    plt.draw()
    plt.pause(0.0001)


