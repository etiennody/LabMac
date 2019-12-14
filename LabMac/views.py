#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project 3 - OpenClassrooms: Aidez MacGyver à s'échapper !
Author:
    Jody Etienne
Github:
    https://github.com/etiennody
"""

import sys
import pygame

from LabMac.constants import WINDOW_WIDTH, WINDOW_HEIGHT, FPS, HERO, SPRITE_SIZE, WALL, FLOOR, BGM#, HERO, BGM, NEEDLE, ETHER, PIPE, GUARDIAN


class LabPygame(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pygame.init()
        pygame.time.Clock().tick(FPS)
        self.window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("LabMac - Help MacGyver !")
        # """Text font"""
        # font = pygame.font.SysFont('Consolas', 15)

    def show_text(self, window_surface, font, text, color, position):
        """Show the text on screen"""
        text_render = font.render(text, True, color)
        rect = text_render.get_rect()
        rect.left, rect.top = position
        self.window_surface.blit(text_render, rect)
        return rect.right

    def button(self, window_surface, position, text, buttoncolor=(120, 120, 120), linecolor=(20, 20, 20), textcolor=(255, 255, 255), bwidth=200, bheight=50):
        """Create and config buttons"""
        left, top = position
        pygame.draw.line(window_surface, linecolor, (left, top), (left+bwidth, top), 5)
        pygame.draw.line(window_surface, linecolor, (left, top-2), (left, top+bheight), 5)
        pygame.draw.line(window_surface, linecolor, (left, top+bheight), (left+bwidth, top+bheight), 5)
        pygame.draw.line(window_surface, linecolor, (left+bwidth, top+bheight), (left+bwidth, top), 5)
        pygame.draw.rect(window_surface, buttoncolor, (left, top, bwidth, bheight))
        font = pygame.font.SysFont('Consolas', 30)
        text_render = font.render(text, 1, textcolor)
        rect = text_render.get_rect()
        rect.centerx, rect.centery = left + bwidth / 2, top + bheight / 2
        return self.window_surface.blit(text_render, rect)

    def interface(self, mode='game_start'):
        """Create interface for start and end game with mouse"""
        pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        if mode == 'game_start':
            clock = pygame.time.Clock()
            while True:
                self.window_surface.fill((41, 36, 33))
                button_1 = self.button(self.window_surface, (150, 150), 'START')
                button_2 = self.button(self.window_surface, (150, 250), 'QUIT')
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit(-1)
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if button_1.collidepoint(pygame.mouse.get_pos()):
                            return True
                        elif button_2.collidepoint(pygame.mouse.get_pos()):
                            pygame.quit()
                            sys.exit(-1)
                pygame.display.update()
                clock.tick(FPS)

        if mode == 'game_end':
            clock = pygame.time.Clock()
            while True:
                self.window_surface.fill((41, 36, 33))
                button_1 = self.button(self.window_surface, (150, 150), 'RESTART')
                button_2 = self.button(self.window_surface, (150, 250), 'QUIT')
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit(-1)
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if button_1.collidepoint(pygame.mouse.get_pos()):
                            return True
                        elif button_2.collidepoint(pygame.mouse.get_pos()):
                            pygame.quit()
                            sys.exit(-1)
                pygame.display.update()
                clock.tick(FPS)
        else:
            raise ValueError('Interface.mode unsupport <%s>...' % mode)

    def play_music_background(self):
        '''Launch the game music background'''
        pygame.mixer.init()
        pygame.mixer.music.load(BGM)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)


class MazeView(pygame.sprite.Sprite):
    def __init__(self, maze):
        pygame.sprite.Sprite.__init__(self)
        self.maze = maze
        self.floor = []
        self.walls = []
        self.weapons = []
        self.hero = None
        self.start = None
        self.exit = None
        self.width = None
        self.height = None
        self.window_surface = WINDOW_WIDTH * WINDOW_HEIGHT

    def display_elements(self, window_surface):
        clock = pygame.time.Clock()
        while True:
            self.window_surface.blit(pygame.image.load(WALL), (self.maze.walls.y * SPRITE_SIZE, self.maze.walls.x * SPRITE_SIZE))
            # self.window_surface.blit(pygame.image.load(FLOOR), (pos.y * SPRITE_SIZE, pos.x * SPRITE_SIZE))
            # for weap, pos in enumerate(self.weapons):
            #     if weap == 0:
            #         self.window_surface.blit(self.needle_render, (pos.y * SPRITE_SIZE, pos.x * SPRITE_SIZE))
            #     elif weap == 1:
            #         self.window_surface.blit(self.ether_render, (pos.y * SPRITE_SIZE, pos.x * SPRITE_SIZE))
            #     elif weap == 2:
            #         self.window_surface.blit(self.pipe_render, (pos.y * SPRITE_SIZE, pos.x * SPRITE_SIZE))
            #     self.window_surface.blit(self.guardian_render, (self.exit.y * SPRITE_SIZE, self.exit.x * SPRITE_SIZE))
            pygame.display.update()
            clock.tick(FPS)


# class MazeView(LabPygame, pygame.sprite.Sprite):

#     def __init__(self, maze, *args, **kwargs):
#         pygame.sprite.Sprite.__init__(self)
#         super().__init__(self, *args, **kwargs)
#         self.maze = maze
#         # self.wall = wall
#         # self.display_elements(self.window_surface)

#         self.maze_render = pygame.Surface(self.window_surface.get_size()).convert()
#         self.maze_render.fill((153, 153, 255))

        # self.wall = self.load_image(WALL, -1)
        # self.wall_render = pygame.transform.scale(self.wall_img, (32, 32))

        # self.floor_img = self.load_image(FLOOR, -1)
        # self.floor_render = pygame.transform.scale(self.floor_img, (32, 32))

        # self.guardian_img = self.load_image(GUARDIAN, -1)
        # self.guardian_render = pygame.transform.scale(self.guardian_img, (30, 30))

        # self.needle_img = self.load_image(NEEDLE, -1)
        # self.needle_render = pygame.transform.scale(self.needle_img, (30, 30))

        # self.ether_img = self.load_image(ETHER, -1)
        # self.needle_render = pygame.transform.scale(self.needle_img, (30, 30))

        # self.pipe_img = self.load_image(PIPE, -1)
        # self.pipe_render = pygame.transform.scale(self.needle_img, (30, 30))


# class HeroView(LabPygame, pygame.sprite.Sprite):

#     def __init__(self, maze, hero, *args, **kwargs):
#         pygame.sprite.Sprite.__init__(self)
#         super().__init__(*args, **kwargs)
#         self.hero = hero
#         self.maze = maze

#         self.image = pygame.image.load("./LabMac/resources/images/macgyver.png")
#         self.rect = self.image.get_rect()
#         self.rect.topleft = self.maze.hero.y_pixel, self.maze.hero.x_pixel
#         # import pdb; pdb.set_trace()
#         self.hero = pygame.Rect(300, 100, 32, 32)
#         self.hero_img = self.load_image(HERO, -1).convert()
#         self.hero_render = pygame.transform.scale(self.hero_img, (32, 32))
