"""
    A simple vector field plot.

    u(x,y,z) represents the i-th component of the vector,
    v(x,y,z) represents the j-th component of the vector,
    w(x,y,z) represents the k-th component of the vector,
    thus,
    
        V(x,y,z) = u(x,y,z)i + v(x,y,z)j + w(x,y,z)k,

    where i, j, k are the unit vectors to the xyz coordinate system.
"""

from plot import Figure
from vectorfield import *
import numpy as np

def u(x,y,z):
    return y / 10
def v(x,y,z):
    return (y - x) / 10
def w(x,y,z):
    return 0*z

fig = Figure(800, 800)
fig.add(VectorFieldCH(u, v, w, 5))
fig.show()
