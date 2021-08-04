def dsp(DP, AL, DVN):
    from GWD import GWD
    import numpy as np
    from DirSM import DirSM
    DM, DBM, D_P, DRR=DirSM()
    GW_rows, GW_Col,GW_Layers=GWD(DM)
    a=[]
    for i in range(GW_Layers):
        a.append(f'L{i+1}')
        
   
    LogDis=np.zeros(GW_Layers)
    for i in range(len(DVN)):
        if DVN[i].split('_')[0]=='LongDis':
            for j in range(GW_Layers):
                if DVN[i].split('_')[1]==a[j]:
                    LogDis[j]=AL[i]
          
        if DVN[i].split('_')[1]=='Hraio':
            Hraio=AL[i]
        if DVN[i].split('_')[1]=='Vratio':
            Vratio=AL[i]
        if DVN[i].split('_')[1]=='Eff':
            Eff=AL[i]
        
        
        
    txt = "{:2.6f}"
    
    
    with open(DM+"/NJMOD.dsp","r") as files:
        lines=files.readlines()
        
    for i in range(len(lines)):
        if "LONGITUDINAL" in lines[i]:
            for j in range(GW_Layers):
                lines[i+j+1]=f'         0 {txt.format(LogDis[j])}\n'
        if 'RATIO OF HORIZ' in lines[i]:
            lines[i+1]=f'         0 {txt.format(Hraio)}\n'
        if 'RATIO OF VERTIC' in lines[i]:
            lines[i+1]=f'         0 {txt.format(Vratio)}\n'
        if 'EFFECTIVE MOLECULAR' in lines[i]:
            lines[i+1]=f'         0 {txt.format(Eff)}\n'
            
            

    with open(DP+"/NJMOD.dsp","w") as files:
        for i in range(len(lines)):
            files.write(lines[i])
        