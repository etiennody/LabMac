"""
Project 3 - OpenClassrooms: Aidez MacGyver à s'échapper !
Author:
    Jody Etienne
Github:
    https://github.com/etiennody
"""


class Position:

    def __init__(self, x, y):
        self.set_position(x, y)

    def __repr__(self):
        return str(Position({self.x}, {self.y}))

    def set_position(self, x, y):
        self.x = x
        self.y = y
