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
from LabMac.model.items import Maze
from LabMac.model.items import Hero


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


class MazeView:

    def __init__(self):
        self.map_render = pygame.Surface(self.maze.labpygame_object.screen.get_size()).convert()
        self.map_render.fill((25, 25, 25))

        self.wall_img = self.maze.wall.load_image("wall.png", -1)
        self.wall_render = pygame.transform.scale(self.wall_img, (32, 32))

        self.floor_img = self.maze.floor.load_image("floor.png", -1)
        self.floor_render = pygame.transform.scale(self.floor_img, (32, 32))


class HeroView:

    def __init__(self):
        self.hero_img = self.maze.hero.load_image("macgyver.png", -1)
        self.hero_render = pygame.transform.scale(self.hero_img, (30, 30))


class ItemsView:

    def __init__(self):
        pass
