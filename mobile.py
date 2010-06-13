# System Modules
import math
import random

# Third-party Modules
import pyglet
from pyglet.gl import *

# Local Modules
import settings
import utils

class Drifter(object):
    """ An object that drifts with no forces acting on it.
    
    """
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.rotation = random.randint(0, 360)
        self.velocity_vector = ((random.random()-0.5) * 10, (random.random()-0.5) * 10)
        self.rotation_vector = random.randint(-90, 90)
    
    def debug(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(self.x, self.y, 0.0)
        v_x, v_y = self.velocity_vector
        
        glBegin(GL_LINES)
        glColor4f(1.0, 0.0, 0.0, 0.5)
        glVertex2f(0.0, 0.0)
        glVertex2f(v_x*1, v_y*1)
        glEnd()
    
    def update(self, delta_time):
        """ Update the position and rotation of the drifting object
        
        """
        
        v_x, v_y = self.velocity_vector
        
        self.x, self.y = utils.toroidal_space(
            self.x + (v_x * delta_time),
            self.y + (v_y * delta_time))
        
        self.rotation = self.rotation + (self.rotation_vector * delta_time)
    
    def draw(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(self.x, self.y, 0.0)
        glRotatef(self.rotation, 0, 0, 1)
        
        glBegin(GL_LINE_LOOP)
        glColor4f(1.0, 1.0, 1.0, 1.0)
        for x, y in utils.poly_circle(0.1, 36):
            glVertex2f(x, y)
        glEnd()

class Impulser(object):
    """ An object with a thruster layout.
    
    This class only modifies the velocity and rotational vectors. Pair
    it with Drifter for drifting after thrusters cease.
    
    """
    
    def __init__(self, main=25.0, retro=15.0, vernier=10.0):
        self.main = main
        self.retro = retro
        self.vernier = vernier
    
    def stabilize(self, delta_time):
        if self.rotation_vector > 0:
            self.port_thruster(delta_time)
        if self.rotation_vector < 0:
            self.starboard_thruster(delta_time)
    
    def main_thruster(self, delta_time):
        radian = math.radians(self.rotation+90)
        force_x = math.cos(radian) * self.main * delta_time
        force_y = math.sin(radian) * self.main * delta_time
        v_x, v_y = self.velocity_vector
        self.velocity_vector = (v_x + force_x, v_y + force_y)
    
    def retro_thruster(self, delta_time):
        radian = math.radians(self.rotation-90)
        force_x = math.cos(radian) * self.main * delta_time
        force_y = math.sin(radian) * self.main * delta_time
        v_x, v_y = self.velocity_vector
        self.velocity_vector = (v_x + force_x, v_y + force_y)
    
    def port_thruster(self, delta_time):
        self.rotation_vector = self.rotation_vector - self.vernier
    
    def starboard_thruster(self, delta_time):
        self.rotation_vector = self.rotation_vector + self.vernier

