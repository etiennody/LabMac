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

import Labmac.constants as cs
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
                    if character == cs.FLOOR_CHAR:
                        self.floor.append(Position(x, y))
                    elif character == cs.WALL_CHAR:
                        self.wall.append(Position(x, y))
                    elif character == cs.START_CHAR:
                        self.start == Position(x, y)
                        self.floor.append(Position(x, y))
                    elif character == cs.EXIT_CHAR:
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

    def can_move_to(self, x, y):
        if Position(x, y) in self.floor:
            self

    def move_hero_up(self):
        if self.can_move_to(self.hero.x - 1, self.hero.y):
            self.hero.up()

    def move_hero_down(self):
        if self.can_move_to(self.hero.x + 1, self.hero.y):
            self.hero.down()

    def move_hero_left(self):
        if self.can_move_to(self.hero.x, self.hero.y - 1):
            self.hero.left()

    def move_hero_right(self):
        if self.can_move_to(self.hero.x, self.hero.y + 1):
            self.hero.right()
