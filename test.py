# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 16:33:48 2021

@author: moi
"""

# Test file

from ant import *
from maze import *
from algorithms import *
import simpy


test_structure = np.array([
        [0, 1, 0],  # path to nest
        [1, 0, 1],  # path, path
        [0, 1, 0]  # path to food
    ])
    
paths = create_maze(test_structure)
for i in paths:
    print("Parent location : ", paths[i].location)
    print("Children : ")
    for child in paths[i].children:
        print(child.location)


# print("ant location : ", ant.location, "speed = ", ant.speed)
nest = (0, 1)
food = (2, 1)


def flow(env):
    count = 0
    while count < 4:
        yield env.timeout(random.randint(5,10))
        # add ant
        # new_ant = Ant(nest, count)

        env.process(ant_simulation(env, count))
        count += 1


def ant_simulation(env, id):
    # Maybe add something at the beginning of the process to control how ants are entering the maze
    ant = Ant(nest, id)
    while ant.location != food:

        # When arriving at an intersection, the ant has to make a choice
        # current = paths[ant.location]
        # path1 = current.children[0]
        # path2 = current.children[1]
        # algorithm1(ant, path1, path2)
        ant.location = (ant.location[0]+1, ant.location[1])
        # Then we don't care about the ant until it reaches the new intersection
        # new = paths[ant.location]
        # travelling_time = new.length*ant.speed
        travelling_time = 15
        print('ant: ', ant.id, ant.location, env.now)
        yield env.timeout(travelling_time)


env = simpy.Environment()
# We can probably loop here to get the number of ants we want

env.process(flow(env))
# Run the simulation
env.run()


