import numpy as np
import pygame

from settings import *
from simulation import Simulation


class Visualization:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(NAME)
        self.screen = pygame.display.set_mode(SCREENSIZE)
        self.clock = pygame.time.Clock()

        self.gridCols = np.arange(0, SCREENSIZE[0] + 1, FIELDSIZE)
        self.gridRows = np.arange(0, SCREENSIZE[1] + 1, FIELDSIZE)

        self.calculateCords()

    def calculateCords(self):
        self.gridCords = np.zeros((self.gridRows.size, self.gridCols.size, 2))
        for row in range(self.gridCords.shape[0]):
            for col in range(self.gridCords.shape[1]):
                self.gridCords[row, col] = [
                    (col + 1) * FIELDSIZE - FIELDSIZE / 2,
                    (row + 1) * FIELDSIZE - FIELDSIZE / 2,
                ]

    def drawGrid(self):
        for col in self.gridCols:
            pygame.draw.line(self.screen, GRIDCOLOR, (col, 0), (col, self.gridRows[-1]))
        for row in self.gridRows:
            pygame.draw.line(self.screen, GRIDCOLOR, (0, row), (self.gridCols[-1], row))

    def drawAnts(self):
        for row in range(self.sim.grid.shape[0]):
            for col in range(self.sim.grid[row].size):
                if self.sim.grid[row, col]:
                    pygame.draw.circle(
                        self.screen, ANTCOLOR, self.gridCords[row, col], ANTSIZE / 2
                    )

    def mainLoop(self):
        self.sim = Simulation(self.gridCords.shape[:2])

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill("white")
            self.drawGrid()
            self.drawAnts()

            pygame.display.flip()
            self.clock.tick(5)
        pygame.quit()
