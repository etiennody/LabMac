#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project 3 - OpenClassrooms: Aidez MacGyver à s'échapper !
Author:
    Jody Etienne
Github:
    https://github.com/etiennody
"""

from position import MoveablePosition


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

    def move_hero_up(self, set_position):
        self.set_position.up

    def move_hero_down(self, set_position):
        self.set_position.down

    def move_hero_left(self, set_position):
        self.set_position.left

    def move_hero_right(self, set_position):
        self.set_position.right

    # Put weapons in inventory
    def in_inventory(self):
        self.inventory.append(self.set_position)
        return "You have found a weapon"
        return f"You have {len(self.inventory)} weapons in your inventory"

    # Get the three weapons to put the guardian to sleep and exit the maze
    def end_game(self):
        if len(self.inventory) == 3:
            print("YOU WIN")
        else:
            print("GAME OVER")



# class Guardian(Position):
#     pass
