def copyPSO(A):
    # Directory of the Agents
    from DirSM import DirSM
    DM, DBM, DP, DRR=DirSM()
    from distutils.dir_util import copy_tree
    import shutil
    import os
    with open(DM+'/SWAT-MODFLOW-PSO/Initialization.txt') as file:
        lines=file.readlines()
    for i in range(len(lines)):
        if 'Copy_Particles' in lines[i]:
            if float(lines[i].split()[0])==1:
                try:
                    shutil.copytree(DM , DP+"/particle"+str(A) ,ignore=shutil.ignore_patterns("SWAT-MODFLOW-PSO", "Backup"))
                except:
                    print("The folder for Particle{A} is already there")
    PD=DP+'/particle'+str(A)
    return (PD)
