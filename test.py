"""
    A simple, time-varying vector field plot.

    u(x,y,z,t) represents the i-th component of the vector,
    v(x,y,z,t) represents the j-th component of the vector,
    w(x,y,z,t) represents the k-th component of the vector,
    thus,

        V(x,y,z,t) = u(x,y,z,t)i + v(x,y,z,t)j + w(x,y,z,t)k,

    where i, j, k are the unit vectors to the xyz coordinate system.
"""

from plot import Figure
from vectorfield import *
import numpy as np

def u(x,y,z,t):
    return 0*x
def v(x,y,z,t):
    return 0.1*np.sin(t + x)
def w(x,y,z,t):
    return 0*x

fig = Figure(800, 800)
fig.add(VectorFieldT(u, v, w, 4, 0, 2*np.pi, 0.05))
fig.show()
