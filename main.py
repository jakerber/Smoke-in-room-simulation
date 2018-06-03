"""
Philosophy of Time & Time Travel, Final Project

Author:         Josh Kerber
Date:           2 June 2018
Description:    Smoke in corner of the room, a simulation
"""

import random
from packages.graphics import *
from packages.constants import *
from packages.SmokeParticle import SmokeParticle

class Room:
    """room object"""

    def __init__(self, numParticles=NUM_PARTICLES, cornerDistance=MAX_DISTANCE_CORNER, roomBounds=MAX_DISTANCE_ROOM):
        self.numParticles = numParticles        # number of particles in the room
        self.cornerDistance = cornerDistance    # distance to edge of room corner
        self.roomBounds = roomBounds            # distance to end of room
        self.particles = {}                     # particles in room
        self.coordDict = {}                     # dictionary mapping occupied coordinates to particles

        # generate particles in room
        for index in range(self.numParticles):
            newParticle = SmokeParticle()       # instantiate new particle
            newParticle.index = index

            # set coordinates and velocities
            newParticle.coordX, newParticle.coordY, newParticle.coordZ = self.getRandomRoomCoordinate(self.cornerDistance)
            newParticle.velX *= random.choice([-1, 1])
            newParticle.velY *= random.choice([-1, 1])
            newParticle.velZ *= random.choice([-1, 1])

            # store particle in room
            self.particles[newParticle.index] = newParticle
            coordinates = newParticle.getCoordString()
            if coordinates in self.coordDict:
                self.coordDict[coordinates].add(index)
            else:
                self.coordDict[coordinates] = set([index])

    def getRandomRoomCoordinate(self, limit, digits=DISTANCE_DIGITS):
        """get random x, y, z coordinate in room"""
        x = random.uniform(0, limit)
        y = random.uniform(0, limit)
        z = random.uniform(0, limit)
        return x, y, z

    def moveParticle(self, index):
        """execute a particle move"""
        particle = self.particles[index]
        coordinates = particle.getCoordString()

        # remove old coordinates from dict
        self.coordDict[coordinates].discard(index)
        if len(self.coordDict[coordinates]) == 0:
            del self.coordDict[coordinates]

        # update particle coordinates – actually move the particle
        particle.coordX += particle.velX
        particle.coordY += particle.velY
        particle.coordZ += particle.velZ
        particle.roundCoords()

        # reverse velocity if collision with inner wall
        if particle.coordX <= 0:
            particle.coordX = 0.0001
            particle.velX *= -1
            particle.velX += -1 * random.uniform(0, 0.05) if particle.velX > 0 else random.uniform(0, 0.05)
        if particle.coordY <= 0:
            particle.coordY = 0.0001
            particle.velY *= -1
            particle.velY += -1 * random.uniform(0, 0.05) if particle.velY > 0 else random.uniform(0, 0.05)
        if particle.coordZ <= 0:
            particle.coordZ = 0.0001
            particle.velZ *= -1
            particle.velZ += -1 * random.uniform(0, 0.05) if particle.velZ > 0 else random.uniform(0, 0.05)

        # reverse velocity if collision with outer wall
        if particle.coordX >= self.roomBounds:
            particle.coordX = self.roomBounds - 0.0001
            particle.velX *= -1
            particle.velX += -1 * random.uniform(0, 0.05) if particle.velX > 0 else random.uniform(0, 0.05)
        if particle.coordY >= self.roomBounds:
            particle.coordY = self.roomBounds - 0.0001
            particle.velY *= -1
            particle.velY += -1 * random.uniform(0, 0.05) if particle.velY > 0 else random.uniform(0, 0.05)
        if particle.coordZ >= self.roomBounds:
            particle.coordZ = self.roomBounds - 0.0001
            particle.velZ *= -1
            particle.velZ += -1 * random.uniform(0, 0.05) if particle.velZ > 0 else random.uniform(0, 0.05)

        # reverse velocity if collision with other particle
        newCoordinates = particle.getCoordString()
        if newCoordinates in self.coordDict:
            particle.velX *= -1
            particle.velY *= -1
            particle.velZ *= -1
            particle.velX += -1 * random.uniform(0, 0.05) if particle.velX > 0 else random.uniform(0, 0.05)
            particle.velY += -1 * random.uniform(0, 0.05) if particle.velY > 0 else random.uniform(0, 0.05)
            particle.velZ += -1 * random.uniform(0, 0.05) if particle.velZ > 0 else random.uniform(0, 0.05)

        # store new particle coordinates
        if newCoordinates not in self.coordDict:
            self.coordDict[newCoordinates] = set()
        self.coordDict[newCoordinates].add(index)

    def plot(self, milliseconds):
        """plot the current state of the room"""
        x, y, z = [], [], []
        for index in self.particles:
            particle = self.particles[index]

            # collect coordinates in arrays
            x.append(particle.coordX)
            y.append(particle.coordY)
            z.append(particle.coordZ)

        # call graphics lib to plot
        setPlot(x, y, z, milliseconds)

    def runSim(self):
        """simulate smoke particles moving through a room"""
        for ms in range(NUM_MILLISECONDS + 1):
            for index in self.particles:
                self.moveParticle(index)    # execute move

            # plot graphics every 100th move
            if ms % 100 == 0:
                print('time={} milliseconds'.format(ms))
                self.plot('{}/{} milliseconds'.format(str(ms), NUM_MILLISECONDS))

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
