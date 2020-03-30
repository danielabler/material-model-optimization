import os
from os import path
import pandas as pd

def GetRes(Directory):
    
    # List all folders
    Folders = os.listdir(Directory)
    
    # Data frame to store values
    Columns = ['Nu','Mu','Alpha','Cost']
    DataFrame = pd.DataFrame(columns=Columns, dtype='float64')
    
    for Folder in Folders:
        
        ResultsFile = os.path.join(Directory,Folder,'results.pkl')
        
        if path.exists(ResultsFile):
            
            Results = pd.read_pickle(ResultsFile)
            
            Nu                      = Results.Nu
            Mu                      = Results.Mu
            Alpha                   = Results.Alpha
            ConstitutiveModel       = Results.ConstitutiveModel
            NumberElements          = Results.NumberElements
            BCsType                 = Results.BCsType
            CompressionCostNoNorm   = Results.CompressionCostNoNorm
            TensileCostNoNorm       = Results.TensileCostNoNorm
            SimpleShearCostNoNorm   = Results.SimpleShearCostNoNorm
            TotalCostNoNorm         = Results.TotalCostNoNorm
            CompressionCostNormMax  = Results.CompressionCostNormMax
            TensileCostNormMax      = Results.TensileCostNormMax
            SimpleShearCostNormMax  = Results.SimpleShearCostNormMax
            TotalCostNormMax        = Results.TotalCostNormMax
            CompressionCostStep     = Results.CompressionCostStep
            TensileCostStep         = Results.TensileCostStep
            SimpleShearCostStep     = Results.SimpleShearCostStep
            TotalCostStep           = Results.TotalCostStep
            
        else:
            Nu                      = 'NaN'
            Mu                      = 'NaN'
            Alpha                   = 'NaN'
            ConstitutiveModel       = 'NaN'
            NumberElements          = 'NaN'
            BCsType                 = 'NaN'
            CompressionCostNoNorm   = 'NaN'
            TensileCostNoNorm       = 'NaN'
            SimpleShearCostNoNorm   = 'NaN'
            TotalCostNoNorm         = 'NaN'
            CompressionCostNormMax  = 'NaN'
            TensileCostNormMax      = 'NaN'
            SimpleShearCostNormMax  = 'NaN'
            TotalCostNormMax        = 'NaN'
            CompressionCostStep     = 'NaN'
            TensileCostStep         = 'NaN'
            SimpleShearCostStep     = 'NaN'
            TotalCostStep           = 'NaN'
            
        Simulation = {    'Nu'                      : Nu,
                          'Mu'                      : Mu,
                          'Alpha'                   : Alpha,
                          'ConstitutiveModel'       : ConstitutiveModel,
                          'NumberElements'          : NumberElements,
                          'BCsType'                 : BCsType,
                          'CompressionCostNoNorm'   : CompressionCostNoNorm,
                          'TensileCostNoNorm'       : TensileCostNoNorm,
                          'SimpleShearCostNoNorm'   : SimpleShearCostNoNorm,
                          'TotalCostNoNorm'         : TotalCostNoNorm,
                          'CompressionCostNormMax'  : CompressionCostNormMax,
                          'TensileCostNormMax'      : TensileCostNormMax,
                          'SimpleShearCostNormMax'  : SimpleShearCostNormMax,
                          'TotalCostNormMax'        : TotalCostNormMax,
                          'CompressionCostStep'     : CompressionCostStep,
                          'TensileCostStep'         : TensileCostStep,
                          'SimpleShearCostStep'     : SimpleShearCostStep,
                          'TotalCostStep'           : TotalCostStep}
        
        DataFrame = DataFrame.append(Simulation, ignore_index=True)
        
        os.remove(ResultsFile)
        
    return DataFrame	
