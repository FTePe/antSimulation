from ant import *


def path_max(path1, path2, method):
    if method == "foraging_pheromone":
        if path1.foraging_pheromone > path2.foraging_pheromone:
            check = path1
        else:
            check = path2
        return check
    else:
        return "unknown method"


def algorithm1(ant, paths=[]):
    if len(paths) == 0:
        ant.uturn()
    elif len(paths) == 1:
        return paths[ant.forward()]
    elif len(paths) == 2:
        path1 = paths[0]
        path2 = paths[1]
        ant.path1 = path1
        ant.path2 = path2
        if not ant.fed:
            # ant is unfed
            if not path1.foraging_pheromone and not path2.foraging_pheromone:
                # and is exploring
                ant.navigation = "alternative+directional"
                ant.lay_pheromone = "exploration"

                return paths[ant.navigate(path1=path1, path2=path2)]
            else:
                ant.lay_pheromone = "foraging"
                #following foraging route
                check = path_max(path1, path2, "foraging_pheromone")
                if ant.override(check):
                    ant.navigation = "directional"

                    return paths[ant.navigate(path1=path1, path2=path2)]
                else:
                    ant.navigation = "foraging pheromone"

                    return paths[ant.navigate(path1=path1, path2=path2)]


        else:  # ant is fed
            if not path1.foraging_pheromone and not path2.foraging_pheromone: #scouting
                ant.navigation = "alternative"

                return paths[ant.navigate(path1=path1, path2=path2)]
            else: #following foraging route
                ant.lay_pheromone = "foraging"
                if path1.foraging_pheromone > path2.foraging_pheromone:
                    check = path1
                else:
                    check = path2
                if ant.override(check):
                    ant.navigation = "directional"

                    return paths[ant.navigate(path1=path1, path2=path2)]
                else:
                    ant.navigation = "foraging pheromone"

                    return paths[ant.navigate(path1=path1, path2=path2)]







