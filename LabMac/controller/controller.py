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


class Application:
    # Is the game itself
    def __init__(self):
        # Initialize the main object
        self.open = False
        self.maze = Maze(filename="./LabMac/resources/map/map.txt")

    def loop(self):
        print(self.maze.hero)
        # Launch the main loop of the game
        self.open = True
        while self.open:
            command = input(
                "Where do you want to move ? \
                u for up , d for down, l for left, r for right \
                or q to quit the game)?"
            )
            if command == "u":
                self.maze.move_hero_up()
            elif command == "d":
                self.maze.move_hero_down()
            elif command == "l":
                self.maze.move_hero_left()
            elif command == "r":
                self.maze.move_hero_right()
            elif command == "q":
                self.open = False

            print(self.maze.hero)

#             result = self.maze.fight_guardian()
#             if result is None:
#                 continue
#             if result:
#                 print("YOU WIN")
#             else:
#                 print("YOU LOOSE")


def main():
    # Main entry point to play
    application = Application()
    application.loop()
