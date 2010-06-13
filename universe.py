# System Modules


# Third Party Modules
import pyglet
from pyglet.gl import *

# Local Modules


class Universe(list):
    """ In mathematics, and particularly in set theory and the
    foundations of mathematics, a universe is a class that contains (as
    elements) all the entities one wishes to consider in a given
    situation.
    
    http://en.wikipedia.org/wiki/Universe_(mathematics)
    
    """
    
    def update(self, delta_time):
        """ Advance all entities by the given time """
        
        for entity in self:
            entity.update(delta_time)
    
    def draw(self):
        """ Draw all entities """
        
        glClear(GL_COLOR_BUFFER_BIT)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        for entity in self:
            entity.draw()

