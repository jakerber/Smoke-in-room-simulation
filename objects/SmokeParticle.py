"""
SmokeParticle.py

Author:         Josh Kerber
Date:           1 June 2018
Description:    Smoke particle class
"""

import sys

# import sim constants
sys.path.append('..')
import libraries.constants as constants
import libraries.graphics as graphics

class SmokeParticle:
    """single smoke particle object"""

    def __init__(self):
        self.index = 0

        # current location
        self.coordX = None
        self.coordY = None
        self.coordZ = None

        # current velocities (m/s)
        self.velX = 0.01
        self.velY = 0.01
        self.velZ = 0.01

    def roundCoords(self):
        """round coordinates to decimal place"""
        self.coordX = round(self.coordX, constants.DISTANCE_DIGITS)
        self.coordY = round(self.coordY, constants.DISTANCE_DIGITS)
        self.coordZ = round(self.coordZ, constants.DISTANCE_DIGITS)

    def isInCorner(self):
        """determine if particle is in corner of room"""
        return self.coordX < constants.MAX_DISTANCE_CORNER and self.coordY < constants.MAX_DISTANCE_CORNER and self.coordZ < constants.MAX_DISTANCE_CORNER

    def getCoordString(self):
        """get coordinates of particle as string"""
        return str([self.coordX, self.coordY, self.coordZ])

    def __str__(self):
        """string representation of object"""
        coords = 'coordinates=' + str([self.coordX, self.coordY, self.coordZ])
        vel = 'velocities=' + str([self.velX, self.velY, self.velZ])
        return '{0:<30} {1:<30}'.format(coords, vel)
