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
            pass


def main():
    # Main entry point to play
    application = Application()
    application.loop()


if __name__ == "__main__":
    main()
