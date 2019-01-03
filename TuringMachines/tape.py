# -*- encoding: utf-8 -*-

from enum import IntEnum

class Direction(IntEnum):
    LEFT = 0
    RIGHT = 1

class Tape:
    """ A Turing Machine's tape. Each of the left/right ends
    will be padded with a character 'd' (empty symbol)
    """
    def __init__(self, content: str):
        self.content = 'd{}d'.format(content)
        self.rw_head_pos = 1

    def read(self):
        """ Read the character from the cell on the rw_head """
        return self.content[self.rw_head_pos]

    def write(self, c):
        """ Write the character to the cell on the rw_head """
        self.content = self.content[:self.rw_head_pos] + c + self.content[(self.rw_head_pos+1):]

    def move_head(self, direction):
        """ Move the read write head of the tape in the specified direction
        :param direction: Left: 0, Right: 1
        """
        self.rw_head_pos += (1 if direction == Direction.RIGHT else -1)

    def __str__(self):
        return self.content
