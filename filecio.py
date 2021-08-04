def filecio(DM,NSY,BYS,BJDS,EJDS,NYSKIP):
    for d in range(len(DM)):
        f=open(DM[d]+"/file.cio","r") 
        lines=f.readlines()
        f.close()
        for i in range (len(lines)):
            
            if "NBYR" in lines[i]:
                lines[i]=f'               {NSY}    | NBYR : Number of years simulated\n'
            if "IYR" in lines[i]:
                lines[i]=f'            {BYS}    | IYR : Beginning year of simulation\n'
            if "IDAF" in lines[i]:
                lines[i]=f'               {BJDS}    | IDAF : Beginning julian day of simulation\n'
            if "IDAL" in lines[i]:
                lines[i]=f'             {EJDS}    | IDAL : Ending julian day of simulation\n'
            if "NYSKIP" in lines[i]:
                lines[i]=f'               {NYSKIP}    | NYSKIP: number of years to skip output printing/summarization\n'
                
        ff=open(DM[d]+"/file.cio","w")
        for i in range (len(lines)):
            ff.write(lines[i])
    ff.close()