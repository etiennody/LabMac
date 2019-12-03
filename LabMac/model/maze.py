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
        self.walls = []
        self.weapons = []
        self.hero = None
        # self.guardian = None
        self.start = None
        self.exit = None
        self.width = None
        self.height = None
        self.load(filename)
        # self.random_position_weapons()

    def __contains__(self, position):
        return position in self.floor

    # Associate a character to a position from a text file in lists
    def load(self, filename):
        with open(filename) as f:
            map = f.readlines()
            for lin, line in enumerate(map):
                for char, character in enumerate(line):
                    position = Position(char, lin)
                    if character == START_CHAR:
                        self.start = position
                        self.floor.append(position)
                    elif character == EXIT_CHAR:
                        self.exit = position
                        self.floor.append(position)
                    elif character == FLOOR_CHAR:
                        self.floor.append(position)
                    else:
                        self.walls.append(position)

            self.width = char + 1
            self.height = lin + 1

    def add_hero(self, hero):
        self.hero = hero
        self.hero = self.start
        self.hero.maze = self

    # def can_move_to(self):
    #     return Position(x, y) in self.maze.floor

    # @can_move_to
    # def move_hero_up(self):
    #     if self.can_move_to(self.hero.x - 1, self.hero.y):
    #         self.hero.up()
    #         for weapon in self.weapons:
    #             if self.hero == weapon:
    #                 self.hero.pick_up_weapon()

    # @can_move_to
    # def move_hero_down(self):
    #     if self.can_move_to(self.hero.x + 1, self.hero.y):
    #         self.maze.down()
    #         for weapon in self.weapons:
    #             if self.hero == weapon:
    #                 self.hero.pick_up_weapon()

    # def move_hero_left(self):
    #     if self.can_move_to(self.hero.x, self.hero.y - 1):
    #         self.hero.left()
    #         for weapon in self.weapons:
    #             if self.hero == weapon:
    #                 self.hero.pick_up_weapon()

    # def move_hero_right(self):
    #     if self.can_move_to(self.hero.x, self.hero.y + 1):
    #         self.hero.right()
    #         for weapon in self.weapons:
    #             if self.hero == weapon:
    #                 self.hero.pick_up_weapon()

    # get random positions for weapons
    def random_positions_weapons(self):
        self.weapons = random.sample(
            set(self.floor) - {self.start, self.exit}, 3)
        weapons = ["ether", "pipe", "needle"]
        for position in weapons:
            self.weapons.append(weapons(x=position.x, y=position.y, name=weapons.pop()))
