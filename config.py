import os
import sys
import socket

hostname = socket.gethostname()

#== GENERAL PATHS
if hostname.startswith("submit") or hostname.startswith("knode") or hostname.startswith("anode") or hostname.startswith("hnode") or hostname.startswith("jnode"):
    path_home = "/home/ubelix/artorg/abler"
    path_singularity = os.path.join(path_home, 'singularity')
    path_experiments_base = os.path.join(path_home, 'SIMULATIONS')
    path_to_repos = os.path.join(path_home, "repositories", "material-model-optimization")
    name_slurm_job_template = "slurm_array_job_template_ubelix.sh"
else: # local
    path_to_repos = "/opt/project/"
    path_experiments_base = os.path.join(path_to_repos, 'SIMULATIONS')

path_glimslibants2017 = os.path.join(path_singularity, 'libadjoint-2017-2_ants_meshtool.img')

base_path = os.path.dirname(__file__)

if not os.path.exists(path_experiments_base):
    os.mkdir(path_experiments_base)

# add paths to glimslib, pasty_local
sys.path.append(path_to_repos)
path_to_pasty = os.path.join(path_to_repos, "pasty_local")
sys.path.append(path_to_pasty)







