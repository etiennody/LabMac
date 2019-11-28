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
from position import Position as pos
from items import Floor, Hero


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

    def __contains__(self, position):
        return position in self.floor

    def load(self):
        with open():
            for x in range(0, 15):
                for y in range(0, 15):
                    if char == pos.FLOOR_CHAR:
                        self.floor.append(Floor(x, y))
                    elif char == pos.START_CHAR:
                        self.hero = Hero(x, y)
                        self.floor.append(Floor(x, y))
                    elif char == pos.EXIT_CHAR:
                        self.guardian = pos.Guardian(x, y)
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

    def add_hero(self, hero):
        self.hero = hero
        self.position = self.start
        self.hero.maze = self

    def win(self, weapons, position):
        return len(weapons) == 0 and self.position.hero == self.exit

    def loose(self, weapons, position):
        return len(weapons) > 0 and self.position.hero == self.exit
