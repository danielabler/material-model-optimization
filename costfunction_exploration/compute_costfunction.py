# ---------------------------------------------------------------------------------------------------------------------
# Intializes simulation by preparing the simulation domain and identifying target fields
# ---------------------------------------------------------------------------------------------------------------------

import os
from costfunction_exploration import config_study as config

# Ensure that directory exists
print("Current simulation directory '%s'"%config.sim_data_dir)
os.makedirs(config.sim_data_dir, exist_ok=True)

#-- Read Study parameters
parameters = config.get_study_parameters(config.sim_base_dir)

#== DO SOMETHING =================================================
print(parameters)

test_output = {"sim_id"  : config.sim_id,
               "sim_dir" : config.sim_data_dir,
               "a_result": 10}

#== WRITE OUTPUT ==================================================
path_to_results = os.path.join(config.sim_data_dir, 'results.pkl')
import pandas as pd
dict_as_pandas = pd.Series(test_output)
dict_as_pandas.to_pickle(path_to_results)


print("Finished computation of cost function")
