class Nest:
    def __init__(self, colony, breedChance=0.1):
        self.colony = colony
        self.breedChance = breedChance
        self.noAnts = 0
        colony.addNest(self)

    @property
    def color(self):
        return self.colony.color
