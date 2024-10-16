import numpy as np


class Shape:
    pass


def generate_shapes():
    # Shape I
    shape_i = Shape(
        np.array(
            np.array([[1, 0], [1, 1], [1, 2], [1, 3]]),
            np.array([[0, 1], [1, 1], [2, 1], [2, 2]]),
        )
    )
