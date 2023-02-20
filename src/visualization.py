import random

import numpy as np
import pygame

from ant import Ant
from nest import Nest
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

        self.font = pygame.font.Font(None, FONTSIZE)

        self.calculateCords()
        self.initSim()

    def calculateCords(self):
        self.gridCords = np.zeros((self.gridRows.size - 1, self.gridCols.size - 1, 2))
        for row in range(self.gridCords.shape[0]):
            for col in range(self.gridCords.shape[1]):
                self.gridCords[row, col] = [
                    (col + 1) * FIELDSIZE - FIELDSIZE / 2,
                    (row + 1) * FIELDSIZE - FIELDSIZE / 2,
                ]

    def randField(self):
        size = self.gridCords.shape[:2]
        return (random.randint(0, size[0] - 1), random.randint(0, size[1] - 1))

    def initSim(self):
        size = self.gridCords.shape[:2]
        self.sim = Simulation(size)
        size = np.array(size)
        center = size // 2

        redColony = self.sim.addColony("red")
        self.sim.placeNest(redColony, center)
        self.sim.placeNest(redColony, size - 1)

        blueColony = self.sim.addColony("blue")
        self.sim.placeNest(blueColony, self.randField())

        yellowColony = self.sim.addColony("yellow")
        self.sim.placeNest(yellowColony, self.randField())
        self.sim.placeNest(yellowColony, self.randField())
        self.sim.placeNest(yellowColony, self.randField())

    def drawGrid(self):
        for col in self.gridCols:
            pygame.draw.line(self.screen, GRIDCOLOR, (col, 0), (col, self.gridRows[-1]))
        for row in self.gridRows:
            pygame.draw.line(self.screen, GRIDCOLOR, (0, row), (self.gridCols[-1], row))

    def drawAnts(self):
        for row in range(self.sim.grid.shape[0]):
            for col in range(self.sim.grid[row].size):
                curr = self.sim.grid[row, col]
                # draw ants
                if isinstance(curr, Ant):
                    pygame.draw.circle(
                        self.screen,
                        curr.color,
                        self.gridCords[row, col],
                        ANTSIZE / 2,
                    )
                # draw nests
                if isinstance(curr, Nest):
                    center = self.gridCords[row, col]
                    x = center[0] - ANTSIZE / 2
                    y = center[1] - ANTSIZE / 2
                    pygame.draw.rect(
                        self.screen,
                        curr.color,
                        pygame.Rect(x, y, ANTSIZE, ANTSIZE),
                    )

    def drawStats(self):
        textHeight = 0
        for colony in self.sim.colonies:
            statsText = colony.color + " colony: " + str(colony.noAnts) + " ants"
            text = self.font.render(statsText, True, colony.color)
            self.screen.blit(text, (0, textHeight))
            textHeight += FONTSIZE

    def mainLoop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(BACKGROUNDCOLOR)
            self.drawGrid()
            self.drawAnts()
            self.drawStats()

            self.sim.simulate()

            pygame.display.flip()
            self.clock.tick(5)
        pygame.quit()
