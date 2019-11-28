#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project 3 - OpenClassrooms: Aidez MacGyver à s'échapper !
Author:
    Jody Etienne
Github:
    https://github.com/etiennody
"""

import Maze.maze


def main(self):
    maze = Maze()
    while True:
        resp = input("where do you want to move (u, d, l r)?")
        if resp == "u":
            maze.move_hero_up()
        if resp == "d":
            maze.move_hero_down()
        if resp == "l":
            maze.move_hero_left()
        if resp == "r":
            maze.move_hero_right()

    if maze.win():
        print("YOU WIN!!")
    if maze.loose():
        print("GAME OVER")


if __name__ == "__main__":
    main()
