

from ant import *
from maze import *
from algorithms import *
import simpy
import math

test_structure = np.array([
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0],  # stretching
    [1, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0],  # stretching
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
])

paths = create_maze(test_structure)


nest = (0, 3)
food = (6, 3)

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
num_ants = 1000
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





def ant_simulation(env, id):
    # Maybe add something at the beginning of the process to control how ants are entering the maze
    ant = Ant(nest, id)
    while ant.location != food:

        # When arriving at an intersection, the ant has to make a choice
        current = paths[ant.location]
        child_path = []
        child_path_location = []
        for i,e in enumerate(current.children):
            child_path.append(current.children[i])
            child_path_location.append(current.children[i].location)


        # algorithm1(ant, child_path)
        ant.location = random.choice(child_path_location)

        new = paths[ant.location]
        travelling_time = new.length/ant.speed

        print(' ant%s: %s %.3f s'% (ant.id, ant.location, env.now))
        yield env.timeout(travelling_time)


env = simpy.Environment()


env.process(flow(env))
# Run the simulation
env.run()


