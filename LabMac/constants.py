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
WINDOW_HEIGHT = 512
BACKGROUND = os.path.join('LabMac', 'resources', 'images', 'background.png')
BACKGROUND_COLOR = (41, 36, 33)
TEXT_COLOR = (255, 255, 255)
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

# Audio
BGM = os.path.join('LabMac', 'resources', 'audio', 'bgm.wav')
WIN_SOUND = os.path.join('LabMac', 'resources', 'audio', 'win.wav')
GAMEOVER_SOUND = os.path.join('LabMac', 'resources', 'audio', 'gameover.wav')
