class Colony:
    def __init__(self, color):
        self.color = color
        self.nests = []

    @property
    def noAnts(self):
        noAnts = 0
        for nest in self.nests:
            noAnts += nest.noAnts
        return noAnts

    def addNest(self, nest):
        self.nests.append(nest)
