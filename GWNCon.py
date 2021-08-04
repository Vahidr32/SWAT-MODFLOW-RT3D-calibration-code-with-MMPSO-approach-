import numpy as np
import matplotlib.pyplot as plt
import datetime
from Initialization import Initialization
from Get_Directory import Get_Directory
from DirSM import DirSM
DBM,DP,DRR,DM=Get_Directory()
DM, DBM, DP, DRR=DirSM()
[NSB,NOP,MNIt,NSY,BYS,BJDS,EJDS,NYSKIP,C1I,C1F,C2I,C2F,RC,NG, NOW, NSD, SDate, FDate,NCores,MMPSO, TCir1, TCir2,DPI]=Initialization(DM=DM)


NO3=np.nan*np.zeros([1464, NOP*MNIt])
c=0
NSD=1464
for i in range(NOP):
    for j in range(MNIt):
        DR=DP+f'/particle{i}/swatmf_out_RT_OBSNO3{j}.txt'
        print(DR)
        with open(DR,'r') as file:
            lines=file.readlines()
            try:
                NO3[0:NSD, c]=[float(x.split()[33]) for x in lines[2+14*365:-365]]
                c=c+1
            except:
                'nothing'
Minn=[]
Maxx=[]
for k in range(NSD):
    PPU=[]
    DDD=[] 
    for i in range(NOP*MNIt):
        PPU.append(NO3[k][i])
    NFP=np.nanpercentile((PPU[0:NSD]),[2.5,97.5])
    Minn.append(NFP[0])
    Maxx.append(NFP[1])


date = datetime.date(1998+14,1,1)
dateplot=[]
for j in range((len(NO3))):
    date += datetime.timedelta(days=1)
    dateplot.append(date)

fig=plt.figure(figsize=[10,5])
ax = fig.gca()
ax.plot()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
#plt.fill_between(dateplot[0:NSD], Minn[0:NSD],Maxx[0:NSD],color='green',alpha=.25)
plt.plot(dateplot,NO3[0:NSD,10],'blue',linewidth=1)
plt.title("d) Monthly simulated GW concentration")
plt.ylabel('mg/l',fontsize=12)
fig.savefig(DRR+'/NC.jpeg', dpi=300)