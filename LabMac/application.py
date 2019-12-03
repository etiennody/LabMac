#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project 3 - OpenClassrooms: Aidez MacGyver à s'échapper !
Author:
    Jody Etienne
Github:
    https://github.com/etiennody
"""
from LabMac.model.game import Game
from LabMac.model.maze import


class Application:
    # Is the game itself
    def __init__(self):
        # Initialize the main object
        self.open = False
        self.game = Game()

    def loop(self):
        # Launch the main loop of the game
        self.open = True
        while self.open:
            # Launching the loop as long as the game is open
            self.maze()
            if self.hero.position in self.maze.weapon:
                if self.hero.position in self.maze.in_inventory:
                    pass
                else:
                    self.hero.random_position_weapons()
            self.try_to_move()
            if self.user == "q":
                self.open = False
            else:
                if self.position == self.maze.exit:
                    self.hero.fight_guardian()
                self.open = False


def main():
    # Main entry point to play
    application = Application()
    application.loop()


if __name__ == "__main__":
    main()
