#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project 3 - OpenClassrooms: Aidez MacGyver à s'échapper !
Author:
    Jody Etienne
Github:
    https://github.com/etiennody
"""

from .position import Position


# class Floor(Position):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.content = None

#     def is_empty(self):
#         return self.content is None


class Hero:
    def __init__(self):
        self.position = None
        self.maze = None
        self.inventory = []

    def move(self, direction):
        new_position = self.position + direction
        if new_position in self.maze.floor:
            self.position = new_position

    # Put weapon in inventory
    def pick_up_weapon(self, weapon):
        self.in_inventory.add(weapon)
        weapon.x = None
        weapon.y = None

    # Put positions weapons in inventory
    def in_inventory(self):
        self.inventory.append(self.position)
        return "You have found a weapon"
        return f"You have {len(self.inventory)} weapon(s) in your inventory"

    # Get the three weapons to put the guardian to sleep and exit the maze
    # def check_end_game(self):
    #     return len(self.inventory) == 3

    # All conditions to fight with the guardian at the end
    def fight_guardian(self):
        return self.position == self.maze.exit and len(self.inventory) == 3


class Weapon(Position):
    def __init__(self, name, *args, **kwargs):
        super().__init__()
        self.name = name


# class Guardian(Position):
#     pass
