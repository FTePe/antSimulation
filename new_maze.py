from graph import *
import numpy as np



def tower_hanoi(size,name=''): #Size is the number of pieces to move (must be int>=1)
    maze
    if size == 1:
        #Create intersections
        top = Intersection(name+'top')
        left = Intersection(name+'left')
        right = Intersection(name+'right')
        
        #Create the path between intersections
        tl = new_Path(name+'tl',top,left,30,0,3)
        tr = new_Path(name+'tr',top,right,-30,0,3)
        lr = new_Path(name+'lr',left,right,30,-30,2)
        
        #Link intersections
        top.add_link(left,tl)
        top.add_link(right,tr)
        left.add_link(right,lr)
        
        #Generate the maze
        maze1 = Maze([top,left,right])
        return maze1
    
    else:
        #Generate the lower order mazes
        maze_top = tower_hanoi(size-1,name+'top-')
        maze_left = tower_hanoi(size-1,name+'left-')
        maze_right = tower_hanoi(size-1,name+'right-')
        
        #Spot the interconnected intersections
        top_left = maze_top.intersections[3**(size-2)+(size>2)*(3*(size-3)+1)]
        top_right = maze_top.intersections[3**(size-1)-1]
        left_top = maze_left.intersections[0]
        right_top = maze_right.intersections[0]
        left_right = maze_left.intersections[3**(size-1)-1]
        right_left = maze_right.intersections[3**(size-2)+(size>2)*(3*(size-3)+1)]
        
        #Create the path between intersections
        tl = new_Path(name+'tl'+str(size),top_left,left_top,-30,0,3)
        tr = new_Path(name+'tr'+str(size),top_right,right_top,30,0,3)
        lr = new_Path(name+'lr'+str(size),left_right,right_left,30,-30,2)
        
        #Link intersections
        top_left.add_link(left_top,tl)
        top_right.add_link(right_top,tr)
        left_right.add_link(right_left,lr)
        
        #Gathering all the intersections
        intersections = []
        for intersection in maze_top.intersections:
            intersections.append(intersection)
        for intersection in maze_left.intersections:
            intersections.append(intersection)
        for intersection in maze_right.intersections:
            intersections.append(intersection)

        #Generating the big maze with the nest
        nest = intersections[0]
        big_maze = Maze(intersections,nest)
        
        #Still need the mirror part
        
        return big_maze
        
  
def test():
    maze=tower_hanoi(3)
    maze.show()
    print('NEST : ')
    maze.nest.show()
    

if __name__ == '__main__':
    test()

"""
def create_maze(m_map, m_paths={}):
    maze = Maze()
    # m(aze)_map defines the layout
    # returns m(aze)_paths a dictionary of paths, with their locations in m_map as their keys
    loc_map = np.transpose(np.nonzero(m_map))
    for loc in loc_map:
        loc = tuple(loc)
        new_intersection=Intersection(loc)      #Create a new intersection where there is a non zero value
        maze.add_intersection(new_intersection) #Add the intersection to the maze
      
            
    return 1
   
def add_path(self,start,end):
    path = Path(start,end)
    start.add_branch(path)
    end.add_branch(path)
           
        
    if loc[0]>0: 
        angle = 0  # some simple trig * path length
        if loc[0] > 0:
            parents = parent_check(m_map[loc[0]-1], loc)
        else:
            parents = []
        m_paths[loc] = Path(angle, loc, parents)
        for parent_loc in parents:
            m_paths[parent_loc].add_child(m_paths[loc])
    return m_paths


def parent_check(m, loc):
    # m = row of m_map to be searched for parents
    # loc = the location of the path
    # returns a list of tuples of parents locations
    locs = np.nonzero(m)[0]
    parents = []
    for l in locs:
        if l == loc[1]+1 or l == loc[1]-1:
            parents.append((loc[0]-1, l))
    return parents


new = [
    [0, 0, 0, 0, 99, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 2, 0, 2, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 2, 0, 0, 0, 2, 0, 0],
]

different = [
    [2],
    [2, 2],
    [2, 0, 2]
]

def test():
    # choose which test to run
    test_structure = np.array([
        [0, 1, 0],  # path to nest
        [1, 0, 1],  # path, path
        [0, 1, 0]  # path to food
    ])
    
    test_structure = np.array([
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 1, 0], # stretching
        [1, 0, 1, 0, 1, 0, 1],
        [0, 1, 0, 0, 0, 1, 0],  # stretching
        [0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0]
    ])
    
    a = create_maze(test_structure)
    print(a)
    for i in a:
        print(a[i].parents)


if __name__ == '__main__':
    test()
    
"""