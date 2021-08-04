def DelParticles(A):
    # Directory of the Agents
    from DirSM import DirSM
    DM, DBM, DP, DRR=DirSM()
    #from distutils.dir_util import copy_tree
    #copy_tree(DM, DP+"/particle"+str(A),preserve_mode=1)
    import shutil
    import os
    try:
        shutil.rmtree(DP+"/particle"+str(A))
        
    except:
           print('No folder need to be deleted')
