def Par_input(DP,INF):
    
    import numpy as np
    with open(DP+INF, "r") as datafile:
        VNum=(datafile.read().split()[7::7])
    with open(DP+INF, "r") as datafile:
        VN=(datafile.read().split()[8::7])
    with open(DP+INF, "r") as datafile:
        FileName=(datafile.read().split()[9::7])
    with open(DP+INF, "r") as datafile:
        MaxB=(datafile.read().split()[11::7])
    with open(DP+INF, "r") as datafile:
        Parameter=(datafile.read().split()[12::7])
    with open(DP+INF, "r") as datafile:
        MinB=(datafile.read().split()[13::7])
    with open(DP+INF, "r") as datafile:
        Grouping=(datafile.read().split()[10::7])
    for i in range(len(VN)):
        MaxB[i]=float(MaxB[i])
        Parameter[i]=float(Parameter[i])
        MinB[i]=float(MinB[i])
        VNum[i]=float(VNum[i])
    datafile.close()
    
    NV=len(VN)
    
    
    
    return(NV, VN,MaxB,Parameter,MinB,FileName, Grouping,VNum)
