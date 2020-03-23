import pathlib as pl
import pandas as pd
from costfunction_exploration import config_study as config
from pasty_local.pasty.parametric_study import ParametricStudy


varying_params = {"nu":      {'range' : [0.395, 0.455], "steps" : 2},
                  "mu":      {'range' : [0.2,0.8],      "steps" : 2},
                  "alpha":   {'range' : [-30,-20],      "steps" : 2}}

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
