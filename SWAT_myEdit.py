def SWAT_myEdit(DP, DG, V, VS, VF, VV):
    import glob
    from DirSM import DirSM
    import ntpath
    DM, DBM, D_P, DRR=DirSM()
    Name=glob.glob(DM+'/Backup'+'/*.'+VS)
    # we should note that this code can edit any parameter in GW files, Sub files, bsn file and rte files
    if VS=='mgt' or VS=='rte' or VS=='sub' or VS=='bsn' or VS=='gw' or VS=='hru':
        if len(VF)==0: VF='ArcSWAT'
        if VS=='mgt': txt = "{:2.2f}"
        if VS=='rte' or 'sub': txt = "{:3.3f}"
        if VS=='gw': txt = "{:3.4f}"
        if VS=='hru': txt = "{:3.4f}"
        if VS=='gw': V=V+" "
        if VS=='bsn': txt = "{:1.3f}"
        if V=='FertilizerAM':
            for j in range(len(Name)):
                if DG=='v':
                    with open(DP+'/'+ ntpath.basename(Name[j]), "r") as file: lines=file.readlines()
                    for k in range(len(VF)):
                        if VF[k] in lines[0]:
                            for i in range(len(lines)):
                                if 'Operation Schedule:' in lines[i]:
                                    for m in range(len(lines)-i):
                                        try:
                                            if lines[i+m].split()[2]=='3':
                                                a=lines[i+m].replace(lines[i+m].split()[4], str(VV))
                                                lines[i+m]=a
                                        except:
                                            'next line'
                            with open(DP+'/'+ ntpath.basename(Name[j]), "w") as file:                
                                for i in range(len(lines)):
                                    file.write(lines[i])
        if V=='FertilizerTD':
            for j in range(len(Name)):
                if DG=='v':
                    with open(DP+'/'+ ntpath.basename(Name[j]), "r") as file: lines=file.readlines()
                    for k in range(len(VF)):
                        if VF[k] in lines[0]:
                            for i in range(len(lines)):
                                if 'Operation Schedule:' in lines[i]:
                                    for m in range(len(lines)-i):
                                        try:
                                            if lines[i+m].split()[2]=='3':
                                                a=lines[i+m].replace(lines[i+m].split()[1], str(int(VV)))
                                                lines[i+m]=a
                                        except:
                                            'next line'
                            with open(DP+'/'+ ntpath.basename(Name[j]), "w") as file:                
                                for i in range(len(lines)):
                                    file.write(lines[i])
        if V=='GrazingM':
            for j in range(len(Name)):
                if DG=='v':
                    with open(DP+'/'+ ntpath.basename(Name[j]), "r") as file: lines=file.readlines()
                    for k in range(len(VF)):
                        if VF[k] in lines[0]:
                            for i in range(len(lines)):
                                if 'Operation Schedule:' in lines[i]:
                                    for m in range(len(lines)-i):
                                        try:
                                            if lines[i+m].split()[2]=='9':
                                                a=lines[i+m].replace(lines[i+m].split()[7], str(VV))
                                                lines[i+m]=a
                                        except:
                                            'next line'
                            with open(DP+'/'+ ntpath.basename(Name[j]), "w") as file:                
                                for i in range(len(lines)):
                                    file.write(lines[i])
        if V!='GrazingM' and V!='FertilizerTD' and V!='FertilizerAM':
            for j in range(len(Name)):
                if DG=='v':
                    with open(DP+'/'+ ntpath.basename(Name[j]), "r") as file: lines=file.readlines()
                    for k in range(len(VF)):
                        if VF[k] in lines[0]:
                            for i in range(len(lines)):
                                if V in lines[i]:
                                    a=lines[i].replace(lines[i].split()[0], txt.format(VV))
                                    lines[i]=a
                        with open(DP+'/'+ ntpath.basename(Name[j]), "w") as file:                
                            for i in range(len(lines)):
                                file.write(lines[i])
                if DG=='r':
                    with open(Name[j],'r') as file: lines=file.readlines()
                    for n in range(len(VF)):
                        if VF[n] in lines[0]:
                            for i in range(len(lines)):
                                    if V in lines[i]:
                                        lines[i]=lines[i].replace(lines[i].split()[0],(str(float(lines[i].split()[0])+VV*float(lines[i].split()[0])))) 
                            with open(DP+'/'+ ntpath.basename(Name[j]),'r') as file: 
                                lines2=file.readlines()
                                for i in range(len(lines2)):
                                    if V in lines2[i]:
                                        lines2[i]=lines[i]
                            with open(DP+'/'+ ntpath.basename(Name[j]),'w') as f:
                                for i in range(len(lines2)):
                                    f.write(lines2[i])
    if VS=='sol':
        if V=='SOL_AWC()': V1,txt='Ave. AW Incl. Rock Frag  :',"{:12.2f}" 
        if V=='SOL_CBN()': V1,txt='Organic Carbon [weight %]:',"{:12.2f}"
        if V=='SOL_K()':   V1,txt='Ksat. (est.)      [mm/hr]:',"{:12.2f}"
        if V=='ANION_EXCL': V2,txt=' Porosity fraction from which anions are excluded:',"{:1.3f}"
        else: V2="Nist"
        for j in range(len(Name)):
            a=[]
            if DG=='r':
                with open(Name[j],'r') as file: lines=file.readlines()
                for n in range(len(VF)):
                    if VF[n] in lines[0]:
                        lines_modified=[]
                        for i in range(len(lines)):
                                if V1 in lines[i]:
                                    for k in range(len(lines[i].split(':')[1].split())):
                                        a.append((float(lines[i].split(':')[1].split()[k])+VV*float(lines[i].split(':')[1].split()[k]))) 
                                    lines[i]=lines[i].split(':')[0]+':'
                                    for k in range(len(a)):
                                        lines[i]=lines[i]+txt.format(a[k])
                                    lines_modified.append(lines[i]+'\n')
                                if V2 in lines[i]:
                                    lines_modified.append(lines[i].replace(lines[i].split(':')[1],' '+ txt.format(VV)+'\n'))
                        with open(DP+'/'+ ntpath.basename(Name[j]),'r') as file: lines=file.readlines()
                        for i in range(len(lines)):
                            if V1 in lines[i]:
                                lines[i]=', '.join(map(str, lines_modified))
                            if V2 in lines[i]:
                                lines[i]=', '.join(map(str, lines_modified))
                        with open(DP+'/'+ ntpath.basename(Name[j]),'w') as f:
                            for i in range(len(lines)):
                                f.write(lines[i])
            if DG=='v':
                with open(DP+'/'+ ntpath.basename(Name[j]),'r') as file: lines=file.readlines()
                for k in range(len(VF)):
                    if VF[k] in lines[0]:
                        lines_modified=[]
                        for i in range(len(lines)):
                                if V2 in lines[i]:
                                    a=lines[i].replace(lines[i].split(':')[1],' '+ txt.format(VV)+'\n')
                                    lines[i]=a
                        with open(DP+'/'+ ntpath.basename(Name[j]), "w") as file:
                            for i in range(len(lines)):
                                file.write(lines[i])