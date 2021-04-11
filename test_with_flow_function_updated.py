

from ant_updated import *
from maze_classes import *
from algorithms_updated import *
import simpy
import math
import numpy as np
from tower_of_hanoi import *
import matplotlib.pyplot as plt


size = 2
maze = mirror_hanoi(size)
nest_name = 'up'+'-top'*size
food_name = 'down'+'-bottom'*size
nest = maze.get_intersection(nest_name)
food = maze.get_intersection(food_name)
print(nest)




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
num_ants = 10


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
    evap.interrupt()


def evaporation(env,maze):
    go_on = True
    while go_on:
        try :
            for path in maze.get_all_paths():
                path.foraging_pheromone -= lambda_i*path.foraging_pheromone
                path.exploration_pheromone -= lambda_i*path.exploration_pheromone
                if path.foraging_pheromone < 0:
                    path.foraging_pheromone = 0
                if path.exploration_pheromone < 0:
                    path.exploration_pheromone = 0
            yield env.timeout(1) 
            print('PHEROMONE')
        except simpy.Interrupt:
            print("END")
            go_on = False

#time_in_maze=np.zeros(num_ants+1)
time_in_maze = []

def ant_simulation(env, id):
    
    
    ant = Ant(nest, id)
    ant_start = env.now
    
    #Ant moves to the food source
    while not ant.next_inter.isequal(food):#ant.location != food:
        #Update the position of the ant
        ant.previous_inter = ant.current_inter
        ant.current_inter = ant.next_inter
        
        #Look for the next position
        current_loc, next_loc, path = algorithm2(ant)
        
        #Travel along the path
        travelling_time = path.length/ant.speed
        print('   ant%s: heading from %s to %s at time %.3f s'% (ant.id, ant.current_inter, ant.next_inter, env.now))
        
        yield env.timeout(travelling_time)
        
    time_to_food = env.now-ant_start
    print(' ant%s: FOUND the food source after %.3f s travelling at speed %.2f m/s'% (ant.id, time_to_food, ant.speed))
    
    #Reset the memory of the ant so that we can use the same path to go to the food source and come back
    ant.previous_inter = food
    ant.current_inter = food
    
    #ant is eating
    yield env.timeout(t_f)
    ant.fed = 1
    
    #Ant comes back to nest
    while not ant.next_inter.isequal(nest):#ant.location != nest:
        #Update the position of the ant
        ant.previous_inter = ant.current_inter
        ant.current_inter = ant.next_inter
        
        #Look for next position
        current_loc, next_loc, path = algorithm2(ant)
        
        #Travel along the path
        travelling_time = path.length/ant.speed
        print('   ant%s: heading from %s to %s at time %.3f s'% (ant.id, ant.current_inter, ant.next_inter, env.now))
        
        yield env.timeout(travelling_time)
        
    time_to_come_back = env.now-ant_start
    print(' ant%s: CAME BACK to nest after %.3f s travelling at speed %.2f m/s'% (ant.id, time_to_come_back, ant.speed))
    #time_in_maze[id]=time_to_come_back
    time_in_maze.append(time_to_come_back)



env = simpy.Environment()

evap = env.process(evaporation(env,maze))

env.process(flow(env))

env.run()

mean = np.mean(time_in_maze)
std = np.std(time_in_maze)
print('Mean solving time = %.2f s, standard deviation = %.2f s' %(mean,std))

plt.hist(time_in_maze,bins=10)
plt.show()
