#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project 3 - OpenClassrooms: Aidez MacGyver à s'échapper !
Author:
    Jody Etienne
Github:
    https://github.com/etiennody
"""


class Application:
    # Is the game itself
    def __init__(self):
        # Initialize the main object
        self.open = False

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
                if self.set_position == self.maze.exit:
                    self.hero.end_game()
                self.open = False


def main():
    # Main entry point to play
    application = Application()
    application.loop()


if __name__ == "__main__":
    main()
