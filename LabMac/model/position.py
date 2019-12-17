#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project 3 - OpenClassrooms: Aidez MacGyver à s'échapper !
Author:
    Jody Etienne
Github:
    https://github.com/etiennody
"""
from LabMac.constants import SPRITE_SIZE


class Position:
    # x, y : initial positions
    def __init__(self, x, y):
        super().__init__()
        self.set_position(x, y)

    def __repr__(self):
        return f"Position({self.x}, {self.y})"

        # Define the equality between self position and another position
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return self.x * 1000 + self.y

    # Define the addition between self position and move position
    def __add__(self, movement):
        return Position(self.x + movement.mx, self.y + movement.my)

    @property
    def x_pixel(self):
        '''Property that calculates the pixel position'''
        self.x * SPRITE_SIZE

    @property
    def y_pixel(self):
        '''Property that calculates the pixel position'''
        self.y * SPRITE_SIZE

    # x, y : positions
    def set_position(self, x, y):
        self.x = x
        self.y = y


class Movement(Position):

    def up(self):
        self.y -= 1

    def down(self):
        self.y += 1

    def left(self):
        self.x -= 1

    def right(self):
        self.x += 1
