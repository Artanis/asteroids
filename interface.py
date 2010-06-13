# System Modules


# Third Party Modules
import pyglet
from pyglet.gl import *

# Local Modules

class Hud(object):
    def __init__(self, window):
        self.window = window
    
    def draw(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
        glBegin(GL_LINE_LOOP)
        glColor4f(1.0, 1.0, 1.0, 1.0)
        glVertex2f(self.window.height-50, self.window.width-50)
        glVertex2f(self.window.height-50, 50)
        glVertex2f(50, 50)
        glVertex2f(50, self.window.width-50)
        glEnd()

