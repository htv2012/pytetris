import numpy as np


class Board:
    def __init__(self, screen, height, width):
        self._screen = screen
        self._height = height
        self._width = width
        self._matrix = np.zeros([width, height], dtype=int)
        self._current_tile = None
        self._score = 0
