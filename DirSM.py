def DirSM():
    import os
    f=open(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))+'/Directory.txt')
    lines=f.readlines()
    
    DM=[]
    DBM=[]
    DP=[]
    DRR=[]
    for i in range(len(lines)):
        if 'DM' in lines[i]:
            DM=lines[i].split()[1]
            
        if 'DBM' in lines[i]:
            DBM=lines[i].split()[1]         
        
        if 'DP' in lines[i]:
            DP=lines[i].split()[1]
            
        if 'DRR' in lines[i]:
            DRR=lines[i].split()[1]
    return(DM, DBM, DP, DRR)