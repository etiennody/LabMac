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
import sys

# from LabMac.constants import BACKGROUND_COLOR
# from LabMac.views import LabPygame
# from LabMac.model.maze import Maze


class Application:
#     # Is the game itself
#     def __init__(self, labpygame_object: LabPygame = None):
#         # Initialize the main object
#         self.open = False
#         self.labpygame = labpygame_object
#         self.gameplay = Maze(self.labpygame)
#         self.gameplay.load("./Labmac/resources/map/map.text")

    def loop(self):

        # Launch the main loop of the game
        self.open = True
        # Initialize Pygame
        pygame.init()
        size = WIDTH, HEIGHT = 640, 480
        rect = pygame.Rect(50, 50, 50, 50)
        BLACK = (0, 0, 0)
        YELLOW = (255, 255, 0)
        speed = [4, 4]
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode(size)

        while self.open:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT()
                    sys.exit()
            rect = rect.move(speed)
            if rect.left < 0 or rect.right > WIDTH:
                speed[0] = -speed[0]
            if rect.top < 0 or rect.bottom > HEIGHT:
                speed[1] = -speed[1]
            screen.fill(BLACK)
            pygame.draw.rect(screen, YELLOW, rect, 0)
            pygame.display.flip()
            clock.tick(30)

            # self.labpygame.window_surface.fill(BACKGROUND_COLOR)

            # command = input(
            #     "\nWhere do you want to move ? 'u' for up , 'd' for down, 'l' for left, 'r' for right or 'q' to quit the game)?"
            # )
            # if command == "u":
            #     self.maze.move_hero_up()
            # elif command == "d":
            #     self.maze.move_hero_down()
            # elif command == "l":
            #     self.maze.move_hero_left()
            # elif command == "r":
            #     self.maze.move_hero_right()
            # elif command == "q":
            #     pygame.display.flip()
            # else:
            #     print("Choose another direction!")

            # result = self.maze.fight_guardian()
            # if result:
            #     print(result)
            #     pygame.display.flip()


def main():
    # Main entry point to play
    application = Application()
    application.loop()


"""class Application:
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
    application.loop()"""
