from costfunction_exploration import config_study as config
from pasty_local.pasty.parametric_study import ParametricStudy

import os
import pandas as pd
import pathlib as pl
import sys, getopt
from itertools import product


def analyze(base_dir):
    print("-- Analyzing '%s'" % base_dir)
    p_params = pl.Path(base_dir).joinpath('experiment_params.py')
    params = config.load_parameter_file(p_params)
    ps = ParametricStudy(base_dir)
    ps.reload_state()
    ps.config['results_file_name'] = "results.pkl"
    ps.collect_results(verbose=True)
    ps.save_state()


def main(argv):

    #-- ITERATE THROUGH FOLLOWING PARAMETER COMBINATIONS
    material_models    = ['neo-hookean']
    number_of_elements = [1, 10]
    param_combinations = product(*[material_models, number_of_elements ])
    

    try: 
        opts, args = getopt.getopt(argv, "hm:",["mode="])
    except getopt.GetoptError:
        print("postprocess.py -m <mode>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print("postprocess.py -m <mode>")
            sys.exit()
        elif opt in ("-m", "--mode"):
            mode = arg.strip()

    for params in param_combinations:
        material_model, n_elements = params
        experiment_name = config.create_sim_dir_name(material_model, n_elements)
        sim_base_dir = os.path.join(config.path_experiments_base, 'material-model-optimization', experiment_name)
        if os.path.exists(sim_base_dir):
            print("=====================================================================")
            print("==== %s " % experiment_name)
            print("=====================================================================")
        
            if mode == 'analyze':
                analyze(sim_base_dir)
            else:
                print("== Path '%s' does not exist"%sim_base_dir)


if __name__ == "__main__":
    main(sys.argv[1:])
