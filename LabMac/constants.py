#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project 3 - OpenClassrooms: Aidez MacGyver à s'échapper !
Author:
    Jody Etienne
Github:
    https://github.com/etiennody
"""
import os
import pygame

# Default game constants definition
START_CHAR = "S"
EXIT_CHAR = "E"
FLOOR_CHAR = "0"
WALL_CHAR = "x"

# Initialize window
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 480
BACKGROUND_COLOR = (153, 153, 255)
SPRITE_SIZE = 32


# Frame rate
FPS = 60

# Images
MAP = os.path.join('LabMac', 'resources', 'map', 'map.txt')
HERO = 'macgyver.png'
GUARDIAN = 'guardian.png'
WALL = 'wall.png'
FLOOR = 'floor.png'
ETHER = 'ether.png'
NEEDLE = 'needle.png'
PIPE = 'pipe.png'


class Pygame:

    def __init__(self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT):
        pygame.init()
        pygame.time.Clock().tick(FPS)
        self.window_surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption("LabMac - Help MacGyver !")

    def load_image(self, name, colorkey=None):

        fullpath = os.path.join('LabMac', 'resources', 'images', name)

        try:
            image = pygame.image.load(fullpath)
            if image.get_alpha() is None:
                image = image.convert()
            else:
                image = image.get_alpha()
        except pygame.error:
            print("Cannot load image", name)
            raise SystemExit

        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        return image
