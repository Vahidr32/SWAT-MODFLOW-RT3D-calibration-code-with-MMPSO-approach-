def POption():
    from DirSM import DirSM
    DM, DBM, DP, DRR=DirSM()
    with open(DM+'/SWAT-MODFLOW-PSO/Printing.txt', 'r') as file:
        lines=file.readlines()
        for i in range(len(lines)):
            if "ITNS95" in lines[i]:
                pm=[]
                a=int(lines[i].split()[0])
                j=i+1
                while j <i+a+1:
                    if lines[j]!='\n':
                        pm.append(int(lines[j].split()[0]))
                    else:
                         a=a+1
                    j=j+1
    return(pm)