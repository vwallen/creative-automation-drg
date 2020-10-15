import math
from functools import partial


def calculate_extrusion(ln, h, nd, fd, em=1):
    '''
    Returns gcode E value for a particular line

        Parameters:
            ln (float): line length (mm)
            h  (float): line height (mm)
            nd (float): nozzle diameter (mm)
            fd (float): filament diameter (mm)
            em (float): extrusion multiplier

        Returns:
            E value (float): E value to use for G1 command
    '''
    return (h * nd * em * ln) / ((math.pi/4) * fd**2)


def calculate_extrusion_xy(x, y, h, nd, fd, em=1):
    '''
    Returns gcode E value for a particular line projected from x and y coordinates

        Parameters:
            x (float): x distance of G1 command (mm)
            y (float): y distance of G1 command (mm)
            h  (float): line height (mm)
            nd (float): nozzle diameter (mm)
            fd (float): filament diameter (mm)
            em (float): extrusion multiplier

        Returns:
            E value (float): E value to use for G1 command
    '''
    ln = math.sqrt(x**2 + y**2)
    return calculate_extrusion(ln, h, nd, fd, em)

# Shortcuts for my current setup:
E = partial(calculate_extrusion, h=0.28, nd=0.4, fd=1.75, em=1)
Exy = partial(calculate_extrusion_xy, h=0.28, nd=0.4, fd=1.75, em=1)

# Or use this constant (per mm of travel):
E_MULTIPLIER = E(1)