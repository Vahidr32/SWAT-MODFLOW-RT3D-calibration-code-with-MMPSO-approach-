def SpatialDistribution(DP, It):
    from DirSM import DirSM
    import matplotlib.pyplot as plt
    import numpy as np
    from Initialization import Initialization
    DM, DBM, DP_P, DRR=DirSM()
    import os
    [NSB,NOP,MNIt,NSY,BYS,BJDS,EJDS,NYSKIP,C1I,C1F,C2I,C2F,RC,NG, NOW, NSD, SDate, FDate,NCores,MMPSO, TCir1, TCir2,DPI]=Initialization(DM=DM)
    year=BYS+NSY-NYSKIP
    with open(DM+'/SWAT-MODFLOW-PSO/Initialization.txt') as file:
        lines=file.readlines()
        for i in range(len(lines)):
            if 'GW_Col' in lines[i]:
                column=int(lines[i].split()[0])
            if 'GW_rows' in lines[i]:
                row=int(lines[i].split()[0])
    with open(DM+'/SWAT-MODFLOW-PSO/Printing.txt') as file:
        lines=file.readlines()
        for i in range(len(lines)):
            if 'WS_Fig' in lines[i]:
                WS_Fig=float(lines[i].split()[0])
            if 'HS_Fig' in lines[i]:
                HS_Fig=float(lines[i].split()[0])
            if 'HS_Fig' in lines[i]:
                HS_Fig=float(lines[i].split()[0])
            if 'TitleS_Font' in lines[i]:
                TitleS_Font=float(lines[i].split()[0])

    Layer=1
    GWH=np.nan*np.ones([row,column])
    with open(DP+f'/swatmf_out_MF_head_yearly{It}.txt') as file:
        lines=file.readlines()
        for i in range(len(lines)):
            if "year" in lines[i] and float(lines[i].split()[1])==year:
                for m in range(column*Layer):
                    if "layer" in lines[i+m+1] and float(lines[i+m+1].split()[1])==Layer:
                        for j in range(row):
                            for k in range(column):
                                if float(lines[i+j+2+m].split()[k])>-100:
                                    GWH[j,k]=lines[i+j+2+m].split()[k]
                                else:
                                    GWH[j,k]=np.nan
    fig, ax = plt.subplots(figsize = (WS_Fig,HS_Fig))
    img = ax.contourf(GWH, cmap="nipy_spectral",levels=200 ,origin="upper", extent=[1,column,1,row],vmin=0)
    ax.axis('off')
    plt.title('a) Annual GW head',fontsize=TitleS_Font,loc='left',fontname='Times New Roman')
    cb=plt.colorbar(img, ax=ax)
    cb.ax.tick_params(labelsize=0.75*TitleS_Font) #Set the font size of the color scale scale.
    cb.set_label('Elevation (m)',fontsize=int(TitleS_Font),fontname='Times New Roman') #Set the label font and size of the colorbar
    fig.savefig(DRR+'/GWHE.jpeg', dpi=DPI)
    cb=[]
    GWNC=np.nan*np.ones([row,column])
    
    if os.path.isfile(DP+f'/swatmf_out_RT_cno3_yearly{It}.txt') is True: 
        with open(DP+f'/swatmf_out_RT_cno3_yearly{It}.txt') as file:
            lines=file.readlines()
            for i in range(len(lines)):
                if "year" in lines[i] and float(lines[i].split()[1])==year:
                    print('yes')
                    for m in range(column*Layer):
                        if "layer" in lines[i+m+1] and float(lines[i+m+1].split()[1])==Layer:
                            print('yes')
                            for j in range(row):
                                for k in range(column):
                                    if np.isnan(GWH[j,k])==False:
                                        GWNC[j,k]=lines[i+j+2+m].split()[k]
                                    else:
                                        GWNC[j,k]=np.nan                
    ##### Figure                                
    fig, ax = plt.subplots(figsize = (WS_Fig,HS_Fig))
    img = ax.contourf(GWNC, cmap="nipy_spectral",levels=200 ,origin="upper", extent=[1,column,1,row], vmin=0)
    ax.axis('off')
    plt.title('Annual GW nitrate concentration',fontsize=TitleS_Font,loc='left',fontname='Times New Roman')
    cb=plt.colorbar(img, ax=ax)
    cb.ax.tick_params(labelsize=int(TitleS_Font)) #Set the font size of the color scale scale.
    cb.set_label('NO3 (mg/l)',fontsize=int(TitleS_Font),fontname='Times New Roman') #Set the label font and size of the colorbar
    fig.savefig(DRR+'/GWNC.jpeg', dpi=DPI)
    cb=[]
    import numpy as np
    GWR=np.nan*np.ones([row,column])
    with open(DP+f'/swatmf_out_MF_recharge_yearly{It}.txt') as file:
        lines=file.readlines()
        for i in range(len(lines)):
            if "year" in lines[i] and float(lines[i].split()[1])==year:
                print('yes')
                for j in range(row):
                    for k in range(column):
                        if np.isnan(GWH[j,k])==False:
                            GWR[j,k]=lines[i+j+1].split()[k]
                        else:
                            GWR[j,k]=np.nan
##### Recharge Figure
    fig, ax = plt.subplots(figsize = (WS_Fig,HS_Fig))
    img = ax.contourf(GWR, cmap="nipy_spectral",origin="upper",levels=200, extent=[1,column,1,row])
    ax.axis('off')
    plt.title('b) Annual GW recharge',fontsize=TitleS_Font,loc='left',fontname='Times New Roman')
    cb=plt.colorbar(img, ax=ax)
    cb.ax.tick_params(labelsize=int(TitleS_Font)) #Set the font size of the color scale scale.
    cb.set_label('GW recharge (m\u00b3/year)',fontsize=int(TitleS_Font),fontname='Times New Roman') #Set the label font and size of the colorbar
    fig.savefig(DRR+'/Recharge.jpeg', dpi=DPI)
#### Water table Figure
    from MNAME import MNAME
    MNAME=MNAME()
    with open (DM+f'/SWAT-MODFLOW-PSO/Particles/MODFLOW/{MNAME}.dis','r') as file:
        lines=file.readlines()
        TE=np.zeros([row,column])
        for i in range(len(lines)):
            if 'TOP' in lines[i]:
                start=int(i)
        d=1
        for i in range(row):
            c=0
            f=0
            while c<column:
                try:
                    TE[i,c]=lines[start+d].split()[f]
                    f=f+1
                    c=c+1
                except:
                       d=d+1
                       f=0
            d=d+1
    WT=np.zeros([row,column])
    a=[]
    for y in range(NSY-NYSKIP):
        for i in range(row):
            for j in range(column):
                WT[i,j]=GWH[i,j]-TE[i,j]
    fig, ax = plt.subplots(figsize = (WS_Fig,HS_Fig))
    img = ax.contourf(GWH-TE, cmap="nipy_spectral",levels=200 ,origin="upper", extent=[1,column,1,row])
    ax.axis('off')
    plt.title('a) Annual GW table',fontsize=TitleS_Font,loc='left',fontname='Times New Roman')
    cb=plt.colorbar(img, ax=ax)
    cb.ax.tick_params(labelsize=int(TitleS_Font)) #Set the font size of the color scale scale.
    cb.set_label('GW table (m)',fontsize=TitleS_Font,fontname='Times New Roman') #Set the label font and size of the colorbar
    plt.savefig(DRR+'/WT.jpeg', dpi=DPI)