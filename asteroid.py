# System Modules


# Third-party Modules
import pyglet
from pyglet.gl import *

# Local Modules
import mobile

class Asteroid(mobile.Drifter):
    def draw(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(self.x, self.y, 0.0)
        glRotatef(self.rotation, 0, 0, 1)
        glScalef(0.02, 0.02, 1.0)
        
        glBegin(GL_LINE_LOOP)
        glColor4f(1.0, 1.0, 1.0, 1.0)
        glVertex2f(5.0, 45.0)
        glVertex2f(30.0, 50.0)
        glVertex2f(40.0, 35.0)
        glVertex2f(40.0, -10.0)
        glVertex2f(25.0, -25.0)
        glVertex2f(20.0, -50.0)
        glVertex2f(-5.0, -50.0)
        glVertex2f(-35.0, -30.0)
        glVertex2f(-40.0, -5.0)
        glVertex2f(-30.0, 15.0)
        glVertex2f(-5.0, 20.0)
        glEnd()
        
        self.debug()

class LargeAsteroid(mobile.Drifter):
    def draw(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(self.x, self.y, 0.0)
        glRotatef(self.rotation, 0, 0, 1)
        glScalef(0.02, 0.02, 1.0)
        
        glBegin(GL_LINE_LOOP)
        glColor4f(1.0, 1.0, 1.0, 1.0)
        glVertex2f(30.0, 85.0)
        glVertex2f(55.0, 70.0)
        glVertex2f(60.0, 45.0)
        glVertex2f(70.0, 40.0)
        glVertex2f(80.0, -5.0)
        glVertex2f(65.0, -50.0)
        glVertex2f(35.0, -70.0)
        glVertex2f(20.0, -85.0)
        glVertex2f(-5.0, -70.0)
        glVertex2f(-45.0, -70.0)
        glVertex2f(-80.0, -20.0)
        glVertex2f(-70.0, 20.0)
        glVertex2f(-15.0, 40.0)
        glEnd()
        
        self.debug()

class SmallAsteroid(mobile.Drifter):
    def draw(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(self.x, self.y, 0.0)
        glRotatef(self.rotation, 0, 0, 1)
        glScalef(0.02, 0.02, 1.0)
        
        glBegin(GL_LINE_LOOP)
        glColor4f(1.0, 1.0, 1.0, 1.0)
        glVertex2f(20.0, 10.0)
        glVertex2f(25.0, 0.0)
        glVertex2f(15.0, -5.0)
        glVertex2f(10.0, -15.0)
        glVertex2f(0.0, -10.0)
        glVertex2f(-15.0, -10.0)
        glVertex2f(-25.0, 0.0)
        glVertex2f(-20.0, 10.0)
        glVertex2f(-10.0, 10.0)
        glVertex2f(-5.0, 15.0)
        glEnd()
        
        self.debug()

