from ant_updated import *


def path_max(path1, path2, method):
    if method == "foraging_pheromone":
        if path1.foraging_pheromone > path2.foraging_pheromone:
            check = path1
        else:
            check = path2
        return check
    else:
        return "unknown method"


def algorithm1(ant):
    
    paths = []
    current = ant.current_inter
    previous = ant.previous_inter
    for neighbor in current.get_connections():
        if not neighbor.isequal(previous):
            path = current.get_path(neighbor)
            paths.append(path)
            
    if len(paths)>2:
        return "More than 2 options"
    
    elif len(paths) == 1:
        #print("Only 1 option")
        choice = paths[0]
        
    elif len(paths) == 0:
        ant.uturn()
        print("U-turn")
        
    else: #If we have two path
        
        path1 = paths[0]
        path2 = paths[1]
        
        if not ant.fed:
            # ant is unfed
            if not path1.foraging_pheromone and not path2.foraging_pheromone:
                # and is exploring
                ant.navigation = "alternative+directional"
                ant.lay_pheromone = "exploration"
            else:
                #following foraging route
                check = path_max(path1, path2, "foraging_pheromone")
                if ant.override(check):
                    ant.navigation = "directional"
                else:
                    ant.navigation = "foraging pheromone"
                ant.lay_pheromone = "foraging"
    
        else:  # ant is fed
            if not path1.foraging_pheromone and not path2.foraging_pheromone: #scouting
                ant.navigation = "alternative"
            else: #following foraging route
                if path1.foraging_pheromone > path2.foraging_pheromone:
                    check = path1
                else:
                    check = path2
                if ant.override(check):
                    ant.navigation = "directional"
                else:
                    ant.navigation = "foraging pheromone"
            ant.lay_pheromone = "foraging"
            
        #Choose a path        
        choice = paths[ant.navigate(path1,path2)] 
        
    ant.next_inter = current.get_neighbor(choice)
    
    reverse_choice = ant.next_inter.get_path(ant.current_inter)
    
    if ant.lay_pheromone == "foraging":
        if ant.fed:
            choice.foraging_pheromone += Q
            reverse_choice.foraging_pheromone += Q
            
        else:
            choice.foraging_pheromone += q
            reverse_choice.foraging_pheromone += q
    if ant.lay_pheromone == "exploration":
        if ant.fed:
            choice.exploration_pheromone += Q
            reverse_choice.exploration_pheromone += Q
        else:
            choice.exploration_pheromone += q
            reverse_choice.exploration_pheromone += q
        
    return ant.current_inter, ant.next_inter, ant.current_inter.get_path(ant.next_inter)



def algorithm2(ant):
    
    paths = []
    current = ant.current_inter
    previous = ant.previous_inter
    for neighbor in current.get_connections():
        if not neighbor.isequal(previous):
            path = current.get_path(neighbor)
            paths.append(path)
            
    if len(paths)>2:
        return "More than 2 options"
    
    elif len(paths) == 1:
        print("Only 1 option")
        choice = paths[0]
        
    elif len(paths) == 0:
        ant.uturn()
        print("U-turn")
        
    else: #If we have two path
        
        path1 = paths[0]
        path2 = paths[1]
    
        if not ant.fed:  # ant is unfed
            if not path1.foraging_pheromone and not path2.foraging_pheromone:  # scouting
                ant.navigation = "directional"
                ant.lay_pheromone = True
            else:  # following foraging route
                if path1.foraging_pheromone > path2.foraging_pheromone:
                    check = path1
                else:
                    check = path2
                if ant.override(check):
                    ant.navigation = "directional"
                else:
                    ant.navigation = "pheromone"
                ant.lay_pheromone = True
    
        else:  # ant is fed
            if path1.foraging_pheromone == 0 and path2.foraging_pheromone == 0:  # scouting
                ant.navigation = "pheromone"
            else:  # following foraging route
                if path1.foraging_pheromone > path2.foraging_pheromone:
                    check = path1
                else:
                    check = path2
                if ant.override(check):
                    ant.navigation = "directional"
                    print("PHEROMONE OVERRIDDEN")
                else:
                    ant.navigation = "pheromone"
            ant.lay_pheromone = True
        
        print(ant.navigation)
        choice = paths[ant.navigate(path1,path2)] 
        
    ant.next_inter = current.get_neighbor(choice)
    
    reverse_choice = ant.next_inter.get_path(ant.current_inter)
    
    if ant.lay_pheromone:
        if ant.fed:
            choice.foraging_pheromone += Q
            reverse_choice.foraging_pheromone += Q
            
        else:
            choice.foraging_pheromone += q
            reverse_choice.foraging_pheromone += q
    
        
    return ant.current_inter, ant.next_inter, ant.current_inter.get_path(ant.next_inter)

