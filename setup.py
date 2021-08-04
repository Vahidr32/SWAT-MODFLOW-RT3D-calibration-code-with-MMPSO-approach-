import os 
from distutils.dir_util import copy_tree
import shutil
CL = os.path.dirname(os.path.abspath(__file__))
DSSWAT=os.path.dirname(CL)+'/SWAT-MODFLOW-RT3D'

with open(DSSWAT+'/file.cio','r') as file:
    lines=file.readlines()
    for i in range(len(lines)):
        if 'Reach output variables' in lines[i]:
            lines[i+1]='   2   6 13   14   9    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0\n'
with open(DSSWAT+'/file.cio','w') as file:
    for i in range(len(lines)):
        file.write(lines[i])

DMOD=os.path.dirname(CL)+'/MODFLOW'
SWATMODFLOWHPC=os.path.dirname(CL)+'/SWAT-MODFLOW-HPC'
os.mkdir(SWATMODFLOWHPC)
copy_tree(DSSWAT, SWATMODFLOWHPC,preserve_mode=0)
SWATMODFLOWPSO=SWATMODFLOWHPC+'/SWAT-MODFLOW-PSO'
os.mkdir(SWATMODFLOWPSO)
copy_tree(CL+'/ProgramFiles/Initializationfiles', SWATMODFLOWPSO,preserve_mode=0)
Baseflow=SWATMODFLOWPSO+'/Baseflow'
os.mkdir(Baseflow)
copy_tree(CL+'/ProgramFiles/baseflow', Baseflow,preserve_mode=0)
CA_PSO=SWATMODFLOWPSO+'/CA-PSO'
os.mkdir(CA_PSO)
copy_tree(CL, CA_PSO,preserve_mode=0)
shutil.rmtree(CA_PSO+"/ProgramFiles")
Results=SWATMODFLOWPSO+'/Results'
os.mkdir(Results)
Observation=SWATMODFLOWPSO+'/Observation'
os.mkdir(Observation)
Particles=SWATMODFLOWPSO+'/Particles'
os.mkdir(Particles)
MODFLOW=Particles+'/MODFLOW'
os.mkdir(MODFLOW)
copy_tree(DMOD, MODFLOW,preserve_mode=0)
print('the SWAT-MODFLOW-HPC is ready to be transfered to your HPC account'