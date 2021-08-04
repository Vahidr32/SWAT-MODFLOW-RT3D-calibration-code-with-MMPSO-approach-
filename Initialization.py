def Initialization(DM):
    f=open(DM+"/SWAT-MODFLOW-PSO/Initialization.txt","r")
    lines=f.readlines()
    f.close()
    for i in range(len(lines)):
        if 'NSB' in lines[i]:
            NSB=int(lines[i].split()[0])
        if 'NOP' in lines[i]:
            NOP=int(lines[i].split()[0])
        if 'MNIt' in lines[i]:
            MNIt=int(lines[i].split()[0])
        if 'NSY' in lines[i]:
            NSY=int(lines[i].split()[0])
        if 'BYS' in lines[i]:
            BYS=int(lines[i].split()[0])
        if 'BJDS' in lines[i]:
            BJDS=int(lines[i].split()[0])
        if 'EJDS' in lines[i]:
            EJDS=int(lines[i].split()[0])
        if 'NYSKIP' in lines[i]:
            NYSKIP=int(lines[i].split()[0])
        if 'C1I' in lines[i]:
            C1I=float(lines[i].split()[0])
        if 'C1F' in lines[i]:
            C1F=float(lines[i].split()[0])
        if 'C2I' in lines[i]:
            C2I=float(lines[i].split()[0])
        if 'C2F' in lines[i]:
            C2F=float(lines[i].split()[0])
        if 'RC' in lines[i]:
            RC=float(lines[i].split()[0])
        if 'NG' in lines[i]:
            NG=int(lines[i].split()[0])
        if 'NCores' in lines[i]:
            NCores=int(lines[i].split()[0])
        if 'MMPSO' in lines[i]:
            MMPSO=int(lines[i].split()[0])
        if 'TCir1' in lines[i]:
            TCir1=int(lines[i].split()[0])
        if 'TCir2' in lines[i]:
            TCir2=int(lines[i].split()[0])
        if 'DPI' in lines[i]:
            DPI=int(lines[i].split()[0])

    import datetime        
    BDate= datetime.datetime(BYS, 1, 1) + datetime.timedelta(BJDS-1)
    SkippedDate=datetime.datetime(BYS+NYSKIP, BDate.month, BDate.day)+ datetime.timedelta(-BJDS)
    SDate=datetime.datetime(BYS+NYSKIP, 1, 1)
    FDate=datetime.datetime(BYS+NSY-1, 1, 1) + datetime.timedelta(EJDS-1)
    delta = FDate - SDate
    NSD=delta.days+1
    #Number of Skipping days
    delta = SkippedDate - BDate
    NOW=delta.days+1
    return(NSB,NOP,MNIt,NSY,BYS,BJDS,EJDS,NYSKIP,C1I,C1F,C2I,C2F,RC,NG, NOW, NSD, SDate, FDate,NCores,MMPSO,TCir1,TCir2,DPI)