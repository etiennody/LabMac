#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project 3 - OpenClassrooms: Aidez MacGyver à s'échapper !
Author:
    Jody Etienne
GitHub:
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

        # Launch the main loop of the game
        self.open = True

        print("\nMacGyver is located at the entry of the maze in :")
        print(f"Position({self.maze.hero.x}, {self.maze.hero.y})")

        while self.open:
            print("\nUpdate MacGyver position :")
            print(f"Position({self.maze.hero.x}, {self.maze.hero.y})")
            print("\nWeapons position on maze : ")
            print(f"{self.maze.weapons}")
            print(f"\nExit position :")
            print(self.maze.exit)

            command = input(
                "\nWhere do you want to move ? 'u' for up , 'd' for down, 'l' for left, 'r' for right or 'q' to quit the game)?"
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
            else:
                print("Choose another direction!")

            # if self.maze.is_exit_hero():
            #     if self.maze.count_inventory():
            #         print(
            #             "* YOU HAVE FIND THE EXIT AND SEDATED THE GUARDIAN *")
            #         print("-----YOU WIN !!-----")
            #         self.open = False

            result = self.maze.fight_guardian()
            if result:
                print(result)
                self.open = False
            # if result is None:
            #     continue
            # if result:
            #     print("YOU WIN")
            # else:
            #     print("YOU LOOSE")
            #     self.open = False


def main():
    # Main entry point to play
    application = Application()
    application.loop()
