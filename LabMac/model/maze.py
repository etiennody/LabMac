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

    def load(self, filename):
        with open(filename) as f:
            lines = f.readlines()
            for y, line in enumerate(lines):
                for x, character in enumerate(line):
                    if character == Position.FLOOR_CHAR:
                        self.floor.append(Position(x, y))
                    elif character == Position.WALL_CHAR:
                        self.wall.append(Position(x, y))
                    elif character == Position.START_CHAR:
                        self.start == Position(x, y)
                        self.floor.append(Position(x, y))
                    elif character == Position.EXIT_CHAR:
                        self.exit = Position(x, y)
                        self.floor.append(Position(x, y))
                    else:
                        continue

    def get_weapon_position(self, num_weapons):
        # create a [x, y] list of weapons and take position randomly
        weapons = []
        while len(weapons) < num_weapons:
            new_weapons = [random.sample(
                list(self.floor) - {self.start, self.exit}, num_weapons)
            ]
            if new_weapons not in weapons:
                weapons.append(new_weapons)
        return weapons

    def win(self, weapons, position):
        return len(weapons) == 0 and self.position.hero == self.exit

    def loose(self, weapons, position):
        return len(weapons) > 0 and self.position.hero == self.exit

    def can_move
