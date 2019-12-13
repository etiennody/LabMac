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
from pygame.locals import *

from LabMac.model.maze import Maze
from LabMac.views import LabPygame, MazeView#, HeroView
from LabMac.constants import BACKGROUND, FPS#, WINDOW_WIDTH, WINDOW_HEIGHT, HERO, SPRITE_SIZE


class Application:
    """Is the game itself"""
    def __init__(self):
        """Initialize the main object"""
        self.open = False
        self.labpygame = LabPygame()
        self.maze = Maze("./LabMac/resources/map/map.txt")
        self.maze_view = MazeView(self.labpygame)
        self.background = pygame.image.load(BACKGROUND)

    def loop(self):
        """Initialyze the game"""
        self.labpygame.interface(mode='game_start')
        self.labpygame.window_surface.blit(self.background, [0, 0])

        self.maze_view.display_elements(self.labpygame.window_surface)

        self.open = True

        """Launch the main loop of the game"""
        while self.open:
            pygame.time.Clock().tick(FPS)

            """Listen events"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.open = False

            """Change the direction according to the keyboard event"""
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] != 0:
                self.maze.move_hero_up()
            if keys[pygame.K_DOWN] != 0:
                self.maze.move_hero_down()
            if keys[pygame.K_LEFT] != 0:
                self.maze.move_hero_left()
            if keys[pygame.K_RIGHT] != 0:
                self.maze.move_hero_right()

            # Initialize Pygame
            # pygame.init()

            # Initialyze, create and display window
            # self.labpygame.window_surface.blit(self.maze_view.maze_render, (0, 0))

            # self.labpygame.window_surface.blit(self.maze_view.wall_render, (self.maze.walls.set_position.x, self.maze.set_position.y))

            # self.labpygame.window_surface.blit(self.hero_view.hero_render, (self.maze.hero.x * 32, self.maze.hero.x * 32))

            # for item in self.maze:
            #     self.elements_view = MazeView(self.maze, self.labpygame, self.maze_view)
            # self.labpygame.window_surface.blit(self.elements_view, (self.maze.set_position.x, self.maze.set_position.y))

            # Add differents elements: walls, floor, weapons, start, exit
            # self.maze_view.display_elements(self.window_surface)

            # result = self.maze.fight_guardian()
            # if result is None:
            # continue
            #     print(result)
            #     pygame.display.flip()

        # result = self.maze.fight_guardian() # None, True, False

        # if result is None:
        #     continue

        # if result:
        #     self.maze_view.display_win()
        #     return
        # else result:
        #     self.maze_view.display_game_over()
        #     return

        self.labpygame.interface(mode='game_end')


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
