#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project 3 - OpenClassrooms: Aidez MacGyver à s'échapper !
Author:
    Jody Etienne
GitHub:
    https://github.com/etiennody
"""
import pygame

# from LabMac.constants import BACKGROUND_COLOR
from LabMac.views import LabPygame, MazeView
from LabMac.model.maze import Maze
from LabMac.constants import MAP


class Application:
    # Is the game itself
    def __init__(self):
        # Initialize the main object
        self.open = False
        self.labpygame = LabPygame()
        self.maze = Maze(MAP)
        self.maze_view = MazeView()

    def loop(self):

        # Launch the main loop of the game
        self.open = True

        while self.open:

            # Initialyze, create and display window
            self.labpygame.window_surface.blit(self.maze_view.maze_render, (0, 0))

            # Add differents elements: walls, floor, weapons, start, exit
            self.maze_view.display_elements(self.window_surface)

            # Listen events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.open = False

                elif event.type == pygame.KEYDOWN:
                    # Change the direction according to the keyboard event
                    if event.key == pygame.K_UP:
                        self.maze.move_hero_up()
                    elif event.key == pygame.K_DOWN:
                        self.maze.move_hero_down()
                    elif event.key == pygame.K_LEFT:
                        self.maze.move_hero_left()
                    elif event.key == pygame.K_RIGHT:
                        self.maze.move_hero_right()

            # result = self.maze.fight_guardian()
            # if result:
            #     print(result)
            #     pygame.display.flip()

        pygame.display.flip()


def main():
    # Main entry point to play
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
