def btn(DM,DP,Poro_ly):
    
    from GWD import GWD
    row, col, layers=GWD(DM)
    import numpy as np
    txt = "{:1.2f}"
    with open(DM+"/SWAT-MODFLOW-PSO/Particles/MODFLOW/NJMOD.btn","r") as file: lines=file.readlines()
        
    for i in range(len(lines)):
        if 'POROSITY FOR EACH LAYER' in lines[i]:
            Gotta=i
            break
            
    for i in range(len(lines)):
        if 'ICBUND ARRAY' in lines[i]:
            ICBUN=i
            break
            
    with open(DP+"/NJMOD.btn","w") as file:
        for i in range(Gotta+1):
            file.write(lines[i])
        for k in range(layers):
            for i in range(row):
                for j in range(col):
                    if j<col-1:
                        file.write(txt.format(Poro_ly[k])+"\t")
                    else:
                        file.write(txt.format(Poro_ly[k])+"\n")
        
        for i in range(len(lines[ICBUN:-1])+1):
                file.write(lines[i+ICBUN])
            
        
        
        
   