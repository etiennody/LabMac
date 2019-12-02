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

from LabMac.constants import FLOOR_CHAR, START_CHAR, EXIT_CHAR
from .position import Position


class Maze:
    def __init__(self, filename):
        self.floor = []
        # self.walls = []
        self.weapons = []
        self.hero = None
        # self.guardian = None
        self.start = None
        self.exit = None
        self.width = None
        self.height = None
        self.load(filename)
        self.random_position_weapons()

    # def __contains__(self, position):
    #     return position in self.floor

    # Associate a character to a position from a text file
    def load(self, filename):
        with open(filename) as f:
            lines = f.readlines()
            self.width = len(lines)
            self.height = len(lines[0])
            for n_row, line in enumerate(lines):
                for n_col, character in enumerate(line):
                    if character == FLOOR_CHAR:
                        self.floor.append(Position(n_row, n_col))
                    # elif character == WALLS_CHAR:
                    #     self.walls.append(Position(n_row, n_col))
                    elif character == START_CHAR:
                        self.start = Position(n_row, n_col)
                        self.floor.append(Position(n_row, n_col))
                    elif character == EXIT_CHAR:
                        self.exit = Position(n_row, n_col)
                        self.floor.append(Position(n_row, n_col))

    def can_move_to(self, x, y):
        return Position(x, y) in self.maze.floor

    def move_hero_up(self):
        if self.can_move_to(self.hero.x - 1, self.hero.y):
            self.hero.up()
            for weapon in self.weapons:
                if self.hero == weapon:
                    self.hero.pick_up_weapon()

    def move_hero_down(self):
        if self.can_move_to(self.hero.x + 1, self.hero.y):
            self.hero.down()
            for weapon in self.weapons:
                if self.hero == weapon:
                    self.hero.pick_up_weapon()

    def move_hero_left(self):
        if self.can_move_to(self.hero.x, self.hero.y - 1):
            self.hero.left()
            for weapon in self.weapons:
                if self.hero == weapon:
                    self.hero.pick_up_weapon()

    def move_hero_right(self):
        if self.can_move_to(self.hero.x, self.hero.y + 1):
            self.hero.right()
            for weapon in self.weapons:
                if self.hero == weapon:
                    self.hero.pick_up_weapon()

    # get random position for weapons
    def random_positions_weapons(self):
        self.random_positions = random.sample(
            set(self.floor) - {self.start, self.exit}, 3)
        weapons = ["ether", "pipe", "needle"]
        for position in random_positions():
            self.weapons.append(Weapons(x=position.x, y=position.y, name=weapons.pop())
