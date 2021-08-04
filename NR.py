#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from DirSM import DirSM
from Par_input import Par_input
from Initialization import Initialization
import itertools
import numpy as np
VN=[]
Max=[]
Min=[]
NG=[]
from Get_Directory import Get_Directory
DBM,DP,DRR,DM=Get_Directory()
with open(DM+'/SWAT-MODFLOW-PSO/Parameter_input.txt','r') as file:
    lines=file.readlines()
    for i in range(1,len(lines)):
        VN.append(lines[i].split()[1])
        Max.append(float(lines[i].split()[4]))
        Min.append(float(lines[i].split()[6]))
        


NV=len(VN)





with open(DM+'/SWAT-MODFLOW-PSO/Initialization.txt','r') as file:
    lines=file.readlines()
    for i in range(len(lines)):
        if 'NG' in lines[i]:
            NG=int(lines[i].split()[0])

with open  (DRR+'/Particle_BestPosition.txt','r') as file:    
    lines=file.readlines()
    BestParameter=np.zeros([NV,len(lines)-1])
    for j in range(NV):
        for i in range(1,len(lines)):
            BestParameter[j,i-1]=lines[i].split()[j]
            
    
with open  (DRR+'/IO.txt','r') as file:    
    lines=file.readlines()
    Parameter=np.zeros([len(lines),NV])
    Objective=np.zeros([len(lines)])

    C=0
    for i in range(len(lines)):
       
        for j in range(NG):
            Objective[C]=float(lines[i].split()[j])+Objective[C]
        for j in range(NV):
            Parameter[C,j]=float(lines[i].split()[NG+j])
        C=C+1

        
deleting=[]

for i in range(len(VN)):
    if Max[i]-Min[i]==0:
        deleting.append(i)    

Parameter=list(np.delete(Parameter,deleting,1))  
BestParameter=(np.delete(BestParameter,deleting,0))      
VN=list(np.delete(VN,deleting,0)) 
Min=list(np.delete(Min,deleting,0)) 
Max=list(np.delete(Max,deleting,0)) 


NV=NV-len(deleting)
    
    
deleting=[]

for i in range(len(lines)):
    if Objective[i]<np.nanpercentile(Objective,40) or np.isnan(Objective[i])==True:
        deleting.append(i)    

Objective=(np.delete(Objective,deleting,0))
Parameter=(np.delete(Parameter,deleting,0))

print('Global Best',np.nanmax(Objective))
print('Variance',np.nanvar(Objective))





t = np.zeros(Parameter.shape[0])
for i in range(len(t)):
    if i==0:
        t[i]=int(0)
    else:
        t[i]=int(t[i-1]+1) 
        
c = list(itertools.combinations(t, 2))    




Jacobian=np.zeros([len(c),NV])


Objective=list(Objective)
print('Global Best Index',Objective.index(max(Objective)))
Parameter=list(Parameter)
import sys

for i in range(len(c)):
    alpha=int(c[i][0])
    beta=int(c[i][1])
    sys.stdout.write('\rUpdated record: ' + str(i) + ' of ' + str(len(c)))
    sys.stdout.flush()
    for j in range(NV):
        if Parameter[alpha][j]-Parameter[beta][j]!=0:
            Jacobian[i][j]=(Objective[alpha]-Objective[beta])/(Parameter[alpha][j]-Parameter[beta][j])
        if np.isnan(Jacobian[i][j])==True:
            print('jacobian encountered nan value')
            Jacobian[i][j]=0
Hessian=np.array(np.dot(Jacobian.T, Jacobian))
Cor=(np.var(Objective[:-1])*NV*np.var(Jacobian))*np.linalg.inv(Hessian)
CC=(np.var(Objective[:-1])*np.linalg.inv(Hessian))

with open(DRR+'/newrange.txt','w') as file:
    file.write('VariableName\tMaxN\tMinN\tMaxB\tMinB\tMaxO\tMinO\Sensitivity\n')
    txt = "{:1.3f}"
    txt2="{:2.4e}"
    for i in range(NV):
        file.write(f'{VN[i]}\t')
        alpha=np.percentile(BestParameter[i,:-1],[2.5, 97.5])[1]
        beta=np.percentile(BestParameter[i,:-1],[2.5 ,97.5])[0]
        file.write(f'{txt.format(alpha+1.95*abs((Max[i]-beta)/(Max[i]-Min[i]))*np.sqrt(Cor[i][i]))}\t')
        file.write(f'{txt.format(beta-1.95*abs((alpha-Min[i])/(Max[i]-Min[i]))*np.sqrt(Cor[i][i]))}\t')
        file.write(f'{txt.format(max(BestParameter[i,:-1]))}\t')
        file.write(f'{txt.format(min(BestParameter[i,:-1]))}\t')
        file.write(f'{txt.format(Max[i])}\t')
        file.write(f'{txt.format(Min[i])}\t')
        file.write(f'{txt2.format(np.sqrt(CC[i][i]))}\n')

