import random

# Fixed Parameters - Table 2
F_max = 0.42     # Maximum flow of ants
F_0 = 0.0005     # Initial flow of ants
t_r = 127.4      # Recruitment time constant

v_mean = 0.861   # Average speed of ants
v_sd = 0.154     # Standard deviation of ant speed
t_f = 179.9      # Average time at food source

lambda_i = 0.006 # evaporation rate for pheromone

p_angle = 0.889  # Angular bias
phi_max = 90     # Tolerated angular deviation

t_eval = 10      # Network evaluation time
g = 0.8          # Constant in network definition

# Tuned Parameters - Table 3
q = 0            # Pheromone deposition (unfed) = ?
Q = 0            # Pheromone deposition (fed) = ?
w_dir = 0.9      # Weight of directional bias hwen scouting
w_alt = 1-w_dir  # Weight of alternative navigation when scouting = ?
w_fed = 0        # Weight of directional bias when fed ant scouts = ?
w_unfed = 0      # Weight of directional bias when unfed ant scouts = ?
alpha = 4        # Attraction of pheromone differences at branching points
k = 5            # Attraction of branch without pheromone



class Ant:
    def __init__(
            self
    ):
        self.fed = 0
        self.lay_pheromone = None
        self.max_angle = 90
        self.nest_angle = 0
        # Not sure which is more useful
        self.location = (0,0)  # where the ant is
        self.path = None  # what path the ant is on

    def override(self, path):
        if self.fed:
            return self.path_to_nest(path.angle) > self.max_angle

    def navigate(self, method, path1, path2):
        if method == "directional":
            angle1 = self.path_to_nest(path1.angle)
            angle2 = self.path_to_nest(path2.angle)
            if angle1 == angle2:
                return random.randint(0,1)
            elif random.random() <  p_angle:
                return angle1 < angle2
            else:
                return angle1 > angle2

        if method == "foraging pheromone":
            p1 = (k + path1.foraging_pheromone)**alpha
            p2 = (k + path2.foraging_pheromone)**alpha

            if random.random() < p1/(p1+p2):
                return 0
            else:
                return 1

        if method == "alternative":
            p1 = (k + path1.exploration_pheromone) ** alpha
            p2 = (k + path2.exploration_pheromone) ** alpha

            if random.random() < p1 / (p1 + p2):
                return 0
            else:
                return 1

        if method == "alternative+directional":
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

        return "method not known"

    def path_to_nest(self, angle):
        return abs(180*self.fed + angle - self.nest_angle)
