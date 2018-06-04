"""
Philosophy of Time & Time Travel, Final Project

Author:         Josh Kerber
Date:           2 June 2018
Description:    Smoke in corner of the room, a simulation
"""

import random
from packages.graphics import *
from objects.SmokeParticle import SmokeParticle
from objects.Room import Room

# instantiate simulation
room = Room()
room.runSim()

# determine how many particles are in corner
inCorner = 0
for index in room.particles:
    particle = room.particles[index]
    if particle.isInCorner():
        inCorner += 1
print(inCorner, 'in corner')
showPlot()
