def RiverCon(DM,DP,Parameter):
    from MNAME import MNAME
    MNAME=MNAME()
    with open  (DM+f'/SWAT-MODFLOW-PSO/Particles/MODFLOW/{MNAME}.riv','r') as file:
        lines=file.readlines()
        Stage=[]
        Con=[]
        Bed=[]
        Column=[]
        Layer=[]
        Row=[]
        L=[]
        txt = "{:18.12E}"
        for i in range(len(lines)):
            if "Layer Row Column Stage Cond Rbot IFACE" in lines[i]:
                Layer.append(float(lines[i].split()[0]))
                Row.append(float(lines[i].split()[1]))
                Column.append(float(lines[i].split()[2]))
                Stage.append(float(lines[i].split()[3]))
                Con.append(float(lines[i].split()[4]))
                Bed.append(float(lines[i].split()[5]))
                L.append(i)
    with open  (DP+f"/{MNAME}.riv",'w') as file:
        C=0
        for i in range(len(lines)):
            if i in L:
                file.write(f'{    int(Layer[C])}   {int(Row[C])}   {int(Column[C])}  {txt.format(Stage[C]+((Stage[C]-Bed[C])*Parameter[1]))}  {txt.format(Con[C]*(10**Parameter[0]))}   {txt.format(Bed[C]-((Stage[C]-Bed[C])*Parameter[2]))}')
                file.write('      0 # Data Set 6: Layer Row Column Stage Cond Rbot IFACE\n')
                C=C+1
            else:
                 file.write(lines[i])