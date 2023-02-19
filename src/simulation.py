import numpy as np


class Simulation:
    def __init__(self, size):
        self._grid = np.zeros(size)

    @property
    def grid(self):
        return np.random.choice([0, 1], size=self._grid.shape)
