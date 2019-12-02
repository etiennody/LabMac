#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project 3 - OpenClassrooms: Aidez MacGyver à s'échapper !
Author:
    Jody Etienne
Github:
    https://github.com/etiennody
"""

from .position import Position, MoveablePosition


# class Floor(Position):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.content = None

#     def is_empty(self):
#         return self.content is None


class Hero (MoveablePosition):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.inventory = []
        self.set_position = self.maze.start

    def __repr__(self):
        pos = super().__repr__()
        return f"Je suis le Hero dans la position {pos}"

    # Put weapon name in inventory
    def pick_up_weapon(self, weapon):
        self.in_inventory.add(weapon)
        weapon.x = None
        weapon.y = None

    # Put positions weapons in inventory
    def in_inventory(self):
        self.in_inventory.append(self.set_position)
        return "You have found a weapon"
        return f"You have {len(self.inventory)} weapons in your inventory"

    # Get the three weapons to put the guardian to sleep and exit the maze
    def end_game(self):
        if len(self.inventory) == 3:
            print("YOU WIN")
        else:
            print("GAME OVER")


class Weapon(Position):
    def __init__(self, name, *args, **kwargs):
        self.name = name


# class Guardian(Position):
#     pass
