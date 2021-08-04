def rct(DP, RCTVN,RCT_parameter):
    
    import numpy as np
    txt = "{:2.6f}"
    with open(DP+"/NJMOD.rct","r") as file:
        lines=file.readlines()
    try:
        lines[3]=f'0 {txt.format(RCT_parameter[int(RCTVN.index("Bulk"))])}\n'
    except:
        print('no parameter for bulk density')
    try:
        lines[10]=f'{txt.format(RCT_parameter[int(RCTVN.index("Denit"))])}\n'
    except:
        print('no parameter for denitrification')
    try:
        lines[11]=f'{txt.format(RCT_parameter[int(RCTVN.index("MOND"))])}\n'
    except:
        print('no parameter')
    with open(DP+"/NJMOD.rct","w") as file:
        for i in range(len(lines)):
            file.write(lines[i])