#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project 3 - OpenClassrooms: Aidez MacGyver à s'échapper !
Author:
    Jody Etienne
GitHub:
    https://github.com/etiennody
"""

# import random

from LabMac.constants import FLOOR_CHAR, START_CHAR, EXIT_CHAR
from LabMac.model.position import Position
from LabMac.model.items import Hero#, Weapon


class Maze:
    def __init__(self, filename):
        self.floor = []
        self.walls = []
        self.weapons = [Position(9, 1), Position(10, 1), Position(11, 1)]
        self.hero = None
        self.start = None
        self.exit = None
        self.width = None
        self.height = None
        self.load(filename)
        # self.random_positions_weapons()

    def __contains__(self, set_position):
        return set_position in self.floor

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
                        self.hero = Hero(x=char, y=lin)
                    elif character == EXIT_CHAR:
                        self.exit = position
                        self.floor.append(position)
                    elif character == FLOOR_CHAR:
                        self.floor.append(position)
                    else:
                        self.walls.append(position)

            self.width = char + 1
            self.height = lin + 1

    def can_move_to(self, x, y):
        return Position(x, y) in self.floor

    def move_hero_up(self):
        if self.can_move_to(self.hero.x, self.hero.y - 1):
            self.hero.up()
            for weapon in self.weapons:
                if self.hero == weapon:
                    print("You have find a weapon!")
                    # self.hero.pick_up_weapon()

    def move_hero_down(self):
        if self.can_move_to(self.hero.x, self.hero.y + 1):
            self.hero.down()
            for weapon in self.weapons:
                if self.hero == weapon:
                    print("You have find a weapon!")
                    # self.hero.pick_up_weapon()

    def move_hero_left(self):
        if self.can_move_to(self.hero.x - 1, self.hero.y):
            self.hero.left()
            for weapon in self.weapons:
                if self.hero == weapon:
                    print("You have find a weapon!")
                    # self.hero.pick_up_weapon()

    def move_hero_right(self):
        if self.can_move_to(self.hero.x + 1, self.hero.y):
            self.hero.right()
            for weapon in self.weapons:
                if self.hero == weapon:
                    print("You have find a weapon!")
                    # self.hero.pick_up_weapon(weapon)
                    # print("You have find a weapon!")

    # get random positions for weapons
    # def random_positions_weapons(self):
    #     positions = random.sample(
    #         set(self.floor) - {self.start, self.exit}, 3)
    #     weapon_names = ["ether", "pipe", "needle"]
    #     for position in positions:
    #         self.weapons.append(
    #             Weapon(x=position.x, y=position.y, name=weapon_names.pop())
    #         )
