#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project 3 - OpenClassrooms: Aidez MacGyver à s'échapper !
Author:
    Jody Etienne
GitHub:
    https://github.com/etiennody
"""

import pygame
import random

from LabMac.views import LabPygame
from LabMac.model.position import Position
from LabMac.model.items import Weapon, Hero
from LabMac.constants import FLOOR_CHAR, START_CHAR, EXIT_CHAR


class Maze(pygame.sprite.Sprite):
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        self.floor = []
        self.walls = []
        self.weapons = []
        self.hero = None
        self.start = None
        self.exit = None
        self.width = None
        self.height = None
        self.load(filename)
        self.random_positions_weapons()
        self.labpygame = LabPygame()

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
        """Verify if a kind position is in the floor position"""
        return Position(x, y) in self.floor

    def move_hero_up(self):
        if self.can_move_to(self.hero.x, self.hero.y - 1):
            self.hero.up()
            # Take a weapon when the hero moves up
            for weapon in self.weapons:
                if self.hero == weapon:
                    self.hero.pick_up_weapon(weapon)

    def move_hero_down(self):
        if self.can_move_to(self.hero.x, self.hero.y + 1):
            self.hero.down()
            # Take a weapon when the hero moves down
            for weapon in self.weapons:
                if self.hero == weapon:
                    self.hero.pick_up_weapon(weapon)

    def move_hero_left(self):
        if self.can_move_to(self.hero.x - 1, self.hero.y):
            self.hero.left()
            # Take a weapon when the hero moves left
            for weapon in self.weapons:
                if self.hero == weapon:
                    self.hero.pick_up_weapon(weapon)

    def move_hero_right(self):
        if self.can_move_to(self.hero.x + 1, self.hero.y):
            self.hero.right()
            # Take a weapon when the hero moves right
            for weapon in self.weapons:
                if self.hero == weapon:
                    self.hero.pick_up_weapon(weapon)

    # All conditions to fight with the guardian at the end
    def fight_guardian(self):
        if self.hero == self.exit:
            return len(self.hero.inventory) == len(self.weapons)

    # Get random positions for weapons
    def random_positions_weapons(self):
        positions = random.sample(
            set(self.floor) - {self.start, self.exit}, 3)
        # Define a name for each weapons
        weapon_names = ["ether", "pipe", "needle"]
        for position in positions:
            self.weapons.append(
                Weapon(x=position.x, y=position.y, name=weapon_names.pop())
            )
