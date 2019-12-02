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


class Game:
    def __init__(self):
        self.maze = Maze("./LabMac/resources/map/map.txt")
        self.hero = Hero(self.maze)
        self.user = None
        self.open = False

    def quit(self):
        # Quit the game
        self.open = False

    def try_to_move(self):
        # Check requested directions
        while True:
            self.user = input("Where do you want to move u for up , d for down, l for left, r for right or q to quit the game)?")
            if self.user == "u":
                self.maze.move_hero_up()
            elif self.user == "d":
                self.maze.move_hero_down()
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

    # def loop(self):
    #     # Launching the loop as long as the game is open
    #     self.open = True
    #     while self.open:
    #         self.maze()
    #         if self.hero.set_position in self.maze.weapon:
    #             if self.hero.set_position in self.maze.in_inventory:
    #                 pass
    #             else:
    #                 self.hero.random_position_weapons()
    #         self.try_to_move()
    #         if self.user == "q":
    #             self.open = False
    #         else:
    #             self.hero.try_to_move(self.user)
    #         if self.set_position == self.maze.exit:
    #             self.hero.end_game()
    #             self.open = False


def main():
    # Launch the game
    labmac = Game()
    labmac.loop()


# if __name__ == "__main__":
#     main()
