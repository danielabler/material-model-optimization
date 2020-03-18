import pathlib as pl
import pandas as pd
from fenics.costfunction_exploration import config_study as config
from pasty_local.pasty.parametric_study import ParametricStudy


varying_params = {"D_WM":      {'range' : [0.05, 0.4], "stepsize" : 0.05},
                  "rho_WM":    {'range' : [0,1], "steps" : 1},
                  "coupling":  {'range' : [0.05,0.3], "stepsize" : 0.05}}

ps = ParametricStudy(config.parameters['sim_base_dir'], varying_params)
ps.config['id_format']= '%04d'
ps.config['name'] = config.parameters['experiment_name']
ps.create_parameter_table()
ps.generate_simulation_folder_structure(with_param_files=True,
                                        with_template_files=False,
                                        exist_ok=True, verbose=True)
ps.submit_array_job(config.path_slurm_job_template,
                    job_params=config.parameters['jobfile_params'], n_concurrent=100)
ps.save_state()

# extract other parameter at generation time
path_to_params = pl.Path(config.sim_base_dir).joinpath('experiment_params.py')
path_to_params.write_text(pd.Series(config.parameters).to_json())
print("===== ", path_to_params)