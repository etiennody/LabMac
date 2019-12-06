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
        self.set_position = None
        self.inventory = []

    def __repr__(self):
        return f"Hero({self.x}, {self.y})"

    # # Put weapon in inventory
    def pick_up_weapon(self, weapon):
        self.inventory.append(weapon)
        weapon.x = None
        weapon.y = None

    # # Put positions weapons in inventory
    def in_inventory(self):
        self.inventory.append(self.set_position)
        return "You have found a weapon"
        return f"You have {len(self.inventory)} weapon(s) in your inventory"


class Weapon(Position):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
