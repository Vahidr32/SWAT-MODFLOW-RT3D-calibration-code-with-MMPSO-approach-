def RHO(D,OSNF,SDate,NSD):
    from datetime import datetime
    import numpy as np
    with open(D+OSNF, "r") as datafile:
        Date=(datafile.read().split()[0::2])
    with open(D+OSNF, "r") as datafile:
        OBS=(datafile.read().split()[1::2])    
    Observed=[]  
    for i in range(len(OBS)):
        Observed.append(float(OBS[i]))
    for i in range(len(Date)):
        OBSdate= datetime.strptime(Date[i],'%m/%d/%Y')
        if OBSdate==SDate:
            B=i
            break
    
    return(np.array(Observed[B:B+NSD]))
