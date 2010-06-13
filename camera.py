# System Modules


# Third Party Modules
import pyglet
from pyglet.gl import *

# Local Modules
import settings
import utils

class Camera(object):
    def __init__(self, window, x=0.0, y=0.0, rotation=0.0, zoom=1.0):
        self.x = x
        self.y = y
        self.window = window
        self.rotation = rotation
        self.zoom = zoom
    
    @property
    def ratio(self):
        return self.window.width / self.window.height
    
    def world_projection(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(
            -self.zoom * self.ratio, self.zoom * self.ratio,
            -self.zoom, self.zoom,
            -1, 1)
    
    def hud_projection(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(
            0.0, self.window.height,
            0.0, self.window.width,
            -1, 1)

