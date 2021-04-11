class new_Path:
    def __init__(
            self,
            name,
            start,
            end,
            start_angle=0,
            end_angle=0,
            length=1
    ):
        # open to suggestions for variable names as these are kinda long!
        self.name = name
        self.start = start
        self.start_angle = start_angle
        self.end = end
        self.end_angle = end_angle
        self.length = length
        self.foraging_pheromone = 0
        self.exploration_pheromone = 0
        
    def isequal(self,path):
        return self.name == path.name
    
    def show(self):
        print(self.name)
    
def test():
    path1 = new_Path(1,1,2)
    path2 = new_Path(1,1,3)
    print(path1.isequal(path2))
    
if __name__ == '__main__':
    test()



