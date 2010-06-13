# System Modules


# Third Party Modules
import pyglet
from pyglet.gl import *

# Local Modules
import mobile
import utils

class Ship(mobile.Impulser, mobile.Drifter):
    def __init__(self):
        mobile.Drifter.__init__(self, 0.0, 0.0)
        mobile.Impulser.__init__(self)
        self.x = 0.0
        self.y = 0.0
        self.rotation = 0.0
        self.velocity_vector = (0, 0)
        self.rotation_vector = 0
    
    def step(self):
        pass
    
    def draw(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(self.x, self.y, 0.0)
        glRotatef(self.rotation, 0, 0, 1)
        glScalef(0.02, 0.02, 1.0)
        
        glBegin(GL_LINE_LOOP)
        glColor4f(1.0, 1.0, 1.0, 1.0)
        glVertex2f(0.0, 20.0)
        glVertex2f(7.5, -10.0)
        glVertex2f(-7.5, -10.0)
        glEnd()
        
        self.debug()

