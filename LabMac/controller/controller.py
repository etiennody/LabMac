#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project 3 - OpenClassrooms: Aidez MacGyver à s'échapper !
Author:
    Jody Etienne
Github:
    https://github.com/etiennody
"""

from LabMac.model.maze import Maze
from LabMac.model.items import Hero


class KeyController:
    def try_to_move(self):
        # Check requested directions
        while True:
            self.user = input("Where do you want to move u for up , d for down, l for left, r for right or q to quit the game)?")
            if self.user == "u":
                self.maze.move_hero_up()
            elif self.user == "d":
                self.move_hero_down()
            elif self.user == "l":
                self.maze.move_hero_left()
            elif self.user == "r":
                self.maze.move_hero_right()
            elif self.user == "q":
                self.maze.quit()

            result = self.maze.fight_guardian()
            if result is None:
                continue
            if result:
                print("YOU WIN")
            else:
                print("YOU LOOSE")
