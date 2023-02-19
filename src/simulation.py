import random

import numpy as np

from ant import Ant
from nest import Nest


class Simulation:
    def __init__(self, size):
        self.grid = np.empty(size, dtype=object)
        self.nestsPos = []

    """Creation functions"""

    def placeNest(self, place=(0, 0)):
        if self.grid[place] is None:
            self.grid[place] = Nest()
            self.nestsPos.append(place)

    """Transition functions"""

    def breed(self, moved=[]):
        for nest in self.nestsPos:
            for vectorRow in -1, 0, 1:
                for vectorCol in -1, 0, 1:
                    row, col = (nest[0] + vectorRow, nest[1] + vectorCol)
                    # don't place on top of the nest
                    # and look for edges
                    if (
                        (row, col) != nest
                        and row in range(self.grid.shape[0])
                        and col in range(self.grid.shape[1])
                    ):
                        if (
                            self.grid[row, col] is None
                            and np.random.random() < self.grid[nest].breedChance
                        ):
                            self.grid[row, col] = Ant()
                            self.grid[nest].antsCount += 1
                            moved.append(self.grid[row, col])
        return moved

    def move(self, moved=[]):
        for fieldRow in range(self.grid.shape[0]):
            for fieldCol in range(self.grid.shape[1]):
                if (
                    isinstance(self.grid[fieldRow, fieldCol], Ant)
                    and self.grid[fieldRow, fieldCol] not in moved
                ):
                    avalibleMoves = []
                    for vectorRow in -1, 0, 1:
                        for vectorCol in -1, 0, 1:
                            (row, col) = (fieldRow + vectorRow, fieldCol + vectorCol)
                            # don't place on top of the ant
                            # and look for edges
                            if (
                                (row, col) != (fieldRow, fieldCol)
                                and row in range(self.grid.shape[0])
                                and col in range(self.grid.shape[1])
                                and self.grid[row, col] is None
                            ):
                                avalibleMoves.append((row, col))
                    # move
                    if len(avalibleMoves):
                        newField = random.choice(avalibleMoves)
                        self.grid[newField] = self.grid[fieldRow, fieldCol]
                        self.grid[fieldRow, fieldCol] = None
                        moved.append(self.grid[newField])
        return moved

    def simulate(self):
        """Main simulation function where all transitions will be run"""
        moved = []
        moved = self.breed(moved)
        moved = self.move(moved)
