#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project 3 - OpenClassrooms: Aidez MacGyver à s'échapper !
Author:
    Jody Etienne
Github:
    https://github.com/etiennody
"""

from position import Position


class Floor(Position):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.content = None

    def is_empty(self):
        return self.content is None
