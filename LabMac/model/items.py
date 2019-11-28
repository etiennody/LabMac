#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project 3 - OpenClassrooms: Aidez MacGyver à s'échapper !
Author:
    Jody Etienne
Github:
    https://github.com/etiennody
"""

from position import Position, Move


class Floor(Position):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.content = None

    def is_empty(self):
        return self.content is None


class Hero(Position, Move):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.weapons = []

    def __repr__(self):
        pos = super().__repr__()
        return f"Je suis le Hero dans la position {pos}"

    def move_hero_up(self, position):
        self.position = Move(0, -1)

    def move_hero_down(self, position):
        self.position = Move(0, 1)

    def move_hero_left(self, pos):
        self.position = Move(-1, 0)

    def move_hero_right(self, pos):
        self.position = Move(1, 0)


class Guardian(Position):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = self.exit
