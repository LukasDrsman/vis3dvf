import numpy as np
import OpenGL.GL as gl
import OpenGL.GLU as glu

class VectorField:
    def __init__(self, u, v, w, d, sf):

        space = np.linspace(-0.5,0.5,d)
        x, y, z = np.meshgrid(space, space, space)

        self.u = u(x*sf, y*sf, z*sf)
        self.v = v(x*sf, y*sf, z*sf)
        self.w = w(x*sf, y*sf, z*sf)
        self.m = np.sqrt(self.u**2 + self.v**2 + self.w**2)
        self.m = self.m / np.max(self.m)
        self.x = x
        self.y = y
        self.z = z

    def render(self):
        gl.glLineWidth(2.0)
        gl.glBegin(gl.GL_LINES)
        for i in range(self.x.shape[0]):
            for j in range(self.x.shape[1]):
                for k in range(self.x.shape[2]):
                    gl.glColor3f(self.m[i,j,k], 0.5, 1 - self.m[i,j,k])
                    gl.glVertex3f(self.x[i,j,k], self.y[i,j,k], self.z[i,j,k])
                    gl.glVertex3f(self.x[i,j,k] + self.u[i,j,k], self.y[i,j,k] + self.v[i,j,k], self.z[i,j,k] + self.w[i,j,k])
        gl.glEnd()

        gl.glPointSize(4.0)
        gl.glBegin(gl.GL_POINTS)
        for i in range(self.x.shape[0]):
            for j in range(self.x.shape[1]):
                for k in range(self.x.shape[2]):
                    gl.glColor3f(self.m[i,j,k], 0.5, 1 - self.m[i,j,k])
                    gl.glVertex3f(self.x[i,j,k] + self.u[i,j,k], self.y[i,j,k] + self.v[i,j,k], self.z[i,j,k] + self.w[i,j,k])

        gl.glEnd()

class VectorFieldT:
    def __init__(self, u, v, w, d, ti, tf, dt, sf):

        space = np.linspace(-0.5,0.5,d)
        x, y, z = np.meshgrid(space, space, space)

        self.u = u
        self.v = v
        self.w = w

        self.x = x
        self.y = y
        self.z = z

        self.sf = sf

        self.t = ti
        self.T = (ti, tf, dt)

    def render(self):
        u = self.u(self.x*self.sf, self.y*self.sf, self.z*self.sf, self.t)
        v = self.v(self.x*self.sf, self.y*self.sf, self.z*self.sf, self.t)
        w = self.w(self.x*self.sf, self.y*self.sf, self.z*self.sf, self.t)
        m = np.sqrt(u**2 + v**2 + w**2)
        if np.max(m) != 0:
            m = m / np.max(m)

        gl.glLineWidth(2.0)
        gl.glBegin(gl.GL_LINES)
        for i in range(self.x.shape[0]):
            for j in range(self.x.shape[1]):
                for k in range(self.x.shape[2]):
                    gl.glColor3f(m[i,j,k], 0.5, 1 - m[i,j,k])
                    gl.glVertex3f(self.x[i,j,k], self.y[i,j,k], self.z[i,j,k])
                    gl.glVertex3f(self.x[i,j,k] + u[i,j,k], self.y[i,j,k] + v[i,j,k], self.z[i,j,k] + w[i,j,k])
        gl.glEnd()

        gl.glPointSize(4.0)
        gl.glBegin(gl.GL_POINTS)
        for i in range(self.x.shape[0]):
            for j in range(self.x.shape[1]):
                for k in range(self.x.shape[2]):
                    gl.glColor3f(m[i,j,k], 0.5, 1 - m[i,j,k])
                    gl.glVertex3f(self.x[i,j,k] + u[i,j,k], self.y[i,j,k] + v[i,j,k], self.z[i,j,k] + w[i,j,k])

        gl.glEnd()

        if self.t < self.T[1]:
            self.t += self.T[2]
        else:
            self.t = self.T[0]
