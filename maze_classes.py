class Path:
    def __init__(self, name, length=0, start_angle=0, end_angle=0):
        self.name = name
        self.length = length
        self.start_angle= start_angle
        self.end_angle= end_angle
        self.foraging_pheromone = 0
        self.exploration_pheromone = 0
        
    def reverse(self):
        length_reverse = self.length
        start_angle_reverse = self.end_angle-180
        end_angle_reverse = self.start_angle-180
        path_reverse = Path(str(self.name)+'_reverse', length_reverse,start_angle_reverse, end_angle_reverse)
        return path_reverse
        
        
    def __str__(self):
        return 'Path '+str(self.name)


class Intersection:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
    

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, path):
        self.adjacent[neighbor] = path

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id
    
    def change_id(self,new_name):
        self.id = new_name

    def get_path(self, neighbor):
        return self.adjacent[neighbor]
    
    def get_all_paths(self):
        paths = []
        for neighbor in self.get_connections():
            paths.append(self.get_path(neighbor))
        return paths
    
    def isequal(self,intersection):
        return self.get_id() == intersection.get_id()
            
    

class Maze:
    def __init__(self):
        self.inter_dict = {}
        self.num_intersections = 0

    def __iter__(self):
        return iter(self.inter_dict.values())

    def add_intersection(self, node):
        self.num_intersections = self.num_intersections + 1
        new_intersection = Intersection(node)
        self.inter_dict[node] = new_intersection
        return new_intersection

    def get_intersection(self, n):
        if n in self.inter_dict:
            return self.inter_dict[n]
        else:
            return None

    def add_path(self, path, frm, to):
        if frm not in self.inter_dict:
            print(frm, 'added')
            self.add_intersection(frm)
        if to not in self.inter_dict:
            print(to ,'added') 
            self.add_intersection(to)
        self.inter_dict[frm].add_neighbor(self.inter_dict[to], path)
        self.inter_dict[to].add_neighbor(self.inter_dict[frm], path.reverse())

    def get_intersections(self):
        return self.inter_dict.keys()
    
    def copy_intersections(self,maze):
        for name_intersection in maze.get_intersections():
            intersection = maze.get_intersection(name_intersection)
            self.add_intersection(name_intersection)
            self.inter_dict[name_intersection]=intersection
    
    def show(self):
        for node in self.get_intersections():
            inter = self.get_intersection(node)
            print('From ',inter.id)
            for neighbor in inter.adjacent:
                print('     to',neighbor.id, inter.adjacent[neighbor])
        return 

if __name__ == '__main__':

    
    int1 = Intersection('debut')
    print(int1)
    int1.change_id('fin')
    print(int1)
    
    
    g = Maze()

    tl = Path('tl', 3, -30, 0)  
    tr = Path('tr', 3, 30, 0)
    lr = Path('lr', 2, 30, 180-30)

    g.add_path(tl,'top','left')  
    g.add_path(tr,'top','right')
    g.add_path(lr, 'left','right')
    
    """
    for i in g:
        print(i)
        for path in i.get_all_paths():
            print(path)
    """    
    """
        for j in i.get_connections():
            iid = i.get_id()
            jid = j.get_id()
            print (iid, '-',jid,'via', i.get_path(j))
    """  
    """
    for i in g:
        print ('g.inter_dict[%s]=%s' %(i.get_id(), g.inter_dict[i.get_id()]))
    """
    
        
    g.show()
    inter = g.get_intersection('top')
    for neighbor in inter.get_connections():
        print(type(neighbor))
        print(neighbor.isequal(inter))
    print(inter.isequal(inter))


        
    

