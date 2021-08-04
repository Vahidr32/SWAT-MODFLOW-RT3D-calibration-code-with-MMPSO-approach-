def GWDelay(DP, GWDelay):
    
    with open(DP+'/swatmf_link.txt','r') as files:
        lines=files.readlines()
    for i in range(len(lines)):
        if "GW_DELAY" in lines[i]:
            lines[i]=f'{str(GWDelay[0])}    GW_DELAY : Groundwater delay [days]'
    with open(DP+'/swatmf_link.txt','w') as files: 
        for i in range(len(lines)):
            files.write(lines[i])


