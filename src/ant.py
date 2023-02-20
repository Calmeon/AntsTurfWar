class Ant:
    def __init__(self, nest):
        self.nest = nest

    @property
    def colony(self):
        return self.nest.colony

    @property
    def color(self):
        return self.colony.color
