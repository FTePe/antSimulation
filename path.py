class Path:
    def __init__(
            self,
            angle,
            parent
    ):
        self.foraging_pheromone = 0
        self.exploration_pheromone = 0
        self.angle = angle
        # Not sure which is more useful
        self.location = (1,1)  # location of the path
        self.parent = parent  # structure of paths
        self.children = []

    def add_child(self, path):
        self.children.append(path)
