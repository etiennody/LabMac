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
