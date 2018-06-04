"""
Room.py

Author:         Josh Kerber
Date:           1 June 2018
Description:    Room class
"""

import sys
import random

# import custom libraries
sys.path.append('..')
import libraries.constants as constants
import libraries.graphics as graphics

# import smoke particle object
from .SmokeParticle import SmokeParticle

class Room:
    """room object"""

    def __init__(self):
        self.particles = {}     # dictionary mapping particles in room, index -> particle
        self.coordDict = {}     # dictionary mapping occupied coordinates to particles indices

        # generate particles in room
        for index in range(constants.NUM_PARTICLES):
            newParticle = SmokeParticle()       # instantiate new particle
            newParticle.index = index

            # set coordinates and velocities
            newParticle.coordX, newParticle.coordY, newParticle.coordZ = self.getRandomRoomCoordinate(constants.MAX_DISTANCE_CORNER)
            newParticle.velX *= random.uniform(-1, 1)
            newParticle.velY *= random.uniform(-1, 1)
            newParticle.velZ *= random.uniform(-1, 1)

            # store particle in room
            self.particles[newParticle.index] = newParticle
            coordinates = newParticle.getCoordString()
            if coordinates in self.coordDict:
                self.coordDict[coordinates].add(index)
            else:
                self.coordDict[coordinates] = set([index])

    def getRandomRoomCoordinate(self, limit):
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

        # reverse, reduce velocity if collision with inner wall
        if particle.coordX <= 0:
            particle.coordX = 0.0001
            particle.velX *= -1
            particle.velX += -1 * random.uniform(0, 0.025) if particle.velX > 0 else random.uniform(0, 0.025)
        if particle.coordY <= 0:
            particle.coordY = 0.0001
            particle.velY *= -1
            particle.velY += -1 * random.uniform(0, 0.025) if particle.velY > 0 else random.uniform(0, 0.025)
        if particle.coordZ <= 0:
            particle.coordZ = 0.0001
            particle.velZ *= -1
            particle.velZ += -1 * random.uniform(0, 0.025) if particle.velZ > 0 else random.uniform(0, 0.025)

        # reverse, reduce velocity if collision with outer wall
        if particle.coordX >= constants.MAX_DISTANCE_ROOM:
            particle.coordX = constants.MAX_DISTANCE_ROOM - 0.0001
            particle.velX *= -1
            particle.velX += -1 * random.uniform(0, 0.025) if particle.velX > 0 else random.uniform(0, 0.025)
        if particle.coordY >= constants.MAX_DISTANCE_ROOM:
            particle.coordY = constants.MAX_DISTANCE_ROOM - 0.0001
            particle.velY *= -1
            particle.velY += -1 * random.uniform(0, 0.025) if particle.velY > 0 else random.uniform(0, 0.025)
        if particle.coordZ >= constants.MAX_DISTANCE_ROOM:
            particle.coordZ = constants.MAX_DISTANCE_ROOM - 0.0001
            particle.velZ *= -1
            particle.velZ += -1 * random.uniform(0, 0.025) if particle.velZ > 0 else random.uniform(0, 0.025)

        # reverse, reduce velocity if collision with other particle
        newCoordinates = particle.getCoordString()
        if newCoordinates in self.coordDict:
            particle.velX *= -1
            particle.velY *= -1
            particle.velZ *= -1
            particle.velX += -1 * random.uniform(0, 0.025) if particle.velX > 0 else random.uniform(0, 0.025)
            particle.velY += -1 * random.uniform(0, 0.025) if particle.velY > 0 else random.uniform(0, 0.025)
            particle.velZ += -1 * random.uniform(0, 0.025) if particle.velZ > 0 else random.uniform(0, 0.025)

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
        graphics.setPlot(x, y, z, milliseconds)
