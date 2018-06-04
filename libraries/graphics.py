"""
graphics.py

Author:         Josh Kerber
Date:           1 June 2018
Description:    Custom graphics library for simulation
"""

import matplotlib.pyplot as pyplot
from mpl_toolkits.mplot3d import Axes3D
import numpy

#set display of axis
AXIS = Axes3D(pyplot.figure())
AXIS.minorticks_on()
AXIS.tick_params(axis='both', which='minor', length=5, width=2, labelsize=15)
AXIS.tick_params(axis='both', which='major', length=8, width=2, labelsize=15)

# set window title
FIGURE = pyplot.gcf()
FIGURE.canvas.set_window_title('Simulation: Smoke in the Corner of a Room')

def setPlot(coordsX, coordsY, coordsZ, title):
    """plot the smoke in the room on a 3D graph"""
    global AXIS

    # clear previous data
    pyplot.cla()

    # set limits of axis
    AXIS.set_xlim(0,100)
    AXIS.set_ylim(0,100)
    AXIS.set_zlim(0,100)

    # plot data
    x = numpy.array(coordsX)
    y = numpy.array(coordsY)
    z = numpy.array(coordsZ)
    AXIS.plot(x, y, z, 'ok')

    # set title and pause graphics
    pyplot.title(title)
    pyplot.pause(0.01)

def showPlot():
    pyplot.show()
