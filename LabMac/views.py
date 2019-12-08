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

from LabMac.constants import WINDOW_WIDTH, WINDOW_HEIGHT, FPS


class LabPygame:

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
