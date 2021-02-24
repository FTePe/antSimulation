from ant import *


def algorithm1(ant, path1, path2):
    if not path1 and not path2:
        ant.uturn()
    if not ant.fed:  # ant is unfed
        if not path1.foraging_pheromone and not path2.foraging_pheromone: #scouting
            ant.navigation = "alternative+directional"
            ant.lay_pheromone = "exploration"
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


def algorithm2(ant, path1, path2):
    # Single pheromone and directional navigation
    if not path1 and not path2:
        ant.uturn()
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
        if not path1.foraging_pheromone and not path2.foraging_pheromone:  # scouting
            navigation = "alternative"
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

