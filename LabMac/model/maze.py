# -*- coding: utf-8 -*-

"""
Project 3 - OpenClassrooms: Aidez MacGyver à s'échapper !
Author:
    Jody Etienne
Github:
    https://github.com/etiennody
"""
import random

from Labmac import constants as char
from position import Position
from items import Floor, Hero


class Maze:
    def __init__(self, filename):
        self.floor = []
        self.wall = []
        self.hero = None
        self.guardian = None
        self.load(filename)

    def load(self, filename):
        with open(filename):
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
                        return "It's a wall"

    def get_random_weapons(self, num_weapons):
        # create a [x, y] list of weapons
        weapons = []
        while len(weapons) < num_weapons:
            new_weapons = [random.randint(self.floor)]
            if new_weapons not in weapons:
                weapons.append(new_weapons)
        return weapons
