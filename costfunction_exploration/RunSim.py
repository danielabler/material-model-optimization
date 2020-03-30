import init as In
import postprocess as PP
import GetResults as GR
import pandas as pd
import numpy as np
import time
import os


Directory = '/gpfs/homefs/artorg/ms20s284/SIMULATIONS/material-model-optimization/neo-hookean_elements-10/simulations/'
Values = pd.read_csv('costfunction_exploration/Ranges.txt', sep=',', decimal='.')
LastFile = 'sftp://ms20s284@submit.unibe.ch/gpfs/homefs/artorg/ms20s284/SIMULATIONS/material-model-optimization/neo-hookean_elements-10/simulations/sim_1330/results.pkl'


for Iteration in range(0,len(Values),2):
    
    NuVal = [Values.loc[Iteration].Nu, Values.loc[Iteration+1].Nu]
    MuVal = [Values.loc[Iteration].Mu, Values.loc[Iteration+1].Mu]
    AlVal = [Values.loc[Iteration].Alpha, Values.loc[Iteration+1].Alpha]
    
    In.Initialization(NuVal,MuVal,AlVal)
    
    PP.main('analyze')
    
    while not os.path.exists(LastFile):
        time.sleep(60)
        
    DataFrame = GR.GetRes(Directory)
    
    # Save Table
    DataFrame.to_csv('Results' + str(Iteration)  + '.csv', index=False)
