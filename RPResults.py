def RPResults(ParticleDirectory, MNIt):
    import os
    from MNAME import MNAME
    MNAME=MNAME()
    for i in range (len(ParticleDirectory)):
        #if os.path.isfile(ParticleDirectory[i]+ "/output.hru") is True: os.remove(ParticleDirectory[i]+ "/output.hru")
        #if os.path.isfile(ParticleDirectory[i]+ "/output.rch") is True: os.remove(ParticleDirectory[i]+ "/output.rch")
        #if os.path.isfile(ParticleDirectory[i]+ "/output.sed") is True: os.remove(ParticleDirectory[i]+ "/output.sed")
        if os.path.isfile(ParticleDirectory[i]+ f"/{MNAME}.out") is True: os.remove(ParticleDirectory[i]+ f"/{MNAME}.out")
        if os.path.isfile(ParticleDirectory[i]+"/swatmf_out_RT_OBSNO3") is True: os.remove(ParticleDirectory[i]+"/swatmf_out_RT_OBSNO3")
        if os.path.isfile(ParticleDirectory[i]+ "/swatmf_out_RT_OBSP") is True: os.remove(ParticleDirectory[i]+ "/swatmf_out_RT_OBSP")
        if os.path.isfile(ParticleDirectory[i]+ "/swatmf_out_RT_rivno3") is True: os.remove(ParticleDirectory[i]+ "/swatmf_out_RT_rivno3")
        if os.path.isfile(ParticleDirectory[i]+"/swatmf_out_RT_rivP") is True: os.remove(ParticleDirectory[i]+"/swatmf_out_RT_rivP")
        if os.path.isfile(ParticleDirectory[i]+ "/swatmf_out_SWAT_rivno3") is True: os.remove(ParticleDirectory[i]+ "/swatmf_out_SWAT_rivno3")
        if os.path.isfile(ParticleDirectory[i]+ "/swatmf_out_SWAT_rivP") is True: os.remove(ParticleDirectory[i]+ "/swatmf_out_SWAT_rivP")
        if os.path.isfile(ParticleDirectory[i]+ "/swatmf_out_RT_CONCP") is True: os.remove(ParticleDirectory[i]+ "/swatmf_out_RT_CONCP")
        if os.path.isfile(ParticleDirectory[i]+"/swatmf_out_RT_CONCNO3") is True: os.remove(ParticleDirectory[i]+"/swatmf_out_RT_CONCNO3")
        if os.path.isfile(ParticleDirectory[i]+"/swatmf_out_RT_rechno3") is True: os.remove(ParticleDirectory[i]+"/swatmf_out_RT_rechno3")
        if os.path.isfile(ParticleDirectory[i]+ "/swatmf_out_RT_rechP") is True: os.remove(ParticleDirectory[i]+ "/swatmf_out_RT_rechP")
        if os.path.isfile(ParticleDirectory[i]+"/swatmf_out_SWAT_rechno3") is True: os.remove(ParticleDirectory[i]+"/swatmf_out_SWAT_rechno3")
        if os.path.isfile(ParticleDirectory[i]+"/swatmf_out_SWAT_rechP") is True: os.remove(ParticleDirectory[i]+"/swatmf_out_SWAT_rechP")
        if os.path.isfile(ParticleDirectory[i]+"/swatmf_out_MF_obs") is True: os.remove(ParticleDirectory[i]+"/swatmf_out_MF_obs")
        if os.path.isfile(ParticleDirectory[i]+"/swatmf_out_RT_out") is True: os.remove(ParticleDirectory[i]+"/swatmf_out_RT_out")    
    for i in range(len(ParticleDirectory)):
        for j in range (MNIt):
            if os.path.isfile(ParticleDirectory[i]+"/output.rch"+str(j)+".txt") is True:
                try:
                    os.remove(ParticleDirectory[i]+"/output.hru"+str(j)+".txt")
                    os.remove(ParticleDirectory[i]+"/output.std"+str(j)+".txt")
                except: 
                       print('no hru or std saved before')
                if os.path.isfile(ParticleDirectory[i]+"/output.rch"+str(j)+".txt") is True: os.remove(ParticleDirectory[i]+"/output.rch"+str(j)+".txt")
                if os.path.isfile(ParticleDirectory[i]+"/swatmf_out_MF_obs"+str(j)+".txt") is True: os.remove(ParticleDirectory[i]+"/swatmf_out_MF_obs"+str(j)+".txt")
                if os.path.isfile(ParticleDirectory[i]+"/swatmf_out_MF_head_yearly"+str(j)+".txt") is True: os.remove(ParticleDirectory[i]+"/swatmf_out_MF_head_yearly"+str(j)+".txt")
                if os.path.isfile(ParticleDirectory[i]+"/swatmf_out_RT_cno3_yearly"+str(j)+".txt") is True: os.remove(ParticleDirectory[i]+"/swatmf_out_RT_cno3_yearly"+str(j)+".txt")
                if os.path.isfile(ParticleDirectory[i]+"/swatmf_out_MF_recharge_yearly"+str(j)+".txt") is True: os.remove(ParticleDirectory[i]+"/swatmf_out_MF_recharge_yearly"+str(j)+".txt")
                if os.path.isfile(ParticleDirectory[i]+"/swatmf_out_RT_OBSNO3"+str(j)+".txt") is True: os.remove(ParticleDirectory[i]+"/swatmf_out_RT_OBSNO3"+str(j)+".txt")
                if os.path.isfile(ParticleDirectory[i]+"/swatmf_out_SWAT_rivno3"+str(j)+".txt") is True: os.remove(ParticleDirectory[i]+"/swatmf_out_SWAT_rivno3"+str(j)+".txt")
                if os.path.isfile(ParticleDirectory[i]+"/swatmf_out_SWAT_gwsw"+str(j)+".txt") is True: os.remove(ParticleDirectory[i]+"/swatmf_out_SWAT_gwsw"+str(j)+".txt")