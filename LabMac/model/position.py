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
        self.set_position(x, y)

    def __repr__(self):
        return f"Position({self.x}, {self.y})"

    # x, y : positions
    def set_position(self, x, y):
        self.x = x
        self.y = y


class MoveablePosition(Position):
    # Possibles positions to Up, Down, Left and Right
    def __init__(self, mx, my):
        self.mx = mx
        self.my = my

    def up(self):
        self.x -= 1

    def down(self):
        self.x += 1

    def left(self):
        self.x -= 1

    def right(self):
        self.x += 1
