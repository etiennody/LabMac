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

        # Define the equality between self position and another position
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(self.position)

    # Define the addition between self position and move position
    def __add__(self, movement):
        return Position(self.x + movement.mx, self.y + movement.my)

    # x, y : positions
    def position(self, x, y):
        self.x = x
        self.y = y


class Movement:
    def __init__(self, mx, my):
        self.mx = mx
        self.my = my

    def up(self):
        self.mx -= 1

    def down(self):
        self.mx += 1

    def left(self):
        self.my -= 1

    def right(self):
        self.my += 1
