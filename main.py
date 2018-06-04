"""
Philosophy of Time & Time Travel, Final Project

Author:         Josh Kerber
Date:           2 June 2018
Description:    Smoke in corner of the room, a simulation
"""

import random

# import all objects and custom libraries
from libraries.constants import *
from libraries.graphics import *
from objects.SmokeParticle import SmokeParticle
from objects.Room import Room

# instantiate room
room = Room()

# simulate smoke particles moving through the room
for ms in range(NUM_MILLISECONDS + 1):
    for index in room.particles:
        room.moveParticle(index)    # execute move

    # plot graphics every 100th move
    if ms % 100 == 0:
        print('time={} milliseconds'.format(ms))
        room.plot('{} seconds elapsed'.format(str(ms / 1000), NUM_MILLISECONDS))
room.plot('{} seconds elapsed – end of simulation'.format(NUM_MILLISECONDS / 1000))

# determine how many particles are in corner
inCorner = 0
for index in room.particles:
    particle = room.particles[index]
    if particle.isInCorner():
        inCorner += 1
print(inCorner, 'in corner')
showPlot()
