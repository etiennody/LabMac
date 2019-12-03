#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project 3 - OpenClassrooms: Aidez MacGyver à s'échapper !
Author:
    Jody Etienne
Github:
    https://github.com/etiennody
"""

from .maze import Maze


class Game:

    def __init__(self):
        self.maze = Maze()
        self.maze.load(".LabMac/resources/map/map.txt")
        self.mg = None


def main():
    game = Game()
    print(game.maze.floor)


if __name__ == "__main__":
    main()
