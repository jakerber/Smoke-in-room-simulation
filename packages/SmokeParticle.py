"""
SmokeParticle.py

Author:         Josh Kerber
Date:           1 June 2018
Description:    Smoke particle class
"""

from .constants import *

class SmokeParticle:
    """single smoke particle object"""

    def __init__(self):
        self.index = 0

        # current location
        self.coordX = None
        self.coordY = None
        self.coordZ = None

        # current velocities (m/s)
        self.velX = 0.02
        self.velY = 0.02
        self.velZ = 0.02

    def roundCoords(self):
        """round coordinates to decimal place"""
        self.coordX = round(self.coordX, DISTANCE_DIGITS)
        self.coordY = round(self.coordY, DISTANCE_DIGITS)
        self.coordZ = round(self.coordZ, DISTANCE_DIGITS)

    def isInCorner(self):
        """determine if particle is in corner of room"""
        return self.coordX < MAX_DISTANCE_CORNER and self.coordY < MAX_DISTANCE_CORNER and self.coordZ < MAX_DISTANCE_CORNER

    def getCoordString(self):
        """get coordinates of particle as string"""
        return str([self.coordX, self.coordY, self.coordZ])

    def __str__(self):
        """string representation of object"""
        coords = 'coordinates=' + str([self.coordX, self.coordY, self.coordZ])
        vel = 'velocities=' + str([self.velX, self.velY, self.velZ])
        return '{0:<30} {1:<30}'.format(coords, vel)
