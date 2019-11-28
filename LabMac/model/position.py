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

    def __init__(self, x, y):
        self.set_position(x, y)

    def __repr__(self):
        return f"Position({self.x}, {self.y})"

    def set_position(self, x, y):
        self.x = x
        self.y = y


class Move:

    def __init__(self, mx, my):
        self.mx = mx
        self.my = my

    def up(self, mx, my):
        return (0, -1)

    def down(self, mx, my):
        return (0, 1)

    def left(self, mx, my):
        return (-1, 0)

    def right(self, mx, my):
        return (1, 0)
