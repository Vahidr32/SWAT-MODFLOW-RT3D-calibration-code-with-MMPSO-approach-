def Nloads(It):
    import numpy as np
    from Initialization import Initialization
    from Get_Directory import Get_Directory
    from DirSM import DirSM
    import datetime
    from Initialization import Initialization
    import numpy as np
    from Get_Directory import Get_Directory
    from DirSM import DirSM



    DBM,DP,DRR,DM=Get_Directory()
    DM, DBM, DP, DRR=DirSM()
    [NSB,NOP,MNIt,NSY,BYS,BJDS,EJDS,NYSKIP,C1I,C1F,C2I,C2F,RC,NG, NOW, NSD, SDate, FDate,NCores,MMPSO, TCir1,TCir2,DPI]=Initialization(DM=DM)

    SN=np.nan*np.ones([NOP,It,NSD])
    for i in range(NOP):
        for j in range(It): 
            DR=DP+f'/particle{i}/output.rch{j}.txt'
            with open(DR, 'r') as datafile:
                a=(datafile.read().split()[29::11])
            CCC=0
            SNR=49
            for k in range(len(a)):
                if k==SNR:
                    SN[i,j,CCC]=float(a[k])
                    CCC+=1
                    SNR+=NSB
                else:
                    a[k]=[]
    txt = "{:3.3E}"
    SNR=49
    b=[]
    with open(DRR+'/TotalLoads.txt','w') as file:
        file.write(f'The average annual year of Nitrate loads for subbasin{SNR} (tonnes/year)\n')
        for i in range(NOP):
            file.write(f'Particle{i}:\t')
            for j in range(It):
                file.write(f'Iter{j}: ')
                if sum(SN[i,j,0:NSD])/((NSY-NYSKIP)*1000)<10**5 and np.isnan(sum(SN[i,j,0:NSD]))==False:
                     b.append(sum(SN[i,j,0:NSD])/((NSY-NYSKIP)*1000))
                file.write(txt.format(sum(SN[i,j,0:NSD])/((NSY-NYSKIP)*1000))+'\t')
            file.write('\n')
    
        file.write('final conclusion on total loads\n')
        file.write('95 percentile of the average annual total loads:\t')
        file.write(txt.format(np.nanpercentile(b,2.5))+'\t')
        file.write(txt.format(np.nanpercentile(b,97.5))+'\n')
        file.write('The average annual total loads:\t')
        file.write(txt.format(np.nanmean(b))+'\n')



    DBM,DP,DRR,DM=Get_Directory()
    DM, DBM, DP, DRR=DirSM()
    [NSB,NOP,MNIt,NSY,BYS,BJDS,EJDS,NYSKIP,C1I,C1F,C2I,C2F,RC,NG, NOW, NSD, SDate, FDate,NCores,MMPSO, TCir1,TCir2,DPI]=Initialization(DM=DM)
    date = datetime.date(SDate.year,SDate.month,SDate.day)
    GWNL=np.zeros([NOP,It])
    NLeach=np.zeros([NOP,It])
    NSWGW=np.zeros([NOP,It])
    NO3SY=np.zeros([NOP,It])
    NO3LATY=np.zeros([NOP,It])
    ANO3L=np.zeros([NOP,It,NSY-NYSKIP])

    for k in range(NOP):
        for l in range(It):
            DR=DP+f'/particle{k}/output.std{j}.txt'
            print(DR)
            with open(DR,'r') as file:
                
                lines=file.readlines()
                print(lines)
                c=0
                for i in range(len(lines)):
                    if 'NO3 LOAD GW (RT3D)' in lines[i]:
                        if '********' in lines[i].split('=')[1].split()[0]:
                            GWNL[k,l]=np.nan
                        else:
                            GWNL[k,l]=(float(lines[i].split('=')[1].split()[0]))
                 
                    if 'NO3 SW-GW (RT3D)' in lines[i]:
                        if '********' in (lines[i].split('=')[1].split()[0]):
                            NSWGW[k,l]=np.nan
                        else:
                            NSWGW[k,l]=(float(lines[i].split('=')[1].split()[0]))
                    if 'NO3 YIELD (SQ)' in lines[i]:
                        if '********' in (lines[i].split('=')[1].split()[0]):
                            NO3SY[k,l]=np.nan
                        else:
                            NO3SY[k,l]=(float(lines[i].split('=')[1].split()[0]))
                    if 'NO3 YIELD (LAT)' in lines[i]:
                        if '********' in (lines[i].split('=')[1].split()[0]):
                            NO3LATY[k,l]=np.nan
                    else:
                            NO3LATY[k,l]=(float(lines[i].split('=')[1].split()[0]))
                    if 'NO3 LEACHED' in lines[i]:
                        if '********' in (lines[i].split('=')[1].split()[0]):
                            NLeach[k,l]=np.nan
                        else:
                            NLeach[k,l]=(float(lines[i].split('=')[1].split()[0]))
                    try:
                        if lines[i].split()[0]==str(date.year+c):
                            ANO3L[k,l,c]=float(lines[i].split()[21])
                            c=c+1
                    except:
                          'nothing'

    with  open(DRR+'/TotalLoads.txt','a') as file:
        file.write('Nitrate loads reports\n')
        file.write('NO3 loads from GW aquifers(kg/ha) 2.5P  mean 97.5P:\t')
        file.write(txt.format(np.nanpercentile(GWNL.flatten(),2.5))+'\t')
        file.write(txt.format(np.nanmean(GWNL.flatten()))+'\t')
        file.write(txt.format(np.nanpercentile(GWNL.flatten(),97.5))+'\n')
        file.write('NO3 loads from surface water to GW(kg/ha) 2.5P  mean 97.5P:\t')
        file.write(txt.format(np.nanpercentile(NSWGW.flatten(),2.5))+'\t')
        file.write(txt.format(np.nanmean(NSWGW.flatten()))+'\t')
        file.write(txt.format(np.nanpercentile(NSWGW.flatten(),97.5))+'\n')
        file.write('NO3 loads from surface runoff (kg/ha) 2.5P  mean 97.5P:\t')
        file.write(txt.format(np.nanpercentile(NO3SY.flatten(),2.5))+'\t')
        file.write(txt.format(np.nanmean(NO3SY.flatten()))+'\t')
        file.write(txt.format(np.nanpercentile(NO3SY.flatten(),97.5))+'\n')
        file.write('NO3 loads from lateral flow (kg/ha) 2.5P  mean 97.5P:\t')
        file.write(txt.format(np.nanpercentile(NO3LATY.flatten(),2.5))+'\t')
        file.write(txt.format(np.nanmean(NO3LATY.flatten()))+'\t')
        file.write(txt.format(np.nanpercentile(NO3LATY.flatten(),97.5))+'\n')
        file.write('NO3 leached (kg/ha) 2.5P  mean 97.5P:\t')
        file.write(txt.format(np.nanpercentile(NLeach.flatten(),2.5))+'\t')
        file.write(txt.format(np.nanmean(NLeach.flatten()))+'\t')
        file.write(txt.format(np.nanpercentile(NLeach.flatten(),97.5))+'\n')
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(True)
    ax.yaxis.set_ticks_position('none')
    labels = ['GW NO3 Loads', 'SW-GW NO3 Loads', 'SurfaceRunoff NO3 Loads', 'LateralFlow NO3 Loads']

    bplot=ax.boxplot(GWNL.flatten(), widths=0.6,patch_artist=True, positions=[0],labels=[labels[0]],showfliers=False, vert=False)

    bplot=ax.boxplot(NSWGW.flatten(), widths=0.6, patch_artist=True, positions=[1],labels=[labels[1]],showfliers=False, vert=False) 

    bplot=ax.boxplot(NO3SY.flatten(), widths=0.6, patch_artist=True, positions=[2],labels=[labels[2]],showfliers=False, vert=False)

    bplot=ax.boxplot(NO3LATY.flatten(), widths=0.6, patch_artist=True, positions=[3],labels=[labels[3]],showfliers=False, vert=False) 



    fig.savefig(DRR+'/Nutrient.png', dpi=150, bbox_inches='tight')

