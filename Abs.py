def Abs(DP,INF,NV):
    import numpy as np
    with open(DP+INF, "r") as datafile:
        AbsMin=(datafile.read().split()[4::3])
    with open(DP+INF, "r") as datafile:
        AbsMax=(datafile.read().split()[5::3])
    for i in range(NV):
        AbsMax[i]=float(AbsMax[i])
        AbsMin[i]=float(AbsMin[i])
    datafile.close()
    return(AbsMax, AbsMin)
