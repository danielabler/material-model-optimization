from config import *

import os
import json
import pathlib as pl


#=======================================================================================================================
# FUNCTIONS
#=======================================================================================================================

def load_parameter_file(path_to_file):
    p_params = pl.Path(path_to_file)
    if p_params.exists():
        print("Loading parameters from '%s'"%p_params)
        parameters = json.loads(p_params.read_text())
        return parameters
    else:
        print("Cannot load parameters from '%s'"%p_params)


def create_sim_dir_name(material_model, n_elements):
    experiment_name = "%s_elements-%i"%(material_model, n_elements)
    return experiment_name


def get_study_parameters(sim_base_dir=None):
    if not sim_base_dir and 'PATH_SIM_BASE_DIR' in os.environ:
        sim_base_dir = os.environ['PATH_SIM_BASE_DIR']
    p_params = pl.Path(sim_base_dir).parent.joinpath('experiment_params.py')
    parameters = load_parameter_file(p_params)
    return parameters

def get_parameters(sim_dir=None):
    p_params = pl.Path(sim_dir).joinpath('params.py')
    parameters = load_parameter_file(p_params)
    return parameters

#=======================================================================================================================
# Settings
#=======================================================================================================================

material_model = 'neo-hookean'
n_elements = 10

max_sim_time = "00:10:00"
max_sim_memory = "2G"

#=======================================================================================================================
# JOB SUBMISSION SETTINGS
#=======================================================================================================================
code_base_dir = os.path.dirname(__file__)
path_slurm_job_template = os.path.join(code_base_dir, 'slurm_array_job_template_ubelix.sh')

jobfile_params   = {'VAR_PATH_CODE_GLIMSLIB'    : base_path,
                    'VAR_PATH_CODE_EXPERIMENT'  : code_base_dir,
                    'VAR_PATH_SINGULARITY_IMAGE': path_glimslibants2017,
                    'VAR_MAX_CPU_TIME'          : max_sim_time,
                    'VAR_MAX_CPU_MEMORY'        : max_sim_memory }


#=======================================================================================================================
# COLLECT ALL SETTINGS
#=======================================================================================================================

sim_dir_name = create_sim_dir_name(material_model, n_elements)
sim_base_dir = os.path.join(path_experiments_base, 'material-model-optimization', sim_dir_name)

parameters = {}
parameters['experiment_name'] = sim_dir_name
parameters['sim_base_dir']    = sim_base_dir
parameters['jobfile_params']  = jobfile_params


#=======================================================================================================================
# SET PARAMETERS WHEN CALLED FROM ARRAY JOB
#=======================================================================================================================

if 'PATH_SIM_DIR' in os.environ:                        # directory of simulation
    sim_data_dir = os.environ['PATH_SIM_DIR']
else:
    sim_data_dir = ""

if 'PATH_SIM_BASE_DIR' in os.environ:                   # direcetory of simulation study
    sim_base_dir = os.environ['PATH_SIM_BASE_DIR']

if 'SIM_ID' in os.environ:
    sim_id = os.environ['SIM_ID']

if 'TIME_STEP' in os.environ:
    time_step = os.environ['TIME_STEP']
