# ---------------------------------------------------------------------------------------------------------------------
# Intializes simulation by preparing the simulation domain and identifying target fields
# ---------------------------------------------------------------------------------------------------------------------

import os
from costfunction_exploration import config_study as config
import FEniCS.Tests.SimpleFunctions as sf

# Ensure that directory exists
print("Current simulation directory '%s'"%config.sim_data_dir)
os.makedirs(config.sim_data_dir, exist_ok=True)

#-- Read Study parameters
study_parameter_dict = config.get_study_parameters(config.sim_base_dir)

#-- Read current parameter
parameter_dict = config.get_parameters(config.sim_data_dir)

print(parameter_dict)

#== DO SOMETHING =================================================

parameter_list = [parameter_dict["nu"], parameter_dict["mu"], parameter_dict["alpha"] ]

# Optimization Parameters
ConstitutiveModels = ['Ogden', 'Neo-Hookean']
ConstitutiveModel = ConstitutiveModels[0]

BCsTypes = ['Ideal', 'Fixed']
BCsType  = BCsTypes[1]

NumberElementsTested = [1, 2, 3, 5, 10, 20]
NumberElements = NumberElementsTested[5]

LoadCases = ['Compression', 'Tension', 'SimpleShear']
RelativeWeights = [1,1,1]


# Simulation parameters
FinalRelativeStretch = 0.1
RelativeStepSize     = 0.02

cost = sf.CostFunction(parameter_list, ConstitutiveModel, BCsType, NumberElements, LoadCases, RelativeWeights, FinalRelativeStretch, RelativeStepSize)

#== WRITE OUTPUT ==================================================
test_output = {"sim_id"  : config.sim_id,
               "sim_dir" : config.sim_data_dir,
               "cost": cost}

path_to_results = os.path.join(config.sim_data_dir, 'results.pkl')
import pandas as pd
dict_as_pandas = pd.Series(test_output)
dict_as_pandas.to_pickle(path_to_results)


print("Finished computation of cost function")
