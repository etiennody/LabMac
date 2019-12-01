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

from LabMac.constants import FLOOR_CHAR, WALLS_CHAR, START_CHAR, EXIT_CHAR
from .position import Position


class Maze:
    def __init__(self, filename):
        self.floor = []
        self.wall = []
        self.weapons = []
        self.hero = None
        self.guardian = None
        self.start = None
        self.exit = None
        self.width = None
        self.height = None
        self.filename = filename
        self.random_position_weapons()

    # def __contains__(self, position):
    #     return position in self.floor

    # Associate a character to a position from a text file
    def load(self, filename):
        with open(filename) as f:
            lines = f.readlines()
            for n_row, line in enumerate(lines):
                for n_col, character in enumerate(line):
                    if character == FLOOR_CHAR:
                        self.floor.append(Position(n_row, n_col))
                    elif character == WALLS_CHAR:
                        self.walls.append(Position(n_row, n_col))
                    elif character == START_CHAR:
                        self.start = Position(n_row, n_col)
                        self.floor.append(Position(n_row, n_col))
                    elif character == EXIT_CHAR:
                        self.exit = Position(n_row, n_col)
                        self.floor.append(Position(n_row, n_col))
                    self.width = n_col
                    self.height = n_row

    # get random position for weapons
    def random_position_weapons(self):
        self.weapons = random.sample(
            set(self.floor) - {self.start, self.exit}, 3)
        return self.weapons
