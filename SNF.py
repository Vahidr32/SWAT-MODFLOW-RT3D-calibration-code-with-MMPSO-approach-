def SNF(DR,SNR,NSB,NSD):
    import numpy as np
    SN=np.NaN*np.empty(NSD)
    with open(DR, "r") as datafile:
        a=(datafile.read().split()[29::11])
    
    
    CCC=0
    for k in range(len(a)):
        if k==SNR:
            SN[CCC]=a[k]
            CCC+=1
            SNR+=NSB
        else:
            a[k]=[]
    return(SN)