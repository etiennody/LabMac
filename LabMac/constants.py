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
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
BACKGROUND = os.path.join('LabMac', 'resources', 'images', 'background.png')
SPRITE_SIZE = 32

# Frame rate
FPS = 30

# Images
MAP = os.path.join('LabMac', 'resources', 'map', 'map.txt')
HERO = os.path.join('LabMac', 'resources', 'images', 'macgyver.png')
GUARDIAN = os.path.join('LabMac', 'resources', 'images', 'guardian.png')
WALL = os.path.join('LabMac', 'resources', 'images', 'wall.png')
FLOOR = os.path.join('LabMac', 'resources', 'images', 'floor.png')
ETHER = os.path.join('LabMac', 'resources', 'images', 'ether.png')
NEEDLE = os.path.join('LabMac', 'resources', 'images', 'needle.png')
PIPE = os.path.join('LabMac', 'resources', 'images', 'pipe.png')
