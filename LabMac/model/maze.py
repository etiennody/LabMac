#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project 3 - OpenClassrooms: Aidez MacGyver à s'échapper !
Author:
    Jody Etienne
Github:
    https://github.com/etiennody
"""

import random

from LabMac.constants import START_CHAR, EXIT_CHAR, FLOOR_CHAR, WALL_CHAR
from .position import Position
from .items import Floor, Hero


class Maze:
    def __init__(self, filename):
        self.floor = []
        self.wall = []
        self.weapons = []
        self.hero = None
        self.guardian = None
        self.start = None
        self.exit = None
        self.load(filename)
        self.get_random_weapons()

    def __contains__(self, position):
        return position in self.floor

    def load(self):
        with open():
            for x in range(0, 15):
                for y in range(0, 15):
                    if char == Position.FLOOR_CHAR:
                        self.floor.append(Floor(x, y))
                    elif char == Position.START_CHAR:
                        self.hero = Hero(x, y)
                        self.floor.append(Floor(x, y))
                    elif char == Position.EXIT_CHAR:
                        self.guardian = Position.Guardian(x, y)
                        self.floor.append(Floor(x, y))
                    else:
                        return "It's a wall"

    def get_random_position(self, num_weapons):
        # create a [x, y] list of weapons
        weapons = []
        while len(weapons) < num_weapons:
            new_weapons = [random.sample(
                list(self.floor) - {self.start, self.exit}, num_weapons)
            ]
            if new_weapons not in weapons:
                weapons.append(new_weapons)
        return weapons

#    def add_hero(self, hero):
#        self.hero = hero
#        self.position = self.start
#       self.hero.maze = self

    def win(self, weapons, position):
        return len(weapons) == 0 and self.position.hero == self.exit

    def loose(self, weapons, position):
        return len(weapons) > 0 and self.position.hero == self.exit
