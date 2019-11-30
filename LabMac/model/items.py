#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project 3 - OpenClassrooms: Aidez MacGyver à s'échapper !
Author:
    Jody Etienne
Github:
    https://github.com/etiennody
"""

from position import Position, MoveablePosition


class Floor(Position):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.content = None

    def is_empty(self):
        return self.content is None


class Hero(Position, MoveablePosition):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.inventory = []
        self.set_position = self.maze.start

    def __repr__(self):
        pos = super().__repr__()
        return f"Je suis le Hero dans la position {pos}"

    def in_inventory(self):
        self.inventory.append(self.set_position)
        return "You have found a weapon"
        return f"You have {len(self.inventory)} weapons in your inventory"


class Guardian(Position):
    pass
