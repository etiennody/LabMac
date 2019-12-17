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

from LabMac.model.maze import Maze
# from LabMac.model.items import Hero
from LabMac.views import LabPygame, MazeView#, HeroView
from LabMac.constants import FPS#, SPRITE_SIZE, WALL, WALL_CHAR, FLOOR, FLOOR_CHAR, EXIT_CHAR, GUARDIAN, NEEDLE, ETHER, PIPE, HERO


class Application:

    def __init__(self):
        self.open = False
        self.labpygame = LabPygame()
        self.maze = Maze("./LabMac/resources/map/map.txt")
        self.maze_view = MazeView(maze=self.maze)
        """Initialize clock"""
        self.clock = pygame.time.Clock()
        # self.hero = Hero(maze=self.maze, x=self.x, y=self.y)
        # self.hero_view = HeroView(hero=self.maze.hero)
        # Initialyze sprites
        # self.hero_sprites = pygame.sprite.RenderPlain((self.hero))

    def loop(self):
        """Launch the game with start interface"""
        self.labpygame.interface(mode='game_start')

        """Initialize the background music"""
        self.labpygame.play_music_background()

        self.open = True
        """Launch the main loop events"""
        while self.open:
            """Make sure that the game doesn't run at more than 30 frames per second"""
            self.clock.tick(FPS)
            """Listen events"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
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

            """Initialyze the window"""
            self.labpygame.window_surface.blit(self.labpygame.background, (0, 0))

            # Display elements of the game"""
            self.maze_view.display_elements()

            # self.hero.pick_up_weapon()

            # self.hero.fight_guarrdian()

            self.maze_view.update()

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
            pygame.display.update()
            pygame.display.flip()

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
