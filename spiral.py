import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

# Create a spiral
t = np.linspace(0, 10 * np.pi, 1000)  # parameter t to create spiral
x = t * np.cos(t)  # x coordinates
y = t * np.sin(t)  # y coordinates
z = t  # z coordinates

# Convert to list of tuples for PyOpenGL
spiral = list(zip(x, y, z))

def Spiral():
    glBegin(GL_LINE_STRIP)
    for vertex in spiral:
        glVertex3fv(vertex)
    glEnd()

def main():
    pygame.init()
    display = (600, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(90, (display[0] / display[1]), 0.01, 500.0)
    glTranslatef(0.0, 0.0, -75)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 15)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Spiral()
        pygame.display.flip()
        pygame.time.wait(10)

main()

