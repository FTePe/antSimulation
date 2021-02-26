class Path:
    def __init__(
            self,
            angle,
            location,
            parents
    ):
        # open to suggestions for variable names as these are kinda long!
        self.foraging_pheromone = 0
        self.exploration_pheromone = 0
        self.angle = angle
        # Not sure which is more useful
        self.location = location  # location of the path
        self.parents = parents  # structure of paths
        self.children = []

    def add_child(self, path):
        self.children.append(path)

    # def add_parent(self, path):
    #     self.parent.append(path)

def test():
    test_path = Path(0, (1, 0), [(0, 1)])
    print(test_path.parents)

