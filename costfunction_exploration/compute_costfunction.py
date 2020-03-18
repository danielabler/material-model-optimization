# ---------------------------------------------------------------------------------------------------------------------
# Intializes simulation by preparing the simulation domain and identifying target fields
# ---------------------------------------------------------------------------------------------------------------------

import os
from fenics.costfunction_exploration import config_study as config

# Ensure that directory exists
print("Current simulation directory '%s'"%config.sim_data_dir)
os.makedirs(config.sim_data_dir, exist_ok=True)

#-- Read Study parameters
parameters = config.get_study_parameters(config.sim_base_dir)

print(parameters)

print("Finished computation of cost function")