def GWD(DM):
    with open(DM+'/SWAT-MODFLOW-PSO/Initialization.txt') as file:
        lines=file.readlines()
        for i in range(len(lines)):
            if 'GW_rows' in lines[i]:
                GW_rows=int(lines[i].split()[0])
            if 'GW_Col' in lines[i]:
                GW_Col=int(lines[i].split()[0])
            if 'GW_Layers' in lines[i]:
                GW_Layers=int(lines[i].split()[0])
    return (GW_rows, GW_Col,GW_Layers)
