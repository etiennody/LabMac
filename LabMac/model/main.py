#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
import Maze.maze


def main():
    maze = Maze()
    while True:
        # Game initialisation
        the_weapons = get_random_weapons(3)
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
        print("WIN!!")
    if maze.loose():
        print("GAME OVER")


if __name__ == "__main__":
    main()