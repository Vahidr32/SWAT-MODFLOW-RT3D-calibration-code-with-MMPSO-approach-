import numpy as np
import os
from distutils.dir_util import copy_tree
import matplotlib.pyplot as plt
from multiprocessing import Pool, Process
import time
import datetime
import statistics
import gc
from collections import Counter
from scipy.stats.distributions import norm
from pyDOE import lhs
import shutil
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import StrMethodFormatter
from matplotlib.ticker import MaxNLocator
from FigureM import FigureM
from CheckPoint import CheckPoint
from SpatialDistribution import SpatialDistribution
# importing functions
from Get_Directory import Get_Directory
from RHO import RHO
from copyPSO import copyPSO
from VLHS import VLHS
from SWAT_edit import SWAT_edit
from CPVALPSO import CPVALPSO
from SRF import SRF
from SNF import SNF
from Figure import Figure
from Baseflow import Baseflow
from Figure95PPU import Figure95PPU
from OBJNO3 import OBJNO3 
from FigureScatter import FigureScatter
from RNO import RNO
from Par_input import Par_input
from RiverCon import RiverCon
from btn import btn
from dsp import dsp
from Pval import Pval
from rct import rct
from RHS import RHS
from datetime import datetime
from Initialization import Initialization
from filecio import filecio
from ObservationName import ObservationName
from OBJNO3Flux import OBJNO3Flux
from FigureScatter2 import FigureScatter2
from Figure95PPUNO3 import Figure95PPUNO3
from OFSM import OFSM
from DirSM import DirSM
from RPResults import RPResults
from Defination import Defination
from GWD import GWD
from hfunction import *
from POption import POption
import multiprocessing
from PVG import PVG
from InitialHead import InitialHead
from FontPSO import FontPSO
from DelParticles import DelParticles
from copyPSO import copyPSO
#############################################
# the defination of each variable in the code can be called by the following example: 
# Defination(i="RC")
# return: Chance of random selection
DBM,DP,DRR,DM=Get_Directory()
DM, DBM, DP, DRR=DirSM()
if os.path.exists(DRR) is False:
    os.mkdir(DRR)
INF='Parameter_input.txt'
[NSB,NOP,MNIt,NSY,BYS,BJDS,EJDS,NYSKIP,C1I,C1F,C2I,C2F,RC,NG, NOW, NSD, SDate, FDate,NCores,MMPSO, TCir1, TCir2,DPI]=Initialization(DM=DM)
[NV,VN, MaxB, Parameter, MinB, FileName, Grouping, VNum]=Par_input(DM+"/SWAT-MODFLOW-PSO/", INF)
pm=POption()
[SG, SON,SOB,SW, SMO,S_KGEW1,S_KGEW2,S_KGEW3,BG, BON,BOB,BW, BMO,B_KGEW1,B_KGEW2,B_KGEW3, HG, HON,HOC,HW,HMO, H_KGEW1, H_KGEW2,H_KGEW3, NO3G, NON,NOB, NW, NMO,N_KGEW1,N_KGEW2,N_KGEW3]=ObservationName(DM=DM)
NG=int(max(SG+BG+HG+NO3G))
Group_dict = {i:Grouping.count(i) for i in Grouping}
P_Group=-1*np.ones([NG,NV])
GG=[]
with open (DM+"/SWAT-MODFLOW-PSO/Initialization.txt",'r') as file:
    lines=file.readlines()
    for i in range(len(lines)):
        if "NIS" in lines[i]:
            NIS=int(lines[i].split()[0])
for i in range(NG):
    GG.append(str(i+1))
for j in range(len(GG)):
    C=0
    for i in range(len(Grouping[:NV])):
        if Grouping[i]==GG[j]:
            P_Group[j,C]=VNum[i]
            C=C+1
with open(DM+'/SWAT-MODFLOW-PSO/Initialization.txt', 'r') as file:
    lines=file.readlines()
    for i in range(len(lines)):
        if "InertiaMin" in lines[i]:
            InertiaMin=float(lines[i].split()[0])
        if "InertiaMax" in lines[i]:
            InertiaMax=float(lines[i].split()[0])

with open(DM+'/SWAT-MODFLOW-PSO/Initialization.txt') as file:
    lines=file.readlines()
    for i in range(len(lines)):
        if 'Delete_Particles' in lines[i]:
            if float(lines[i].split()[0])==1:
                if __name__ ==  '__main__': 
                    if __name__ ==  '__main__': 
                        multiprocessing.freeze_support()
                        num_processors = NOP
                        p=Pool(processes = num_processors)
                        ParticleDirectory =p.map(DelParticles,[i for i in range(NOP)])

if __name__ ==  '__main__': 
    multiprocessing.freeze_support()
    num_processors = NOP
    p=Pool(processes = num_processors)
    ParticleDirectory =p.map(copyPSO,[i for i in range(NOP)])
filecio(DM=ParticleDirectory,NSY=NSY,BYS=BYS,BJDS=BJDS,EJDS=EJDS,NYSKIP=NYSKIP)
Inertia=np.zeros([NOP])
class Particle:
    X,V=np.zeros([NOP, NV, MNIt+1]),np.zeros([NOP, NV, MNIt+1])
    LocalGoal=np.zeros([NOP, MNIt])
    LocalBest=np.nan*np.zeros([NOP, MNIt])
    LocalBestIndex=np.nan*np.zeros([NOP])
    GlobalBest=np.nan*np.zeros([MNIt])
    GlobalBestIndex=np.nan*np.zeros([2])
    class Group:
        Goal=np.zeros([NG,NOP,MNIt])
        LocalBest=np.nan*np.zeros([NG,NOP,MNIt])
        GlobalBest=np.nan*np.zeros([NG,MNIt])
        LocalBestIndex=np.nan*np.zeros([NG, NOP,1])
        GlobalBestIndex=np.nan*np.zeros([NG,2])
class Sim:
    Stream=np.NaN*np.empty([len(SON),NOP,MNIt, NSD])
    Baseflow=np.NaN*np.empty([len(SON),NOP,MNIt, NSD])
    Head=np.NaN*np.empty([len(HON), NOP,MNIt, NSD])
    NO3Con=np.NaN*np.empty([len(NON), NOP,MNIt, NSD])
    NO3Flux=np.NaN*np.empty([len(NON), NOP,MNIt, NSD])
    NO3Stream=np.NaN*np.empty([len(NON), NOP,MNIt, NSD])
class Obs:
    Stream=np.zeros([len(SON), NSD])
    Baseflow=np.zeros([len(SON), NSD])
    Head=np.zeros([len(HON),NSD])
    NO3ConV=-1*np.ones([len(NON),NSD])
    NO3ConD=-1*np.ones([len(NON),NSD])
    NO3Flux=np.zeros([len(NON), NSD])
class Obj:
    Stream=np.zeros([len(SON),NOP,MNIt])
    Baseflow=np.zeros([len(SON),NOP,MNIt])
    Head=np.zeros([len(HON), NOP,MNIt])
    NO3Con=np.zeros([len(NON), NOP,MNIt])
    NO3Flux=np.zeros([len(NON), NOP,MNIt])
Inertia=np.zeros([NOP])
lhd=VLHS(NV=NV, NS=NOP*NIS, MaxB=MaxB, MinB=MinB)
c=0
for k in range(NIS):
    for i in range(NOP):
        for j in range(NV):
            Particle.X[i][j][k]=lhd[c][j]
        c=c+1
#for i in range(NV):
  #  Particle.X[0][i][0]=Parameter[i]
with open(DM+'/SWAT-MODFLOW-PSO/Initialization.txt') as file:
    lines=file.readlines()
    for i in range(len(lines)):
        if "RFIP" in lines[i]: 
            RFIP=int(lines[i].split()[0])
if RFIP==1 and os.path.isfile(DM+'/SWAT-MODFLOW-PSO/InitialParameters.txt')==True:
    print('reading from initial parameters')
    with open(DM+'/SWAT-MODFLOW-PSO/InitialParameters.txt','r') as file:
        lines=file.readlines()
        NIS=int(np.round(len(lines[0].split())/NOP))
        c=0
        lhd=VLHS(NV=NV, NS=NIS*NOP, MaxB=MaxB, MinB=MinB)
        for It in range(NIS):
            for i in range(NOP):
                for j in range(NV):
                    Particle.X[i][j][It]=lhd[c][j]
                c=c+1
        c=0
        for It in range(NIS):
            for i in range(NOP):
                for j in range(len(lines)):
                    if c<len(lines[0].split()):
                        Particle.X[i][j][It]=float(lines[j].split()[c])
                        if Particle.X[i][j][It]>MaxB[j]:
                            print(f'parameter{VN[j]} in iteration {It} exceeded max')
                            Particle.X[i][j][It]=np.random.uniform(MinB[j],MaxB[j])
                        if Particle.X[i][j][It]<MinB[j]:
                            print(f'parameter{VN[j]} in iteration {It} exceeded min')
                            Particle.X[i][j][It]=np.random.uniform(MinB[j],MaxB[j])
                c=c+1
from SRF import SRF
for i in range(len(SON)):
    Obs.Stream[i,0:NSD]=RHO(D=DM, OSNF= "/SWAT-MODFLOW-PSO/Observation/"+SON[i]+".txt", SDate=SDate, NSD=NSD)
    Obs.Baseflow[i,0:NSD]=Baseflow(Sim=Obs.Stream[i,0:NSD],SDate=SDate, NSD=NSD)
for i in range(len(HON)):
    Obs.Head[i,0:NSD]=RHO(D=DM, OSNF= "/SWAT-MODFLOW-PSO/Observation/"+HON[i]+".txt", SDate=SDate, NSD=NSD)

for i in range(len(NON)):
    NCDate,NCvalue=RNO(D=DM, OSNF= "/SWAT-MODFLOW-PSO/Observation/"+NON[i]+".txt", SDate=SDate, NSD=NSD)
    for j in range(len(NCvalue)):
        Obs.NO3ConV[i,j]=NCvalue[j]
        Obs.NO3ConD[i,j]=NCDate[j] 
import stat
for i in range(NOP):
    
    shutil.copy2(DM+'/swat-modflow3',ParticleDirectory[i])
    os.chmod(ParticleDirectory[i]+'/swat-modflow3', stat.S_IRWXU+ stat.S_IRWXO+stat.S_IRWXG)
    #shutil.copy2(DM+'/swat670_static',ParticleDirectory[i])
    #os.chmod(ParticleDirectory[i]+'/swat670_static', stat.S_IRWXU+ stat.S_IRWXO+stat.S_IRWXG)
for i in range(NOP):
    #print(i)
    copy_tree(DM+'/SWAT-MODFLOW-PSO/Particles/MODFLOW', DP+"/particle"+str(i),preserve_mode=0)
with open(DM+'/SWAT-MODFLOW-PSO/Dic_Variable.txt','r') as file:
    lines=file.readlines()
    Convert=[]
    for i in range(len(lines)):
        Convert.append(lines[i].split()[2])
        VN2=[]
    for i in range(NV):
        for j in range(len(lines)):
            if VN[i]==lines[j].split()[0]:
                VN2.append(lines[j].split()[1])
MaxBB=np.zeros([NV])
MinBB=np.zeros([NV])
for j in range(NV):
    if Convert[j]=='E':
        MaxBB[j]=10**MaxB[j]
        MinBB[j]=10**MinB[j]
    else:
        MaxBB[j]=MaxB[j]
        MinBB[j]=MinB[j]
It=0
RPResults(ParticleDirectory, MNIt)
while It <MNIt:
    print(f'this is iteration{It}')
    if __name__ ==  '__main__': 
        multiprocessing.freeze_support()
        multiprocessing.freeze_support()
        processes = []
        for i in range(NOP):
            Iteration=It
            Core=0
            for Omega in range(NV):
                Parameter[Omega]=Particle.X[i][Omega][It]
            process=Process(target=CPVALPSO,args=(ParticleDirectory[i],Iteration,Parameter,VN,FileName,MaxB,MinB))                              
            processes.append(process)
            process.start()

    for i in range(NOP):
        while os.path.isfile(ParticleDirectory[i]+"/output.rch"+str(It)+".txt") is False:time.sleep(0.01)
        else:
            print(f"Starting the evaliation of solution found by Particle {i}")        
            DR=ParticleDirectory[i]+"/swatmf_out_MF_obs"+str(It)+".txt" 
            for O in range(len(HOC)):
                Sim.Head[O][i][It][0:NSD]=RHS(DR=DR, NSD=NSD+NOW, NOW=NOW, Col=HOC[O]) 
                Obj.Head[O][i][It]=OFSM(s=Sim.Head[O][i][It][0:NSD], o=Obs.Head[O][0:NSD],Wieght= HW[O], Method= HMO[O], KGEw1=H_KGEW1[O], KGEw2=H_KGEW2[O], KGEw3=H_KGEW3[O],ty='GW')
            DR=ParticleDirectory[i]+"/output.rch"+str(It)+'.txt'
            for O in range(len(SOB)):
                Sim.Stream[O][i][It][0:NSD]=SRF(DR=DR,SNR=SOB[O], NSB=NSB, NSD=NSD)
                Sim.Baseflow[O][i][It][0:NSD]=Baseflow(Sim=Sim.Stream[O][i][It][0:NSD],SDate=SDate, NSD=NSD)
                Obj.Stream[O][i][It]=OFSM(Sim.Stream[O][i][It][0:NSD], Obs.Stream[O][0:NSD],Wieght= SW[O], Method= SMO[O], KGEw1=S_KGEW1[O], KGEw2=S_KGEW2[O],KGEw3=S_KGEW3[O],ty='SF')
                Obj.Baseflow[O][i][It]=OFSM(s=Sim.Baseflow[O][i][It][0:NSD], o=Obs.Baseflow[O][0:NSD],Wieght= BW[O], Method= BMO[O], KGEw1=B_KGEW1[O], KGEw2=B_KGEW2[O],KGEw3=B_KGEW3[O],ty='BF')
            for O in range(len(NOB)):
                Sim.NO3Flux[O][i][It][:NSD]=SNF(DR=DR,SNR=NOB[O], NSB=NSB, NSD=NSD)
                Sim.NO3Stream[O][i][It][:NSD]=SRF(DR=DR,SNR=NOB[O], NSB=NSB, NSD=NSD)
                Sim.NO3Con[O][i][It][0:NSD]=(1000/86400)*np.divide(Sim.NO3Flux[O][i][It][0:NSD],Sim.NO3Stream[O][i][It][0:NSD])
                Obj.NO3Con[O][i][It]=NW[O]*OBJNO3(OBS=[Obs.NO3ConD[O],Obs.NO3ConV[O]], SIMCON=Sim.NO3Con[O][i][It][0:NSD], NSD=NSD,KGEw1=N_KGEW1[O], KGEw2=N_KGEW2[O],KGEw3=N_KGEW3[O])
                Obj.NO3Flux[O][i][It]=NW[O]*OBJNO3Flux(ObsStream=Obs.Stream[O][0:NSD], ObsCon=[Obs.NO3ConD[O],Obs.NO3ConV[O]], SimFlux=Sim.NO3Flux[O][i][It][0:NSD],NSD=NSD, KGEw1=N_KGEW1[O], KGEw2=N_KGEW2[O],KGEw3=N_KGEW3[O])
            for k in range(NG):
                for O in range(len(SON)):
                    if SG[O]-1==k:
                        Particle.Group.Goal[k,i,It]=Particle.Group.Goal[k,i,It]+Obj.Stream[O][i][It]
                for O in range(len(SON)):
                    if BG[O]-1==k:
                        Particle.Group.Goal[k,i,It]=Particle.Group.Goal[k,i,It]+Obj.Baseflow[O][i][It]
                for O in range(len(HON)):
                    if HG[O]-1==k:
                        Particle.Group.Goal[k,i,It]=Particle.Group.Goal[k,i,It]+Obj.Head[O][i][It]
                for O in range(len(NON)):
                    if NO3G[O]-1==k:
                        Particle.Group.Goal[k,i,It]=Particle.Group.Goal[k,i,It]+Obj.NO3Flux[O][i][It]+Obj.NO3Con[O][i][It]
            # This line should be deleted if we wanted to publish the code (Costumized)
            #if Particle.Group.Goal[0,i,It]!=-np.inf and np.isnan(Particle.Group.Goal[0,i,It])==False:
               # check=CheckPoint(P=i,It=It)
                #if check>0.6:
                    #Particle.Group.Goal[1,i,It]=Particle.Group.Goal[1,i,It]-25*check
                 #   Particle.Group.Goal[0,i,It]=Particle.Group.Goal[0,i,It]-25*check
            for k in range(NG):
                    Particle.LocalGoal[i,It]=(Particle.Group.Goal[k,i,It])+Particle.LocalGoal[i,It]
            if It==0 and i==0:
                for k in range(NG):
                    Particle.Group.GlobalBest[k,It]=-np.inf
                    Particle.Group.GlobalBestIndex[k,0]=i
                    Particle.Group.GlobalBestIndex[k,1]=It
                Particle.GlobalBest[It]=-np.inf
                Particle.GlobalBestIndex=[i,It]  
            if It==0:
                for k in range(NG):
                    Particle.Group.LocalBest[k,i,It]=-np.inf
                    Particle.Group.LocalBestIndex[k,i,0]=It
                Particle.LocalBest[i,It]=-np.inf
                Particle.LocalBestIndex[i]=It
            if It>0 and i==0:
                for k in range(NG):
                    Particle.Group.GlobalBest[k,It]=Particle.Group.GlobalBest[k,It-1]
                Particle.GlobalBest[It]=Particle.GlobalBest[It-1]   
            if It>0:
                for k in range(NG):
                    Particle.Group.LocalBest[k,i,It]=Particle.Group.LocalBest[k,i,It-1]
                    Particle.Group.LocalBestIndex[k,i,0]=It-1
                Particle.LocalBest[i,It]=Particle.LocalBest[i,It-1]
                Particle.LocalBestIndex[i]=Particle.LocalBestIndex[i-1]
            if Particle.LocalGoal[i,It]>(Particle.GlobalBest[It]):
                print(f'Global best updated by {i}')
                Particle.GlobalBest[It]=Particle.LocalGoal[i,It]
                Particle.GlobalBestIndex=[i,It]    
            for k in range(NG):
                if Particle.Group.Goal[k,i,It]>(Particle.Group.GlobalBest[k,It]):
                    Particle.Group.GlobalBest[k,It]=Particle.Group.Goal[k,i,It]
                    Particle.Group.GlobalBestIndex[k,0]=i
                    Particle.Group.GlobalBestIndex[k,1]=It
                if Particle.Group.Goal[k,i,It]>(Particle.Group.LocalBest[k,i,It]):
                    Particle.Group.LocalBest[k,i,It]=Particle.Group.Goal[k,i,It]
                    Particle.Group.LocalBestIndex[k,i,0]=It
            if Particle.LocalGoal[i,It]>(Particle.LocalBest[i,It]):
                Particle.LocalBest[i,It]=Particle.LocalGoal[i,It]
                Particle.LocalBestIndex[i]=It
            with open  (DRR+"/GoalOutput.txt", 'a') as file:
                file.write(f'particle-{i} local goal for this iteration is {Particle.LocalGoal[i,It]}\n')
                for k in range(NG):
                    file.write(f'particle-{i} local Goal group{k} for this iteration is {Particle.Group.Goal[k,i,It]}\n')
                file.write(f"particle-{i} local Best is {Particle.LocalBest[i,It]}\n")
                for k in range(NG):
                    file.write(f'particle-{i} local Best group{k} for this iteration is {Particle.Group.LocalBest[k,i,It]}\n')
                file.write("\n")
    if It>(NIS-2):
        with open(DM+"/SWAT-MODFLOW-PSO/Parameter_input.txt",'r') as file:
            lines=file.readlines()
            for i in range(1,len(lines)):
                MaxB[i-1]=float(lines[i].split()[4])
                MinB[i-1]=float(lines[i].split()[6])
        print(f"Global best is {Particle.GlobalBest[It]}")
        for k in range(NG):
            print(f'Global Best for group{k} is {Particle.Group.GlobalBest[k,It]}')
        C1=((C1F-C1I)*(It/MNIt))+C1I
        C2=((C2F-C2I)*(It/MNIt))+C2I
        MrG=[]
        InG=[]
        MeG=[]
        
        with open(DM+'/SWAT-MODFLOW-PSO/Initialization.txt', 'r') as file:
            lines=file.readlines()
            for i in range(len(lines)):
                if "InertiaMin" in lines[i]:
                    InertiaMin=float(lines[i].split()[0])
                if "InertiaMax" in lines[i]:
                    InertiaMax=float(lines[i].split()[0])
              
        if -np.inf not in Particle.LocalBest[0:NOP,It]:
            SortedGoal=list(np.sort(Particle.LocalBest[0:NOP,It]))   
            for i in range(NOP):
                Inertia[i]=InertiaMax-(InertiaMax-InertiaMin)*(SortedGoal.index(Particle.LocalBest[i,It]))/NOP
            for i in range(NOP):
                if Particle.LocalBest[i,It]>=np.nanpercentile(Particle.LocalBest[0:NOP,It],85):
                    MrG.append(i)
                if Particle.LocalBest[i,It]>np.nanpercentile(Particle.LocalBest[0:NOP,It],15) and Particle.LocalBest[i,It]<np.nanpercentile(Particle.LocalBest[0:NOP,It],85):
                    InG.append(i)
                if Particle.LocalBest[i,It]<=np.nanpercentile(Particle.LocalBest[0:NOP,It],15):
                    MeG.append(i)
        else:
            SortedGoal=list(np.sort(Particle.LocalBest[0:NOP,It]))
            for i in range(NOP):
                InG.append(i)
                Inertia[i]=InertiaMax-(InertiaMax-InertiaMin)*(SortedGoal.index(Particle.LocalBest[i,It]))/NOP
        with open  (DRR+"/MenteeIndependentMentor.txt", 'w') as file:
            file.write(f"The threshold of Mentor group is {np.nanpercentile(Particle.LocalBest[0:NOP,It],85)}\n")
            file.write(f"The threshold of Mentee group is {np.nanpercentile(Particle.LocalBest[0:NOP,It],15)}\n")
            file.write(f'Mentee group members:{MeG}\n')
            file.write(f'Independent group members:{InG}\n')
            file.write(f'Mentor group members: {MrG}\n')  
            file.write(f'InertiaRanking: {Inertia}\n')
        InertiaS=0.4+0.5*(1-(It/MNIt))/(1+10*(It/MNIt))
        
        for i in range(NOP): 
            if i not in MeG and i not in InG and i not in MrG:
                with open  (DRR+"/MenteeIndependentMentor.txt", 'a') as file:
                    file.write(f'particle {i} reseted due to insufficient information about its objective function value\n')
                for j in range(NV):
                    Particle.X[i][j][It+1]=np.random.uniform(MinB[j], MaxB[j])
            if i in MeG:
                Mentor=[]
                Mentor=int(np.random.choice(MrG))
            for j in range(NV):
                R1=np.random.uniform(0,1)
                R2=np.random.uniform(0,1)
                if MMPSO==1:
                    for o in range(NG):
                        if j in P_Group[o,0:Group_dict[GG[o]]]:
                            if i in MeG:
                                gama=int(Particle.LocalBestIndex[i])
                                alpha=Mentor
                                beta=int(Particle.LocalBestIndex[Mentor])
                                #gama=int(Particle.Group.GlobalBestIndex[o,0])
                                #alpha=int(Particle.Group.GlobalBestIndex[o,0])
                                #beta=int(Particle.Group.GlobalBestIndex[o,1])
                                if np.random.randint(0,2)==1:
                                    Cse=1
                                    Sme=0
                                else:
                                    Cse=0
                                    Sme=1
                                Particle.V[i,j,It+1]=(Inertia[i]*Particle.V[i,j,It])+(0.5*Cse*R2*C1)*((Particle.X[i,j,gama])-(Particle.X[i,j,It]))+(Sme*R2*C2)*((Particle.X[alpha,j,beta])-(Particle.X[i,j,It]))               
                                Particle.X[i][j][It+1]=(Particle.V[i][j][It+1]+Particle.X[i][j][It])
                                while Particle.X[i][j][It+1]>MaxB[j] or Particle.X[i][j][It+1]<MinB[j]:
                                    if MinB[j]==MaxB[j]:
                                        break
                                    if Particle.X[i][j][It+1]>MaxB[j]:
                                        if np.random.uniform(0,1)>0.1:
                                            Particle.V[i,j,It+1]=-1*np.random.uniform(0,1)*Particle.V[i][j][It+1]
                                            Particle.X[i][j][It+1]=Particle.X[i][j][It+1]+Particle.V[i,j,It+1]
                                        else:
                                            Particle.X[i][j][It+1]=MaxB[j]
                                            Particle.V[i,j,It+1]=0
                                    if Particle.X[i][j][It+1]<MinB[j]:
                                        if np.random.uniform(0,1)>0.1:
                                            Particle.V[i,j,It+1]=-1*np.random.uniform(0,1)*Particle.V[i][j][It+1]
                                            Particle.X[i][j][It+1]=Particle.X[i][j][It+1]+Particle.V[i,j,It+1]
                                        else:
                                            Particle.X[i][j][It+1]=MinB[j]
                                            Particle.V[i,j,It+1]=0
                            if i in InG:
                                if np.random.uniform(0,1)>0.85:
                                    gama=int(Particle.LocalBestIndex[i])
                                else:
                                    gama=int(Particle.Group.LocalBestIndex[o,i,0])
                                if np.random.uniform(0,1)>0.85:
                                    alpha=int(Particle.Group.GlobalBestIndex[o,0])
                                    beta=int(Particle.Group.GlobalBestIndex[o,1])
                                else:
                                    alpha=int(Particle.GlobalBestIndex[0])
                                    beta=int(Particle.GlobalBestIndex[1])
                                if np.random.uniform(0,1)>0.5:
                                    Ps=1
                                else:
                                    Ps=0                          
                                Particle.V[i,j,It+1]=(Inertia[i]*Particle.V[i,j,It])+((Ps*R1*C1)*((Particle.X[alpha,j,beta])-(Particle.X[i,j,It])))+(R2*C2)*((Particle.X[i,j,gama])-(Particle.X[i,j,It]))
                                Particle.X[i][j][It+1]=(Particle.V[i][j][It+1]+Particle.X[i][j][It])
                                while Particle.X[i][j][It+1]>MaxB[j] or Particle.X[i][j][It+1]<MinB[j]:
                                    if MinB[j]==MaxB[j]:
                                        break
                                    if Particle.X[i][j][It+1]>MaxB[j]:
                                        if np.random.uniform(0,1)>0.1:
                                            Particle.V[i,j,It+1]=-1*np.random.uniform(0,1)*Particle.V[i][j][It+1]
                                            Particle.X[i][j][It+1]=Particle.X[i][j][It+1]+Particle.V[i,j,It+1]
                                        else:
                                            Particle.X[i][j][It+1]=MaxB[j]
                                            Particle.V[i,j,It+1]=0
                                    if Particle.X[i][j][It+1]<MinB[j]:
                                        if np.random.uniform(0,1)>0.1:
                                            Particle.V[i,j,It+1]=-1*np.random.uniform(0,1)*Particle.V[i][j][It+1]
                                            Particle.X[i][j][It+1]=Particle.X[i][j][It+1]+Particle.V[i,j,It+1]
                                        else:
                                            Particle.X[i][j][It+1]=MinB[j]
                                            Particle.V[i,j,It+1]=0
                            if i in MrG:
                                gama=int(Particle.LocalBestIndex[i])
                                alpha=int(Particle.GlobalBestIndex[0])
                                beta=int(Particle.GlobalBestIndex[1])         
                                Particle.V[i,j,It+1]=(InertiaS*Particle.V[i,j,It])+((0.5*R1*C1)*((Particle.X[alpha,j,beta])-(Particle.X[i,j,It])))+(R2*C2)*((Particle.X[i,j,gama])-(Particle.X[i,j,It]))
                                Particle.X[i][j][It+1]=(Particle.V[i][j][It+1]+Particle.X[i][j][It]) 
                                while Particle.X[i][j][It+1]>MaxB[j] or Particle.X[i][j][It+1]<MinB[j]:
                                    if MinB[j]==MaxB[j]:
                                        break
                                    if Particle.X[i][j][It+1]>MaxB[j]:
                                        if np.random.uniform(0,1)>0.1:
                                            Particle.V[i,j,It+1]=-1*np.random.uniform(0,1)*Particle.V[i][j][It+1]
                                            Particle.X[i][j][It+1]=Particle.X[i][j][It+1]+Particle.V[i,j,It+1]
                                        else:
                                            Particle.X[i][j][It+1]=MaxB[j]
                                            Particle.V[i,j,It+1]=0
                                    if Particle.X[i][j][It+1]<MinB[j]:
                                        if np.random.uniform(0,1)>0.1:
                                            Particle.V[i,j,It+1]=-1*np.random.uniform(0,1)*Particle.V[i][j][It+1]
                                            Particle.X[i][j][It+1]=Particle.X[i][j][It+1]+Particle.V[i,j,It+1]
                                        else:
                                            Particle.X[i][j][It+1]=MinB[j]
                                            Particle.V[i,j,It+1]=0
                else:
                    gama=int(Particle.LocalBestIndex[i])
                    alpha=int(Particle.GlobalBestIndex[0])
                    beta=int(Particle.GlobalBestIndex[1])
                    Particle.V[i,j,It+1]=(InertiaS*Particle.V[i,j,It])+(R2*C2)*((Particle.X[i,j,gama])-(Particle.X[i,j,It]))+(R1*C1)*((Particle.X[alpha,j,beta])-(Particle.X[i,j,It]))               
                    Particle.X[i][j][It+1]=(Particle.V[i][j][It+1]+Particle.X[i][j][It])
                    while Particle.X[i][j][It+1]>MaxB[j] or Particle.X[i][j][It+1]<MinB[j]:
                        if MinB[j]==MaxB[j]:
                            break
                        if Particle.X[i][j][It+1]>MaxB[j]:
                            if np.random.uniform(0,1)>0.1:
                                Particle.V[i,j,It+1]=-1*np.random.uniform(0,1)*Particle.V[i][j][It+1]
                                Particle.X[i][j][It+1]=Particle.X[i][j][It+1]+Particle.V[i,j,It+1]
                            else:
                                Particle.X[i][j][It+1]=MaxB[j]
                                Particle.V[i,j,It+1]=0
                        if Particle.X[i][j][It+1]<MinB[j]:
                                if np.random.uniform(0,1)>0.1:
                                    Particle.V[i,j,It+1]=-1*np.random.uniform(0,1)*Particle.V[i][j][It+1]
                                    Particle.X[i][j][It+1]=Particle.X[i][j][It+1]+Particle.V[i,j,It+1]
                                else:
                                    Particle.X[i][j][It+1]=MinB[j]
                                    Particle.V[i,j,It+1]=0
    with open(DRR+'/IO.txt', 'a') as InputOutputFile:
        txt = "{:2.4E}"
        for i in range(NOP):
            for o in range(NG):
                InputOutputFile.write(txt.format(Particle.Group.Goal[o][i][It])+'\t')
            for j in range(NV):
                InputOutputFile.write(txt.format(Particle.X[i][j][It])+'\t')
            InputOutputFile.write('\n')
    with open  (DRR+"/Particle_BestPosition.txt", 'w') as file:
        for j in range(NV):
            file.write(f'{VN[j]}\t')
        file.write(f'\n')
        for i in range(NOP):
            for j in range(NV):
                file.write(f'{Particle.X[i][j][int(Particle.LocalBestIndex[i])]}\t')
            file.write(f'\n')
    with open  (DRR+"/Particle_CurrentVelocity.txt", 'w') as file:
        for j in range(NV):
            file.write(f'{VN[j]}\t')
        file.write(f'\n')
        for i in range(NOP):
            for j in range(NV):
                file.write(f'{Particle.V[i][j][It]}\t')
            file.write(f'\n')
    if It==0 or (Particle.GlobalBest[It]-Particle.GlobalBest[It-1])!=0:
        #if It>15:
         #   InitialHead(ParticleDirectory[int(Particle.GlobalBestIndex[0])],int(Particle.GlobalBestIndex[1]),int(Particle.GlobalBestIndex[0]))
        SpatialDistribution(ParticleDirectory[int(Particle.GlobalBestIndex[0])],int(Particle.GlobalBestIndex[1]))
        for O in range(len(SOB)):
            Figure(Sim.Stream[O][Particle.GlobalBestIndex[0]][Particle.GlobalBestIndex[1]][0:NSD], Obs.Stream[O][0:NSD], Dir=f"{DRR}/{SON[O]}.png" ,Name=SON[O],GS='Streamflow')
            Figure(Sim.Baseflow[O][Particle.GlobalBestIndex[0]][Particle.GlobalBestIndex[1]][0:NSD], Obs.Baseflow[O][0:NSD], Dir=f"{DRR}/{SON[O]}Base.png",Name=SON[O]+'Base',GS='Baseflow' )
            FigureM(Sim.Stream[O][Particle.GlobalBestIndex[0]][Particle.GlobalBestIndex[1]][0:NSD], Obs.Stream[O][0:NSD], Name=f'{SON[O]}',GS='Streamflow' )
            FigureM(Sim.Baseflow[O][Particle.GlobalBestIndex[0]][Particle.GlobalBestIndex[1]][0:NSD], Obs.Baseflow[O][0:NSD], Name=f'{BON[O]}',GS='Baseflow' )
        for O in range(len(HOC)):
            Figure(Sim.Head[O][Particle.GlobalBestIndex[0]][Particle.GlobalBestIndex[1]][0:NSD], Obs.Head[O][0:NSD], Dir=f"{DRR}/{HON[O]}.png", Name=HON[O],GS='Head')
            FigureM(Sim.Head[O][Particle.GlobalBestIndex[0]][Particle.GlobalBestIndex[1]][0:NSD], Obs.Head[O][0:NSD], Name=f'{HON[O]}',GS='Head')
        for O in range(len(NOB)):
            FigureScatter(Sim=Sim.NO3Con[O][Particle.GlobalBestIndex[0]][Particle.GlobalBestIndex[1]][0:NSD], Obs=[Obs.NO3ConD[O,0:NSD],Obs.NO3ConV[0,0:NSD]],   Dir=f'{DRR}/{NON[O]}.png', Name=NON[O], NSD=NSD)
            FigureScatter2(Sim=Sim.NO3Flux[O][Particle.GlobalBestIndex[0]][Particle.GlobalBestIndex[1]][0:NSD], ObsNO3=[Obs.NO3ConD[O,0:NSD],Obs.NO3ConV[0,0:NSD]], ObsStream=Obs.Stream[0,0:NSD] ,Dir=f'{DRR}/{NON[O]}_2.png', Name=NON[O], NSD=NSD)
    if It>2:
        PVG()
    Xtick_Font,Ytick_Font,YLabel_Font,pad_Font,Title_Font,Legend_Font,W_Fig,H_Fig,LegendP,TitleP,PadV,PadH,Padsize,PadTrans=FontPSO()
    fig=plt.figure(figsize=(1.7*H_Fig,1.2*H_Fig))
    plt.xticks(ticks=None,fontsize=Xtick_Font)
    plt.yticks(ticks=None,fontsize=Ytick_Font)
    plt.ticklabel_format(axis='y',style='sci')
    plt.ylabel('Total Objective function value',fontsize=YLabel_Font, labelpad=10)
    plt.yscale('symlog', linthresh=100)
    plt.title('Global best value',fontsize=Title_Font, pad=15)
    plt.grid(True)
    plt.plot(Particle.GlobalBest[0:It+1],'o--',color='blue')
    plt.tight_layout()
    fig.savefig(DRR+'/Global_Best.png', dpi=DPI)

    fig=plt.figure(figsize=(1.7*H_Fig,1.3*H_Fig))
    plt.xticks(ticks=None,fontsize=Xtick_Font)
    plt.yticks(ticks=None,fontsize=Ytick_Font)
    plt.ticklabel_format(axis='y',style='sci')
    plt.yscale('symlog', linthresh=100)
    plt.ylabel('Total Objective function value',fontsize=YLabel_Font, labelpad=10)
    plt.ylim(2*np.nanmin(Particle.LocalBest[Particle.LocalBest != -np.inf]), np.nanmax(Particle.LocalBest)+0.1*abs(np.nanmax(Particle.LocalBest)))
    plt.title('Local best value',fontsize=Title_Font, pad=15)
    plt.grid(True)
    for i in range(NOP):
        plt.plot(Particle.LocalBest[i,0:It+1],'o--')
    plt.tight_layout()
    fig.savefig(DRR+'/Local_Best.png', dpi=DPI)
    plt.close("all")
    if Particle.GlobalBest[It]>TCir1:
        print(f'the best solution found before max iteration is {Particle.GlobalBest[It]}')
        break
    if It>TCir2+NIS and abs(Particle.GlobalBest[It]-Particle.GlobalBest[It-TCir2])<0.001:
        print(f'the best solution found before max iteration is {Particle.GlobalBest[It]}')
        break
    if abs(np.mean(Particle.LocalBest[0:NOP,It])-Particle.GlobalBest[It])<0.001:
        break
    if It in pm or It==(MNIt-1):
        for O in range(len(HOC)):
            Figure95PPU(Sim.Head[O, 0:NOP,0:MNIt, 0:NSD], Sim.Head[O][Particle.GlobalBestIndex[0]][Particle.GlobalBestIndex[1]][0:NSD], Obs.Head[O][0:NSD],Name=f'95PPU_{HON[O]}', GS='Head')
        for O in range(len(SOB)):
            Figure95PPU(Sim.Stream[O, 0:NOP,0:MNIt, 0:NSD], Sim.Stream[O][Particle.GlobalBestIndex[0]][Particle.GlobalBestIndex[1]][0:NSD], Obs.Stream[O][0:NSD],Name=f'95PPU_{SON[O]}',GS='Stream')
        for O in range(len(NOB)):
            Figure95PPUNO3(AllSim=Sim.NO3Flux[0:NOP][0:MNIt][0:NSD], Sim=Sim.NO3Flux[O][Particle.GlobalBestIndex[0]][Particle.GlobalBestIndex[1]][0:NSD], NO3Obs=Obs.NO3ConV[O,0:-1], N3ObsDate=Obs.NO3ConD[O,0:-1], NO3Stream=Obs.Stream[O][0:NSD], Dir=DRR+'/95PPU_NO3.png')
        for O in range(len(BOB)):
            Figure95PPU(Sim.Baseflow[O, 0:NOP,0:MNIt, 0:NSD], Sim.Baseflow[O][Particle.GlobalBestIndex[0]][Particle.GlobalBestIndex[1]][0:NSD], Obs.Baseflow[O][0:NSD],Name=f'95PPU_{BON[O]}',GS='Baseflow')
    It=It+1
    plt.close("all")
    gc.collect()