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

from LabMac.constants import WINDOW_WIDTH, WINDOW_HEIGHT, FPS, WALL, FLOOR, NEEDLE, ETHER, PIPE, GUARDIAN, SPRITE_SIZE


class LabPygame:

    def __init__(self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT):
        pygame.init()
        pygame.time.Clock().tick(FPS)
        self.window_surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption("LabMac - Help MacGyver !")

    def load_image(self, name, colorkey=None):

        fullpath = os.path.join('.LabMac/resources/images', name)

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
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        return image


class MazeView(LabPygame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.maze_render = pygame.Surface(self.window_surface.get_size()).convert()
        self.maze_render.fill((25, 25, 25))

        self.wall_img = self.load_image(WALL, -1)
        self.wall_render = pygame.transform.scale(self.wall_img, (32, 32))

        self.floor_img = self.load_image(FLOOR, -1)
        self.floor_render = pygame.transform.scale(self.floor_img, (32, 32))

        self.guardian_img = self.load_image(GUARDIAN, -1)
        self.guardian_render = pygame.transform.scale(self.guardian_img, (30, 30))

        self.needle_img = self.load_image(NEEDLE, -1)
        self.needle_render = pygame.transform.scale(self.needle_img, (30, 30))

        self.ether_img = self.load_image(ETHER, -1)
        self.needle_render = pygame.transform.scale(self.needle_img, (30, 30))

        self.pipe_img = self.load_image(PIPE, -1)
        self.pipe_render = pygame.transform.scale(self.needle_img, (30, 30))

    def display_elements(self, window_surface):
        for pos in self.walls:
            window_surface.blit(self.wall_render, (pos.y * SPRITE_SIZE, pos.x * SPRITE_SIZE))
        for pos in self.floor:
            window_surface.blit(self.floor_render, (pos.y * SPRITE_SIZE, pos.x * SPRITE_SIZE))
        for weap, pos in enumerate(self.weapons):
            if weap == 0:
                window_surface.blit(self.needle_render, (pos.y * SPRITE_SIZE, pos.x * SPRITE_SIZE))
            elif weap == 1:
                window_surface.blit(self.ether_render, (pos.y * SPRITE_SIZE, pos.x * SPRITE_SIZE))
            elif weap == 2:
                window_surface.blit(self.pipe_render, (pos.y * SPRITE_SIZE, pos.x * SPRITE_SIZE))
        window_surface.blit(self.guardian_render, (self.exit.y * SPRITE_SIZE, self.exit.x * SPRITE_SIZE))


class HeroView(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.hero_img = self.load_image("macgyver.png", -1)
        self.hero_render = pygame.transform.scale(self.hero_img, (30, 30))
        self.rect = self.hero_render.get_rect()
