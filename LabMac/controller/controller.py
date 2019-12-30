#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project 3 - OpenClassrooms: Aidez MacGyver à s'échapper !
Author:
    Jody Etienne
GitHub:
    https://github.com/etiennody
"""

import sys
import pygame

from LabMac.constants import FPS
from LabMac.model.maze import Maze
from LabMac.views import LabPygame, MazeView, HeroView, Bar


class Application:

    def __init__(self):
        """
        Initialise pygame with labpygame object, the maze, the hero
        and the info bar
        """
        self.open = False
        self.labpygame = LabPygame()
        self.maze = Maze("./LabMac/resources/map/map.txt")
        self.maze_view = MazeView(maze=self.maze)
        self.hero_view = HeroView(hero=self.maze.hero, maze=self.maze)
        self.bar = Bar(hero=self.maze.hero)

    # Define the main loop of the game
    def loop(self):
        # Launch the game with start interface
        self.labpygame.interface()

        # Initialize the background music
        self.labpygame.play_music_background()

        # Launch the main loop events
        while not self.open:
            # Listen events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    # Change the direction according to the keyboard event
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_UP] != 0:
                        self.maze.move_hero_up()
                    if keys[pygame.K_DOWN] != 0:
                        self.maze.move_hero_down()
                    if keys[pygame.K_LEFT] != 0:
                        self.maze.move_hero_left()
                    if keys[pygame.K_RIGHT] != 0:
                        self.maze.move_hero_right()

            # Initialize the window
            self.labpygame.window_surface.blit(
                self.labpygame.background, (0, 480)
            )

            # Display the information bar
            self.bar.display_bar()

            # Display elements(walls, floor, guardian) of the game
            self.maze_view.display_elements()

            # Display the hero of the game
            self.hero_view.display_hero()

            response = self.maze.fight_guardian()
            if response is None:
                pygame.display.flip()
                self.labpygame.clock.tick(FPS)
            elif response:
                # Play the win sound and open a new window if the player wins
                self.labpygame.play_win_sound()
                self.labpygame.display_win()
            else:
                # Play the game over sound and open a new window if the player loses
                self.labpygame.play_gameover_sound()
                self.labpygame.display_lose()


def main():
    """Main entry point to play"""
    application = Application()
    application.loop()


"""
######### CONSOLE VERSION ##########
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

            result = self.maze.fight_guardian()
            if result:
                print(result)
                self.open = False


def main():
    # Main entry point to play
    application = Application()
    application.loop()
"""
