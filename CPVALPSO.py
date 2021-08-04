def CPVALPSO(ParticleDirectory,Iteration,Parameter, VN,FileName,MaxB,MinB):
    from RiverCon import RiverCon
    from btn import btn
    from dsp import dsp
    from Pval import Pval
    from rct import rct
    from SWAT_edit import SWAT_edit
    from collections import Counter
    from DirSM import DirSM
    from GWDelay import GWDelay
    CounterParameter = dict(Counter(FileName))
    DM, DBM, D_P, DRR=DirSM()
    try:
        GWDelay(DP=ParticleDirectory,GWDelay= Parameter[FileName.index('link'):   FileName.index('link')+CounterParameter.get('link')])
    except:
          'no parameter for GW delay'
    try:
        btn(DM=DM, DP=ParticleDirectory, Poro_ly= Parameter[FileName.index('BTN_par'):   FileName.index('BTN_par')+CounterParameter.get('BTN_par')])
        dsp(DP=ParticleDirectory, AL=Parameter[FileName.index('Dsp_par'):   FileName.index('Dsp_par')+CounterParameter.get('Dsp_par')], 
        DVN=VN[FileName.index('Dsp_par'):   FileName.index('Dsp_par')+CounterParameter.get('Dsp_par')])
        rct(DP=ParticleDirectory, RCTVN=VN[FileName.index('RCT_par'):   FileName.index('RCT_par')+CounterParameter.get('RCT_par')], RCT_parameter=Parameter[FileName.index('RCT_par'):   FileName.index('RCT_par')+CounterParameter.get('RCT_par')])
    except:
        'no RT3D parameter'
    Pval(DP=ParticleDirectory, Parameter=Parameter,VN=VN)
    try:
        RiverCon(DM=DM,DP=ParticleDirectory,Parameter=Parameter[FileName.index('M_RIVER'):   FileName.index('M_RIVER')+CounterParameter.get('M_RIVER')])
    except:
        'no river parameter'
    SWAT_edit(DP=ParticleDirectory, 
              SVN=VN[FileName.index('SWAT_par'):   FileName.index('SWAT_par')+CounterParameter.get('SWAT_par')],
              SWAT_parameter= Parameter[FileName.index('SWAT_par'):   FileName.index('SWAT_par')+CounterParameter.get('SWAT_par')],
              Max=MaxB[FileName.index('SWAT_par'):   FileName.index('SWAT_par')+CounterParameter.get('SWAT_par')],
              Min=MinB[FileName.index('SWAT_par'):   FileName.index('SWAT_par')+CounterParameter.get('SWAT_par')])

########################        Starting the simulation
   # with open(DM+'/SWAT-MODFLOW-PSO/Initialization.txt','r') as file:
      #  lines=file.readlines()
      #  for i in range(len(lines)):
       #     if 'TimeOut' in lines[i]:
         #       TimeOut=int(lines[i].split()[0])
    import os
    import subprocess
    from pathlib import Path
    os.chdir(ParticleDirectory)
    print(os.getcwd())
    
    #try:
    #subprocess.run(ParticleDirectory+'/swat-modflow3', timeout=TimeOut)
    subprocess.run(ParticleDirectory+'/swat-modflow3')
    #except subprocess.TimeoutExpired:
        #print('time out')
   
    print('the model runing is finished')
########################    Copying the simulated head file

    from shutil import copyfile
    #copyfile(ParticleDirectory+"/swatmf_out_MF_obs",ParticleDirectory+"/swatmf_out_MF_obs"+str(Iteration)+".txt")
    #if os.path.isfile(ParticleDirectory+"/swatmf_out_RT_OBSNO3") is True:
        #copyfile(ParticleDirectory+"/swatmf_out_RT_OBSNO3",ParticleDirectory+"/swatmf_out_RT_OBSNO3"+str(Iteration)+".txt")
########################    Copying the HRU output file
    copyfile(ParticleDirectory+"/output.hru",ParticleDirectory+"/output.hru"+str(Iteration)+".txt")
    copyfile(ParticleDirectory+"/output.rch",ParticleDirectory+"/output.rch"+str(Iteration)+".txt")
    copyfile(ParticleDirectory+"/output.std",ParticleDirectory+"/output.std"+str(Iteration)+".txt")
    if os.path.isfile(ParticleDirectory+"/swatmf_out_MF_head_yearly") is True:
        copyfile(ParticleDirectory+"/swatmf_out_MF_head_yearly",ParticleDirectory+"/swatmf_out_MF_head_yearly"+str(Iteration)+".txt")
        copyfile(ParticleDirectory+"/swatmf_out_MF_recharge_yearly",ParticleDirectory+"/swatmf_out_MF_recharge_yearly"+str(Iteration)+".txt")
            #copyfile(ParticleDirectory+"/swatmf_out_RT_cno3_yearly",ParticleDirectory+"/swatmf_out_RT_cno3_yearly"+str(Iteration)+".txt")
        #if os.path.isfile(ParticleDirectory+"/swatmf_out_SWAT_rivno3") is True:
           # copyfile(ParticleDirectory+"/swatmf_out_SWAT_rivno3",ParticleDirectory+"/swatmf_out_SWAT_rivno3"+str(Iteration)+".txt")
            #copyfile(ParticleDirectory+"/swatmf_out_SWAT_gwsw",ParticleDirectory+"/swatmf_out_SWAT_gwsw"+str(Iteration)+".txt")
