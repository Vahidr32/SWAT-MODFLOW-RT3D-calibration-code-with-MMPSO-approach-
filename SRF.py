def SRF(DR,SNR,NSB,NSD):
    import numpy as np
    SR=[]
    with open(DR, "r") as datafile:
        a=(datafile.read().split()[27::11])

    for k in range(len(a)):
        if k==SNR:
            SR.append(a[k])
            SNR+=NSB
        else:
            a[k]=[] 
    if len(SR)==NSD:
        return(SR)            
    else:
        SR=np.NaN*np.empty([NSD])
        return(SR)
        