def InitialHead(DP, It,PP):
    from Initialization import Initialization
    from DirSM import DirSM
    import numpy as np
    from MNAME import MNAME
    MNAME=MNAME()
    DM, DBM, DP_P, DRR=DirSM()
    [NSB,NOP,MNIt,NSY,BYS,BJDS,EJDS,NYSKIP,C1I,C1F,C2I,C2F,RC,NG, NOW, NSD, SDate, FDate,NCores,MMPSO, TCir1, TCir2,DPI]=Initialization(DM=DM)
    with open(DM+'/SWAT-MODFLOW-PSO/Initialization.txt','r') as file:
        lines=file.readlines()
        for i in range(len(lines)):
            if 'GW_rows' in lines[i]:
                col=int(lines[i].split()[0])
            if 'GW_Col' in lines[i]:
                row=int(lines[i].split()[0])
    txt = "{:3.7E}"
    NIH=np.zeros([col,row])
    GWHF=np.nan*np.ones([col,row])
    IH=np.nan*np.zeros([col,row])
    
    ###Reading the TOP Elevation
    with open(DP+f'/{MNAME}.dis', 'r') as file:
        liness=file.readlines()
    Layers=[]
    for i in range(len(liness)):
        if "INTERNAL" in liness[i]:
            Layers.append(i)
    TOP=Layers[2]
    MID=Layers[3]
    BOT=Layers[4]
    DEP=Layers[5]
    TOP_E=[]
    MID_E=[]
    BOT_E=[]
    DEP_E=[]

    for i in range(TOP+1,MID):
        for j in range(len(liness[i].split())):
            TOP_E.append(float(liness[i].split()[j]))
    for i in range(MID+1,BOT):
        for j in range(len(liness[i].split())):
            MID_E.append(float(liness[i].split()[j]))
    for i in range(BOT+1,DEP):
        for j in range(len(liness[i].split())):
            BOT_E.append(float(liness[i].split()[j]))
    for i in range(DEP+1,len(liness)-1):
        for j in range(len(liness[i].split())):
            DEP_E.append(float(liness[i].split()[j]))

    TOP_E=np.reshape(TOP_E,[col,row])
    MID_E=np.reshape(MID_E,[col,row])
    BOT_E=np.reshape(BOT_E,[col,row])
    DEP_E=np.reshape(DEP_E,[col,row])
    #### Reading final head
    with open(DP+f'/swatmf_out_MF_head_yearly{It}.txt') as file:
        lines=file.readlines()
        Layer=1
        for y in range(NSY-1,NSY):
            print(BYS+y)
            for i in range(len(lines)):
                if "year" in lines[i] and float(lines[i].split()[1])==BYS+y:
                    for m in range(row*Layer):
                        if "layer" in lines[i+m+1] and float(lines[i+m+1].split()[1])==Layer:
                            for j in range(col):
                                for k in range(row):
                                    if float(lines[i+j+2+m].split()[k])>-100:
                                        GWHF[j,k]=float(lines[i+j+2+m].split()[k])
                                    else:
                                        GWHF[j,k]=np.nan
    ### Reading Initial head
    with open(DP+f'/{MNAME}.bas','r') as file:
        lines=file.readlines()
        for i in range(len(lines)):
            if "HNOFLO" in lines[i]:
                d=1
                for j in range(col):
                    c=0
                    f=0
                    while c<row:
                        try:
                            IH[j,c]=float(lines[i+1+d].split()[f])
                            f=f+1
                            c=c+1
                        except:
                            d=d+1
                            f=0
                    d=d+1     
    ##Making new initial head
    NIH=np.nan*np.zeros([col,row])
    for i in range(col):
        for j in range(row):
            if GWHF[i,j]<=TOP_E[i,j] and GWHF[i,j]>MID_E[i,j] and  np.isnan(GWHF[i,j])==False: 
                NIH[i,j]=GWHF[i,j]
            if GWHF[i,j]<=MID_E[i,j] and  np.isnan(GWHF[i,j])==False:
                NIH[i,j]=IH[i,j]
            if GWHF[i,j]>TOP_E[i,j] and  np.isnan(GWHF[i,j])==False:
                NIH[i,j]=MID_E[i,j]+((TOP_E[i,j]-MID_E[i,j])/30)
    c=0
    while c<5:
        for i in range(col):
            for j in range(row):
                a=[]
                for m in [-2,-1,0,1,2]:
                    for n in [-2,-1,0,1,2]:
                        try:
                            if np.isnan(NIH[i+m,j+n])==False:
                                a.append(NIH[i+m,j+n])
                        except:
                               'no cell'
                if len(a)>0:
                    NIH[i,j]=np.nanmean(a)
        
        for i in range(col):
            for j in range(row):
                if np.isnan(GWHF[i,j])==False and NIH[i,j]>TOP_E[i,j]+4:
                    NIH[i,j]=MID_E[i,j]+((TOP_E[i,j]-MID_E[i,j])/30)
                if np.isnan(GWHF[i,j])==False and NIH[i,j]>TOP_E[i,j] and NIH[i,j]<=TOP_E[i,j]+4:
                    NIH[i,j]=TOP_E[i,j]
                if np.isnan(GWHF[i,j])==False and NIH[i,j]<=MID_E[i,j]: 
                    NIH[i,j]=IH[i,j]
        c=c+1
    for i in range(col):
        for j in range(row):
            if  np.isnan(GWHF[i,j])==True:
                NIH[i,j]=0

    ###Writing new initial head
    with open(DP+f'/{MNAME}.bas','r') as file:
        lines=file.readlines()
        NAMEOFAQUIFER=[]
        for i in range(len(lines)): 
             if 'IBOUND' in lines[i]:
                 NAMEOFAQUIFER.append(lines[i].split()[-2])
        print(NAMEOFAQUIFER)
        for i in range(len(lines)):
            if NAMEOFAQUIFER[0] in lines[i] and "HNOFLO" in lines[i-1]:
                d=i
            if NAMEOFAQUIFER[1] in lines[i]:
                m=i
    c=0
    with open(DP+f'/{MNAME}.bas','w') as file:
        for i in range(len(lines)):
            if i>d and i<m:
                for k in range(len(lines[i].split())):
                    file.write(txt.format(NIH.flatten()[c])+'\t')
                    c=c+1
                file.write('\n')       
            else:        
                file.write(lines[i])
    ##copy to other particles
    print(f'new initial head distribution is written in *.bas file in {DP}')
    import shutil
    for i in range(NOP):
        try:
            shutil.copyfile(DP+f'/{MNAME}.bas',DP_P+f'/particle{i}/{MNAME}.bas')
            print(f'initial {MNAME}.bas copied to {i}th particle')
            
        except:
            print(f'error in copying {MNAME}.bas to {i}th particle')
            print(DP+f'/{MNAME}.bas')
            print(DP_P+f'/particle{i}/{MNAME}.bas')
            