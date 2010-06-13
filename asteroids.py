# System Modules


# Third Party Modules
import pyglet
from pyglet.gl import *

# Local Modules
import settings
import player
import camera as _cam
import asteroid
import universe as _verse
import interface

window = pyglet.window.Window(
    settings.WINDOW_WIDTH,
    settings.WINDOW_HEIGHT)

camera = _cam.Camera(window, 0, 0, 0, settings.CAMERA_ZOOM)
universe = _verse.Universe()
player = player.Player()
hud = interface.Hud(window)

universe.append(player)
universe.append(asteroid.Asteroid(3,4))
universe.append(asteroid.SmallAsteroid(3,4))
universe.append(asteroid.LargeAsteroid(3,4))

@window.event
def on_draw():
    camera.world_projection()
    universe.draw()
    
    #camera.hud_projection()
    #hud.draw()
    
    window.flip()

if __name__ == "__main__":
    pyglet.clock.schedule_interval(universe.update, settings.STEP_INTERVAL)
    window.push_handlers(player.key_handler)
    pyglet.app.run()

