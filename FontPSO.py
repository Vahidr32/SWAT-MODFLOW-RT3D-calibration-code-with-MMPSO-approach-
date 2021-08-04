def FontPSO():
    from DirSM import DirSM
    from Get_Directory import Get_Directory
    DBM,DP,DRR,DM=Get_Directory()
    DM, DBM, DP, DRR=DirSM()
    with open(DM+'/SWAT-MODFLOW-PSO/Printing.txt','r') as file:
        lines=file.readlines()
        for i in range(len(lines)):
            if 'Xtick_Font' in lines[i]:Xtick_Font=float(lines[i].split()[0])
            if 'Ytick_Font' in lines[i]:Ytick_Font=float(lines[i].split()[0])
            if 'YLabel_Font' in lines[i]:YLabel_Font=float(lines[i].split()[0])
            if 'pad_Font' in lines[i]:pad_Font=float(lines[i].split()[0])
            if 'Title_Font' in lines[i]:Title_Font=float(lines[i].split()[0])
            if 'Legend_Font' in lines[i]:Legend_Font=float(lines[i].split()[0])
            if 'W_Fig' in lines[i]:W_Fig=float(lines[i].split()[0])
            if 'H_Fig' in lines[i]:H_Fig=float(lines[i].split()[0])
            if 'LegendP' in lines[i]:LegendP=str(lines[i].split()[0]+' '+lines[i].split()[1])
            if 'TitleP' in lines[i]:TitleP=(lines[i].split()[0])
            if 'PadV' in lines[i]:PadV=float(lines[i].split()[0])
            if 'PadH' in lines[i]:PadH=float(lines[i].split()[0])
            if 'Padsize' in lines[i]:Padsize=float(lines[i].split()[0])
            if 'PadTrans' in lines[i]:PadTrans=float(lines[i].split()[0])
    return(Xtick_Font,
    Ytick_Font,YLabel_Font,pad_Font,
    Title_Font,Legend_Font,W_Fig,H_Fig,
    LegendP,
    TitleP,
    PadV,
    PadH,
    Padsize,
    PadTrans)