import numpy as np
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(10000)

delta = 0.001

def logiMap(x,r):
    return x*r*(1-x)

def logisMap(x,r):
    
    if r >= 4:
        return 'Complete'
    
    plt.plot(r,x,'o',color='b',markersize=1)
    plt.draw()
    plt.pause(0.0001)
    r += delta 
    x = logiMap(x,r)
    return logisMap(x,r)


logisMap(0.3,2.8)
