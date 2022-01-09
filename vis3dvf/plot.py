import pygame as pg
import pygame.locals as pgl
import numpy as np
import OpenGL.GL as gl
import OpenGL.GLU as glu

class Figure:
    def __init__(self, width, height, pltname="VF plot"):
        self.display = (width, height)
        self.plots = []
        self.pltname = pltname

    def rotate(self, rot = (0.0, 0.0, 0.0)):
        gl.glRotate(rot[0], 1, 0, 0)
        gl.glRotate(rot[1], 0, 1, 0)
        gl.glRotate(rot[2], 0, 0, 1)

    def axes(self):
        gl.glLineWidth(2.0)
        gl.glBegin(gl.GL_LINES)

        # x-axis
        gl.glColor3f(235/255, 59/255, 59/255)
        gl.glVertex3f(0.0, 0.0, 0.0)
        gl.glVertex3f(0.2, 0.0, 0.0)

        # y-axis
        gl.glColor3f(145/255, 212/255, 97/255)
        gl.glVertex3f(0.0, 0.0, 0.0)
        gl.glVertex3f(0.0, 0.2, 0.0)

        # z-axis
        gl.glColor3f(147/255, 95/255, 184/255)
        gl.glVertex3f(0.0, 0.0, 0.0)
        gl.glVertex3f(0.0, 0.0, 0.2)

        gl.glEnd()

    def add(self, plot):
        self.plots.append(plot)

    def show(self):
        pg.init()
        pg.display.set_caption(self.pltname)
        pg.display.set_mode(self.display, pgl.DOUBLEBUF | pgl.OPENGL)
        gl.glOrtho(-1, 1, -1, 1, -100, 100)

        gl.glEnable(gl.GL_DEPTH_TEST);

        self.crot = [0, 0, 0]
        self.rotate(self.crot)
        rdrag = False
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

                elif event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        rdrag = True
                        rx, ry = event.pos

                elif event.type == pg.MOUSEBUTTONUP:
                    if event.button == 1:
                        rdrag = False

                elif event.type == pg.MOUSEMOTION:
                    if rdrag:
                        nx, ny = event.pos
                        dx, dy = (nx - rx, ny - ry)
                        self.crot[1] += dx/500

                        a, b, c = self.crot
                        self.rotate((0, dx/500, 0))

                        cz = np.sin(np.radians(b)) * (dy/500)
                        cx = np.cos(np.radians(b)) * (dy/500)
                        self.rotate((cx, 0, cz))
                        self.crot = [a + cx, b, c + cz]

            gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
            self.axes()
            for plot in self.plots:
                plot.render()
            pg.display.flip()
            pg.time.wait(10)
