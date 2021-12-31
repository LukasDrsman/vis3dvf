import numpy as np
import OpenGL.GL as gl
import OpenGL.GLU as glu

class VectorFieldC:
    def __init__(self, u, v, w, d, dz):

        space = np.linspace(-0.5,0.5,d)
        x, y, z = np.meshgrid(space, space, np.linspace(-dz,dz,d))

        self.u = u(x, y, z)
        self.v = v(x, y, z)
        self.w = w(x, y, z)
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

class VectorFieldCH:
    def __init__(self, u, v, w, d):

        space = np.linspace(-0.5,0.5,d)
        x, y, z = np.meshgrid(space, space, space)

        self.u = u(x, y, z)
        self.v = v(x, y, z)
        self.w = w(x, y, z)
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
