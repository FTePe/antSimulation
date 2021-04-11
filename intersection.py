from new_path import new_Path

class Intersection:
    def __init__(
            self,
            name
    ):
        # self.location = location
        self.name = name
        self.neighbours = []
        self.branches = []
        
    
    def add_link(self, intersection,path):
        neighbour1 = (intersection,path)
        neighbour2 = (self, path)
        self.neighbours.append(neighbour1)
        intersection.neighbours.append(neighbour2)

    def add_branch(self, path):
        self.branches.append(path)
    
    def show(self):
        print('Intersection',self.name, end = " ")
        print('has neighbours :')
        for link in self.neighbours:
            neighbour = link[0]
            path = link[1]
            print('    ',neighbour.name,'via',end = " "), 
            path.show()
            
def test():
    int1=Intersection(1)
    int2=Intersection(2)
    path = new_Path('1to2',int1,int2)
    int1.add_link(int2,path)
    int1.show()
    int2.show()
    
if __name__ == '__main__':
    test()
    