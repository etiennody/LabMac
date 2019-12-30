#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project 3 - OpenClassrooms: Aidez MacGyver à s'échapper !
Author:
    Jody Etienne
GitHub:
    https://github.com/etiennody
"""

from LabMac.model.position import Position, Movement


class Hero(Movement):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.position = None
        self.inventory = []

    def __repr__(self):
        return f"Hero({self.x}, {self.y})"

    def pick_up_weapon(self, weapon):
        """Put weapon in inventory"""
        self.inventory.append(weapon)
        weapon.x = None
        weapon.y = None


class Weapon(Position):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

    def has_position(self):
        return self.x and self.y
