from maze_classes import Path, Intersection, Maze
import numpy as np



def tower_hanoi(size,name='',flip=False): #Size is the number of pieces to move (must be int>=1)
    
    top = 'top'*(1-flip)+'bottom'*flip
    left = 'left'*(1-flip)+'right'*flip
    right = 'right'*(1-flip)+'left'*flip
    
    tl = 'tl'*(1-flip)+'br'*flip
    tr = 'tr'*(1-flip)+'bl'*flip
    lr = 'lr'*(1-flip)+'rl'*flip
    
    if size == 1:
        
        maze1 = Maze()
        
        #Create the path between intersections
        tl = Path(name+tl, 3, -(30-180*flip), -180*flip)  
        tr = Path(name+tr, 3, 30-180*flip, -180*flip)
        lr = Path(name+lr, 2, 30-180*flip, 180-30-180*flip)
        
        #Create intersections
        maze1.add_path(tl,name+top,name+left)
        maze1.add_path(tr,name+top,name+right)
        maze1.add_path(lr,name+left,name+right)
        
        return maze1
    
    else: #Recursively call the function at lower sizes
        
        big_maze = Maze()
        
        #Generate the lower order mazes
        maze_top = tower_hanoi(size-1,name+top+'-',flip)
        maze_left = tower_hanoi(size-1,name+left+'-',flip)
        maze_right = tower_hanoi(size-1,name+right+'-',flip)
        
        #Copy the intersections of the sub-mazes to the big maze
        big_maze.copy_intersections(maze_top)
        big_maze.copy_intersections(maze_left)
        big_maze.copy_intersections(maze_right)
        
        #Create the additional path between intersections
        tl = Path(name+tl+str(size), 3, -(30-180*flip), -180*flip)
        tr = Path(name+tr+str(size), 3, 30-180*flip, -180*flip)
        lr = Path(name+lr+str(size), 2, 30-180*flip, 180-30-180*flip)
        
        #Build the name to acces the maze linking intersections
        name_tl = name + top + ('-'+left)*(size-1)
        name_tr = name + top + ('-'+right)*(size-1)
        name_lt = name + left+ ('-'+top)*(size-1)
        name_rt = name + right+('-'+top)*(size-1)
        name_lr = name + left+('-'+right)*(size-1)
        name_rl = name + right+('-'+left)*(size-1)
        
        #Create the path of higher order   
        big_maze.add_path(tl,name_tl,name_lt)
        big_maze.add_path(tr,name_tr,name_rt)
        big_maze.add_path(lr,name_lr,name_rl)
        
        return big_maze
    

def mirror_hanoi(size):
    #Generating two symmetrical towers of hanoi
    maze_up = tower_hanoi(size,'up-',flip=False)
    maze_down = tower_hanoi(size,'down-',flip=True)
    
    #Generating the basis for the combination of both mazes above
    mirror_maze = Maze()
    mirror_maze.copy_intersections(maze_up)
    mirror_maze.copy_intersections(maze_down)
    
    #Defining the linking intersections
    up_left_link = 'up'+'-left'*size
    up_right_link = 'up'+'-right'*size
    down_left_link = 'down'+'-right'*size
    down_right_link = 'down'+'-left'*size
    link1 = Path('link1', 4, -30, 30)
    link2 = Path('link2', 4, 30, -30)
    
    #Addind the links
    mirror_maze.add_path(link1,up_left_link,down_right_link)
    mirror_maze.add_path(link2,up_right_link,down_left_link)
    
    return mirror_maze
    
def alternative_maze(size):
    #Generating two symmetrical towers of hanoi
    maze_up = tower_hanoi(size,'up-',flip=False)
    int_ul='up-left'+'-right'*(size-1)
    int_ur='up-right'+'-left'*(size-1)
    maze_up.remove_connection(maze_up.get_intersection(int_ul),maze_up.get_intersection(int_ur))
    
    maze_down = tower_hanoi(size,'down-',flip=True)
    int_dl='down-left'+'-right'*(size-1)
    int_dr='down-right'+'-left'*(size-1)
    maze_down.remove_connection(maze_down.get_intersection(int_dl),maze_down.get_intersection(int_dr))
    
    
    #Generating the basis for the combination of both mazes above
    alternative_maze = Maze()
    alternative_maze.copy_intersections(maze_up)
    alternative_maze.copy_intersections(maze_down)
    
    
    #Defining the linking intersections
    mid_up_mid_down = Path('mid_up_mid_down',2,0,0)
    mid_up_left = Path('mid_up_left',1,-150,-150)
    mid_up_right = Path('mid_up_right',1,150,150)
    
    mid_down_left = Path('mid_down_left',1,-30,-30)
    mid_down_right = Path('mid_down_right',1,30,30)
    
    alternative_maze.add_path(mid_up_mid_down,'middle_up','middle_down')
    alternative_maze.add_path(mid_up_left,'middle_up',int_ul)
    alternative_maze.add_path(mid_up_right,'middle_up',int_ur)
    alternative_maze.add_path(mid_down_left,'middle_down',int_dl)
    alternative_maze.add_path(mid_down_right,'middle_down',int_dr)
    
    
    return alternative_maze
  
def test():
    """
    #Simple tower of hanoi
    maze=tower_hanoi(2,flip=True)
    maze.show()
    maze=tower_hanoi(2,flip=False)
    maze.show()
    """
    
    #Experiment set up
    maze = mirror_hanoi(1)
    maze.show()
    a=maze.get_intersection('down-left')
    b=maze.get_intersection('up-left')
    path = a.get_path(b)
    print(path.name)
    print(path.start_angle)


if __name__ == '__main__':
    test()