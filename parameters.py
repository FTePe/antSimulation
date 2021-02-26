# Values of Parameters used in the models

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
