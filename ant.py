import random
import numpy as np
from parameters import *


class Ant:
    def __init__(
            self,
            nest,
            name
    ):
        self.id = name
        self.previous_inter
        self.current_inter
        self.next_inter
        self.fed = 0
        self.lay_pheromone = None
        self.nest_angle = 0
        # Not sure which is more useful
        self.location = nest  # where the ant is
        #We should add the speed too
        self.speed = np.random.normal(v_mean, v_sd)
        self.navigation = "default"

    def path_to_nest(self, angle):
        return abs(180*self.fed + angle - self.nest_angle)

    def override(self, path):
        # checks the path is heading in desired direction
        return self.path_to_nest(path.angle) > phi_max

    def navigate(self, path1, path2):
        # determines which path is chosen dependant on the navigation method
        if self.navigation == "directional":
            angle1 = self.path_to_nest(path1.angle)
            angle2 = self.path_to_nest(path2.angle)
            if angle1 == angle2:
                return random.randint(0, 1)
            elif random.random() < p_angle:
                return angle1 < angle2
            else:
                return angle1 > angle2

        if self.navigation == "foraging pheromone":
            p1 = (k + path1.foraging_pheromone)**alpha
            p2 = (k + path2.foraging_pheromone)**alpha

            if random.random() < p1/(p1+p2):
                return 0
            else:
                return 1

        if self.navigation == "alternative":
            p1 = (k + path1.exploration_pheromone) ** alpha
            p2 = (k + path2.exploration_pheromone) ** alpha

            if random.random() < p1 / (p1 + p2):
                return 0
            else:
                return 1

        if self.navigation == "alternative+directional":
            angle1 = self.path_to_nest(path1.angle)
            angle2 = self.path_to_nest(path2.angle)
            if angle1 == angle2:
                p_dir = 0.5
            elif angle1 > angle2:
                p_dir = p_angle
            else:
                p_dir = 1 - p_angle
            p1 = (k + path1.exploration_pheromone) ** alpha
            p2 = (k + path2.exploration_pheromone) ** alpha
            p_ph = p1/(p1+p2)
            p_e = 0.5 - w_alt*(p_ph - 0.5) + w_dir*(p_dir - 0.5)

            if random.random() < p_e:
                return 0
            else:
                return 1

        return "unknown method"


