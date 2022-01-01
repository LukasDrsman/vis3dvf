"""
    A simple, time-varying vector field plot.

    u(x,y,z,t) represents the i-th component of the vector,
    v(x,y,z,t) represents the j-th component of the vector,
    w(x,y,z,t) represents the k-th component of the vector,
    thus,

        V(x,y,z,t) = u(x,y,z,t)i + v(x,y,z,t)j + w(x,y,z,t)k,

    where i, j, k are the unit vectors to the xyz coordinate system.
"""

# necessary imports
from vis3dvf.plot import Figure
from vis3dvf.vectorfield import *
import numpy as np

# i-th component of the time varying vector field
def u(x,y,z,t):
    return 0*x                                   # function must use at leas one of the x,y,z variables (due to numpy)

# j-th component of the time varying vector field
def v(x,y,z,t):
    return 0.1*np.sin(t + x)

# k-th component of the time varying vector field
def w(x,y,z,t):
    return 0*x                                   # function must use at leas one of the x,y,z variables

# Figure(window width, window height)
fig = Figure(800, 800)

# VectorFieldT(u, v, w, vector density, initial time, final time, time delta)
fig.add(VectorFieldT(u, v, w, 6, 0, 2*np.pi, 0.05))

# Render field
fig.show()
