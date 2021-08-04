def MNAME():
    from Get_Directory import Get_Directory
    DBM,DP,DRR,DM=Get_Directory()
    with open(DM+"/modflow.mfn", "r") as file:
        lines=file.readlines()
    for i in range(len(lines)):
        if 'DIS' in lines[i]:
            return(lines[i].split()[2][:-4])