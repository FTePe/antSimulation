# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 16:33:48 2021

@author: moi
"""

#Test file

from ant import *
from maze import *
from algorithms import *
import simpy

ant = Ant()

test_structure = np.array([
        [0, 1, 0],  # path to nest
        [1, 0, 1],  # path, path
        [0, 1, 0]  # path to food
    ])
    
a = create_maze(test_structure)
for i in a:
    print("Parent location : ",a[i].location)
    print("Children : ")
    for child in a[i].children:
        print(child.location)

nest = (0,1)
food = (2,1)
ant.path = a[nest]

print("ant location : ", ant.path.location, "speed = ", ant.speed)



def ant_simulation(env):
    #Maybe add something at the beginning of the process to control how ants are entering the maze
    while ant.path != food:
        #When arriving at an intersection, the ant has to make a choice
        current = ant.path
        path1 = current.children[0]
        path2 = current.children[1]
        algorithm1(ant,path1,path2)
        #Then we don't care about the ant until it reaches the new intersection
        travelling_time = ant.path.length*ant.speed
        yield env.timeout(travelling_time)

env = simpy.Environment()
#We can probably loop here to get the number of ants we want
env.process(ant_simulation(env))
#Run the simulation
env.run()


