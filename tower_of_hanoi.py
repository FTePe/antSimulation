from maze_classes import Path, Intersection, Maze
import numpy as np



def tower_hanoi(size,name='',depth=0): #Size is the number of pieces to move (must be int>=1)
    
    if size == 1:
        
        maze1 = Maze()
        
        #Create the path between intersections
        tl = Path(name+'tl', 3, -30, 0)  
        tr = Path(name+'tr', 3, 30, 0)
        lr = Path(name+'lr', 2, 30, 180-30)
        
        #Create intersections
        maze1.add_path(tl,name+'top',name+'left')
        maze1.add_path(tr,name+'top',name+'right')
        maze1.add_path(lr,name+'left',name+'right')
        
        return maze1
    
    else: #Recursively call the function at lower sizes
        
        big_maze = Maze()
        
        #Generate the lower order mazes
        maze_top = tower_hanoi(size-1,name+'top-',depth+1)
        maze_left = tower_hanoi(size-1,name+'left-',depth+1)
        maze_right = tower_hanoi(size-1,name+'right-',depth+1)
        
        #Copy the intersections of the sub-mazes to the big maze
        big_maze.copy_intersections(maze_top)
        big_maze.copy_intersections(maze_left)
        big_maze.copy_intersections(maze_right)
        
        #Create the additional path between intersections
        tl = Path(name+'tl'+str(size), 3, -30, 0)
        tr = Path(name+'tr'+str(size), 3, 30, 0)
        lr = Path(name+'lr'+str(size), 2, 30, 180-30)
        
        #Build the name to acces the maze linking intersections
        name_tl = name+'top'+'-left'*(size-1)
        name_tr = name+'top'+'-right'*(size-1)
        name_lt = name+'left'+'-top'*(size-1)
        name_rt = name+'right'+'-top'*(size-1)
        name_lr = name+'left'+'-right'*(size-1)
        name_rl = name+'right'+'-left'*(size-1)
        
        #Create the path of higher order   
        big_maze.add_path(tl,name_tl,name_lt)
        big_maze.add_path(tr,name_tr,name_rt)
        big_maze.add_path(lr,name_lr,name_rl)
        
        return big_maze

def mirror_hanoi(size):
    #Generating two symmetrical towers of hanoi
    maze_up = tower_hanoi(size,'up-')
    maze_down = tower_hanoi(size,'down-')
    
    #Generating the basis for the combination of both mazes above
    mirror_maze = Maze()
    mirror_maze.copy_intersections(maze_up)
    mirror_maze.copy_intersections(maze_down)
    
    #Defining the linking intersections
    up_left_link = 'up'+'-left'*size
    up_right_link = 'up'+'-right'*size
    down_left_link = 'down'+'-left'*size
    down_right_link = 'down'+'-right'*size
    link1 = Path('link1', 4, -30, 30)
    link2 = Path('link2', 4, 30, -30)
    
    #Addind the links
    mirror_maze.add_path(link1,up_left_link,down_right_link)
    mirror_maze.add_path(link2,up_right_link,down_left_link)
    
    return mirror_maze
    
    
  
def test():
    #Simple tower of hanoi
    maze=tower_hanoi(3)
    maze.show()
    
    #Experiment set up
    maze = mirror_hanoi(2)
    maze.show()
    

if __name__ == '__main__':
    test()