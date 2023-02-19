import numpy as np
import pygame

NAME = "Ants turf war"
SCREENWIDTH, SCREENHEIGHT = 1200, 1000
ANTSIZE = 10
FIELDSIZE = ANTSIZE * 1.5
SCREENSIZE = (
    SCREENWIDTH - SCREENWIDTH % FIELDSIZE,
    SCREENHEIGHT - SCREENHEIGHT % FIELDSIZE,
)
GRIDCOLOR = "black"
ANTCOLOR = "wheat4"


class Map:
    def __init__(self, size):
        self._grid = np.zeros(size)

    @property
    def grid(self):
        return np.random.choice([0, 1], size=self._grid.shape)


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
        for row in range(self.map.grid.shape[0]):
            for col in range(self.map.grid[row].size):
                if self.map.grid[row, col]:
                    pygame.draw.circle(
                        self.screen, ANTCOLOR, self.gridCords[row, col], ANTSIZE / 2
                    )

    def main(self):
        self.map = Map(self.gridCords.shape[:2])

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


sim = Visualization()
sim.main()
