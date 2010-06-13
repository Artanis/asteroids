# System Modules
import math

# Third-party Modules


# Local Modules
import settings

def poly_circle(radius=1, step=36, include_origin=False):
    """ Generate points composing a circle of given radius and
    precision.
    
    """
    
    if include_origin is True:
        yield (0, 0)
    
    for angle in range(0,360,step):
        radian = math.radians(angle)
        yield (math.sin(radian) * radius, math.cos(radian) * radius)

def toroidal_space(x, y):
    ratio = settings.WINDOW_WIDTH / settings.WINDOW_HEIGHT
    
    min_x = -settings.CAMERA_ZOOM * ratio
    min_y = -settings.CAMERA_ZOOM
    max_x = settings.CAMERA_ZOOM * ratio
    max_y = settings.CAMERA_ZOOM
    
    new_x = x
    new_y = y
    
    if x < min_x:
        new_x = max_x
    if x > max_x:
        new_x = min_x
    if y < min_y:
        new_y = max_y
    if y > max_y:
        new_y = min_y
    
    return (new_x, new_y)
