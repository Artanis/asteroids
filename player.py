from pyglet.window import key

import ship

class Player(ship.Ship):
    def __init__(self):
        ship.Ship.__init__(self)
        
        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]
    
    def update(self, delta_time):
        ship.Ship.update(self, delta_time)
        
        if self.key_handler[key.LEFT]:
            # Fire starboard thrusters
            ship.Ship.starboard_thruster(self, delta_time)
        
        if self.key_handler[key.RIGHT]:
            # fire port-side thrusters
            ship.Ship.port_thruster(self, delta_time)
        
        if self.key_handler[key.UP]:
            # fire main thruster
            ship.Ship.main_thruster(self, delta_time)
        
        if self.key_handler[key.DOWN]:
            # fire retro thruster
            ship.Ship.retro_thruster(self, delta_time)
        
        if self.key_handler[key.Z]:
            # stabilize rotation
            ship.Ship.stabilize(self, delta_time)
        
        if self.key_handler[key.SPACE]:
            # shoot
            pass

