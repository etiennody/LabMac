#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project 3 - OpenClassrooms: Aidez MacGyver à s'échapper !
Author:
    Jody Etienne
Github:
    https://github.com/etiennody
"""


class Position:
    # x, y : initial positions
    def __init__(self, x, y):
        self.position(x, y)

    def __repr__(self):
        return f"Position({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(self.position)

    # x, y : positions
    def position(self, x, y):
        self.x = x
        self.y = y


class MoveablePosition(Position):

    def up(self):
        self.x -= 1

    def down(self):
        self.x += 1

    def left(self):
        self.y -= 1

    def right(self):
        self.y += 1
