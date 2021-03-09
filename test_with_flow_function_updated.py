

from ant_updated import *
from maze_classes import *
from algorithms_updated import *
import simpy
import math
import numpy as np
from tower_of_hanoi import *



# #Based on Eq.4, time step interval 1s
# r = 0.008 # not known, fraction of foraging ant
# num_ants = 1000
# F = []
# def flow(env):
#     count = 1
#
#     while count < num_ants:
#         time_ini  = env.now
#         yield env.timeout(random.randint(5,10))
#         time_lat = env.now
#         time_step = time_lat-time_ini
#         for i in range(time_step):
#             if len(F) == 0:
#                 F.append(F_0)
#             else:
#                 F.append(F[-1]+r*F[-1]*(1-F[-1]/F_max))
#
#             if sum(F)>count and count<=num_ants:
#                 print('ant: %d starts to explore maze at %d s' %(count,env.now-time_step+i))
#                 env.process(ant_simulation(env, count))
#                 count += 1
#


#Based on Eq.5
F = []
num_ants = 3
def flow(env):
    count = 1

    while count < num_ants:
        ti  = env.now
        yield env.timeout(random.randint(5,10))
        t = env.now
        time_step = t-ti
        for i in range(time_step):

            F.append(F_max/(1+(F_max/F_0-1)*math.exp(-t/t_r)))

            if sum(F)>count and count<=num_ants:
                print('ant: %d starts to explore maze at %d' %(count,env.now-time_step+i))
                env.process(ant_simulation(env, count))
                count += 1

#Maze definition

maze = mirror_hanoi(1)
nest = maze.get_intersection('up-top')
food = maze.get_intersection('down-top')
print(nest)



def ant_simulation(env, id):
    # Maybe add something at the beginning of the process to control how ants are entering the maze
    ant_start = env.now
    ant = Ant(nest, id)
    print(ant.previous_inter)
    while not ant.next_inter.isequal(food):#ant.location != food:
        # When arriving at an intersection, the ant has to make a choice
        ant.previous_inter = ant.current_inter
        ant.current_inter = ant.next_inter
        current_loc, next_loc, path = algorithm1(ant)
        #print('current type = ',type(current_loc), 'next_ type = ',type(next_loc))
        travelling_time = path.length/ant.speed

        print(' ant%s: heading from %s to %s using %s at time %.3f s'% (ant.id, ant.current_inter, ant.next_inter, path, env.now))
        yield env.timeout(travelling_time)
        print(' ant%s: arrived at %s at time %.3f s'% (ant.id, ant.next_inter, env.now))
        #maze.show()
    solving_time = env.now-ant_start
    print(' ant%s: found the food source after %.3f s travelling at speed %.2f m/s'% (ant.id, solving_time, ant.speed))


env = simpy.Environment()


env.process(flow(env))

env.run()
