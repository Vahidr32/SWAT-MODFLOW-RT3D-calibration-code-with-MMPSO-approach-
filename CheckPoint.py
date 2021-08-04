def CheckPoint(P,It):
    
    from GWD import GWD
    import numpy as np
    from DirSM import DirSM
    
    DM, DBM, DP, DRR=DirSM()
    col,row,GW_Layers=GWD(DM)
    from Initialization import Initialization
    [NSB,NOP,MNIt,NSY,BYS,BJDS,EJDS,NYSKIP,C1I,C1F,C2I,C2F,RC,NG, NOW, NSD, SDate, FDate,NCores,MMPSO, TCir1, TCir2,DPI]=Initialization(DM=DM)
    Layer=1
    GWH=np.nan*np.ones([col,row,NSY-NYSKIP])
    
    with open(DP+"/particle"+str(P)+f'/swatmf_out_MF_head_yearly{It}.txt','r') as file:
        lines=file.readlines()
    for i in range(len(lines)):
        try:
            if lines[i].split()[0]=='year:' and lines[i].split()[1]=='2015':
                lineM=lines[i+2:i+2+col]
        except:
            'nothing'
    GWH=np.zeros([col,row])
    for i in range(col):
        GWH[i,0:row]=[float(x) if float(x)>-100 else np.nan for x in lineM[i].split()]

    if len(lines)<10:
        with open('/home/u1104091/SWAT-MODFLOW-HPC/SWAT-MODFLOW-PSO/Results/Checkpoint','a') as file:
            file.write('nan\n')
        return(np.nan)
    else:
        with open (DM+'/SWAT-MODFLOW-PSO/Particles/MODFLOW/NJMOD.dis','r') as file:
            lines=file.readlines()
            TE=np.zeros([col,row])
            d=1
            for i in range(col):
                c=0
                f=0
                while c<row:
                    try:
                        TE[i,c]=lines[51+d].split()[f]
                        f=f+1
                        c=c+1
                    except:
                           d=d+1
                           f=0
                d=d+1
        WT=GWH-TE
        a=[x if np.isnan(x)==False and x>10 else 0 for x in WT.flatten()]
        if a!=0:
            with open('/home/u1104091/SWAT-MODFLOW-HPC/SWAT-MODFLOW-PSO/Results/Checkpoint','a') as file:
                file.write(str((np.nansum(a)/(len([x for x in GWH.flatten() if np.isnan(x)==False]))))+'\n')
                #file.write(str((np.nansum(a)))+'\n') 

            return((np.nansum(a)/(len([x for x in GWH.flatten() if np.isnan(x)==False])))) 
        else:
             return(0)