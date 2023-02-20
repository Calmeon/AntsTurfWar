import random

import numpy as np

from ant import Ant
from nest import Nest


class Simulation:
    def __init__(self, size):
        self.grid = np.empty(size, dtype=object)
        self.nestsPos = []

    """Creation functions"""

    def placeNest(self, color, place=(0, 0)):
        if self.grid[place] is None:
            self.grid[place] = Nest(color)
            self.nestsPos.append(place)

    def getAvalibleFields(self, fieldRow, fieldCol):
        """returns free fields in neigboorhood"""
        avalibleFields = []
        for vectorRow in -1, 0, 1:
            for vectorCol in -1, 0, 1:
                (row, col) = (fieldRow + vectorRow, fieldCol + vectorCol)
                # don't include field and look for edges
                if (
                    (row, col) != (fieldRow, fieldCol)
                    and row in range(self.grid.shape[0])
                    and col in range(self.grid.shape[1])
                    and self.grid[row, col] is None
                ):
                    avalibleFields.append((row, col))
        return avalibleFields

    """Transition functions"""

    def breed(self, moved=[]):
        for nest in self.nestsPos:
            avalibleFields = self.getAvalibleFields(nest[0], nest[1])
            for field in avalibleFields:
                if np.random.random() < self.grid[nest].breedChance:
                    self.grid[field] = Ant()
                    self.grid[nest].antsCount += 1
                    moved.append(self.grid[field])
        return moved

    def move(self, moved=[]):
        shuffledRows = list(range(self.grid.shape[0]))
        random.shuffle(shuffledRows)
        shuffledCols = list(range(self.grid.shape[1]))
        random.shuffle(shuffledCols)

        for fieldRow in shuffledRows:
            for fieldCol in shuffledCols:
                if (
                    isinstance(self.grid[fieldRow, fieldCol], Ant)
                    and self.grid[fieldRow, fieldCol] not in moved
                ):
                    avalibleMoves = self.getAvalibleFields(fieldRow, fieldCol)
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
