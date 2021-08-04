def RHS(DR, NSD, NOW, Col):
    import numpy as np
    with open(DR, "r") as file:
        lines=file.readlines()
        Sim=[]
        for i in range(1,len(lines)):
            Sim.append(float(lines[i].split()[int(Col-1)]))
        Sim=np.reshape(Sim, -1)
    if len(Sim)==NSD:
        return (Sim[NOW:NSD])
    else:
        Sim=np.NaN*np.empty([NSD-NOW])
        return (Sim)