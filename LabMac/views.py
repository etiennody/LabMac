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

from LabMac.constants import WINDOW_WIDTH, WINDOW_HEIGHT, FPS, BGM, HERO, SPRITE_SIZE, WALL, FLOOR, GUARDIAN, NEEDLE, PIPE, ETHER, TEXT_COLOR, BACKGROUND_COLOR


class LabPygame(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        """Initialize the window display"""
        pygame.init()
        self.open = False
        self.clock = pygame.time.Clock()
        self.size = (WINDOW_WIDTH, WINDOW_HEIGHT)
        self.window_surface = pygame.display.set_mode(self.size)
        pygame.display.set_caption("LabMac - Help MacGyver !")
        # Filling the background
        self.background = pygame.Surface(self.window_surface.get_size())
        self.background = self.background.convert()
        self.background.fill(BACKGROUND_COLOR)
        """Text font"""
        self.font = pygame.font.SysFont('swiss', 30)

    def show_text(self, window_surface, font, text, color, position):
        """Show the text on screen"""
        text_render = font.render(text, True, color)
        rect = text_render.get_rect()
        rect.left, rect.top = position
        window_surface.blit(text_render, rect)
        return rect.right

    def button(
        self, window_surface, position, text,
        buttoncolor=(120, 120, 120), linecolor=(20, 20, 20),
        textcolor=TEXT_COLOR, bwidth=200, bheight=50
    ):
        """Create and config buttons"""
        left, top = position
        pygame.draw.line(
            window_surface, linecolor, (left, top), (left + bwidth, top), 5
        )
        pygame.draw.line(
            window_surface, linecolor, (
                left, top - 2), (left, top + bheight), 5
        )
        pygame.draw.line(
            window_surface, linecolor, (
                left, top + bheight), (left + bwidth, top + bheight), 5
        )
        pygame.draw.line(
            window_surface, linecolor, (
                left + bwidth, top + bheight), (left + bwidth, top), 5
        )
        pygame.draw.rect(
            window_surface, buttoncolor, (left, top, bwidth, bheight))
        font = pygame.font.SysFont('swiss', 25)
        font.set_bold(True)
        text_render = font.render(text, 1, textcolor)
        rect = text_render.get_rect()
        rect.centerx, rect.centery = left + bwidth / 2, top + bheight / 2
        return self.window_surface.blit(text_render, rect)

    def interface(self, mode='game_start'):
        """Create interface for start with mouse"""
        clock = pygame.time.Clock()
        while True:
            self.window_surface.fill(BACKGROUND_COLOR)
            button_1 = self.button(
                self.window_surface, (150, 290), 'START'
            )
            button_2 = self.button(self.window_surface, (150, 390), 'QUIT')
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

    def display_win(self):
        """Create interface when player win and use mouse"""
        clock = pygame.time.Clock()
        while True:
            self.window_surface.fill(BACKGROUND_COLOR)
            self.text = self.font.render(
                "WELL DONE! YOU WIN!!", 1, (255, 255, 255))
            self.textPos = self.text.get_rect()
            self.textPos.centerx = self.window_surface.get_rect().centerx
            self.textPos.centery = self.window_surface.get_rect().centery
            self.window_surface.blit(self.text, self.textPos)
            button_1 = self.button(self.window_surface, (150, 290), 'RESTART')
            button_2 = self.button(self.window_surface, (150, 390), 'QUIT')
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

    def display_lose(self):
        """Create interface when player lose and use mouse"""
        clock = pygame.time.Clock()
        while True:
            self.window_surface.fill(BACKGROUND_COLOR)
            self.text = self.font.render(
                "GAME OVER... Let's try again!", 1, TEXT_COLOR)
            self.textPos = self.text.get_rect()
            self.textPos.centerx = self.window_surface.get_rect().centerx
            self.textPos.centery = self.window_surface.get_rect().centery
            self.window_surface.blit(self.text, self.textPos)
            button_1 = self.button(self.window_surface, (150, 290), 'RESTART')
            button_2 = self.button(self.window_surface, (150, 390), 'QUIT')
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

    def play_music_background(self):
        """Launch the background music of the game"""
        pygame.mixer.init()
        pygame.mixer.music.load(BGM)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)


class MazeView(pygame.sprite.Sprite):
    def __init__(self, maze):
        super().__init__()
        self.maze = maze
        self.window_surface = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT)
        )
        self.walls_img = pygame.image.load(WALL).convert()
        self.walls_rect = self.walls_img.get_rect()
        self.walls_render = pygame.transform.scale(self.walls_img, (32, 32))
        #
        self.floor_img = pygame.image.load(FLOOR).convert()
        self.floor_rect = self.floor_img.get_rect()
        self.floor_render = pygame.transform.scale(self.floor_img, (32, 32))
        #
        self.needle_img = pygame.image.load(NEEDLE).convert_alpha()
        self.needle_rect = self.needle_img.get_rect()
        self.needle_render = pygame.transform.scale(self.needle_img, (30, 30))
        #
        self.ether_img = pygame.image.load(ETHER).convert_alpha()
        self.ether_rect = self.ether_img.get_rect()
        self.ether_render = pygame.transform.scale(self.ether_img, (30, 30))
        #
        self.pipe_img = pygame.image.load(PIPE).convert_alpha()
        self.pipe_rect = self.pipe_img.get_rect()
        self.pipe_render = pygame.transform.scale(self.pipe_img, (30, 30))
        #
        self.guardian_img = pygame.image.load(GUARDIAN).convert_alpha()
        self.guardian_rect = self.guardian_img.get_rect()
        self.guardian_render = pygame.transform.scale(
            self.guardian_img, (30, 30)
        )

    def display_elements(self):
        # Display the image of walls in its position
        for wall in self.maze.walls:
            self.window_surface.blit(
                self.walls_render, (
                    wall.x * SPRITE_SIZE, wall.y * SPRITE_SIZE
                )
            )
        # Display the image of floor in its position
        for floor in self.maze.floor:
            self.window_surface.blit(
                self.floor_render, (
                    floor.x * SPRITE_SIZE, floor.y * SPRITE_SIZE
                )
            )
        # Display weapons in each positions with their images
        for weap in self.maze.weapons:
            if not weap.has_position():
                continue
            if weap.name == "needle":
                self.window_surface.blit(
                    self.needle_render, (
                        weap.x * SPRITE_SIZE, weap.y * SPRITE_SIZE
                    )
                )
            elif weap.name == "ether":
                self.window_surface.blit(
                    self.ether_render, (
                        weap.x * SPRITE_SIZE, weap.y * SPRITE_SIZE
                    )
                )
            elif weap.name == "pipe":
                self.window_surface.blit(
                    self.pipe_render, (
                        weap.x * SPRITE_SIZE, weap.y * SPRITE_SIZE
                    )
                )
        # Display the image of guardian in its position
        self.window_surface.blit(
            self.guardian_render, (
                self.maze.exit.x * SPRITE_SIZE,
                self.maze.exit.y * SPRITE_SIZE
            )
        )
        pygame.display.update()


class HeroView(LabPygame, pygame.sprite.Sprite):

    def __init__(self, maze, hero):
        super().__init__()

        self.hero = hero
        self.maze = maze
        self.hero_img = pygame.image.load(HERO)
        self.hero_render = pygame.transform.scale(self.hero_img, (30, 30))
        self.rect = self.hero_img.get_rect()
        self.rect.topleft = self.maze.hero.x, self.maze.hero.y

    def display_hero(self):
        self.window_surface.blit(self.hero_render, (
            self.maze.hero.x * SPRITE_SIZE, self.maze.hero.y * SPRITE_SIZE))
        pygame.display.update()


class Bar(LabPygame, pygame.sprite.Sprite):

    def __init__(self, hero):
        super().__init__()
        pygame.font.init()
        self.hero = hero
        self.font = pygame.font.SysFont('swiss', 16)
        self.generate_text()
        self.rect = self.image.get_rect()
        self.rect.topleft = 5, 480

    def generate_text(self):
        if len(self.hero.inventory) == 0:
            self.image = self.font.render(
                f"Help MacGyver! Find 3 weapons to sedate the guardian.",
                True, TEXT_COLOR
            )
        elif len(self.hero.inventory) == 1:
            self.image = self.font.render(
                f"You have {len(self.hero.inventory)}/3"
                " weapon in your bag.",
                True, TEXT_COLOR
            )
        elif len(self.hero.inventory) > 1 and len(self.hero.inventory) < 3:
            self.image = self.font.render(
                f"You have {len(self.hero.inventory)}/3"
                " weapons in your bag.",
                True, TEXT_COLOR)
        elif len(self.hero.inventory) == 3:
            self.image = self.font.render(
                f"You can sedate the guardian and leave the maze! Go!",
                True, TEXT_COLOR)

    def display_bar(self):
        self.generate_text()
        self.window_surface.blit(self.image, self.rect)
