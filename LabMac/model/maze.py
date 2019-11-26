# -*- coding: utf-8 -*-

"""
Project 3 - OpenClassrooms: Aidez MacGyver à s'échapper !
Author:
    Jody Etienne
Github:
    https://github.com/etiennody
"""


from items import Floor
from LabMac import constants


class Maze:

    def __init__(self, filename):
        self.floor = []
        self.wall = []
        self.hero = None
        self.guardian = None
        self.weapons = None
        self.load(filename)

    def load(self):
        for x in xrange(0, 15):
            for y in xrange(0, 15):
                if char == FLOOR_MAZE:
                    self.floor.append(Floor(x, y))
                elif char == START_MAZE:
                    self.hero = Hero(x, y)
                    self.floor.append(Floor(x, y))
                elif char == EXIT_MAZE:
                    self.guardian = Guardian(x, y)
                    self.floor.append(Floor(x, y))
                else:
                    pass