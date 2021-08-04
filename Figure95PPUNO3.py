def Figure95PPUNO3(AllSim, Sim, NO3Obs,N3ObsDate, NO3Stream, Dir):
    import datetime
    from Initialization import Initialization
    from DirSM import DirSM
    from hfunction import NSE, R2, MAE, KGE, Pbias
    import matplotlib.pyplot as plt
    import numpy as np
    import statistics
    from FontPSO import FontPSO
    DM, DBM, DP, DRR=DirSM()
    [NSB,NOP,MNIt,NSY,BYS,BJDS,EJDS,NYSKIP,C1I,C1F,C2I,C2F,RC,NG, NOW, NSD, SDate, FDate,NCores,MMPSO, TCir1, TCir2,DPI]=Initialization(DM=DM)
    Xtick_Font,Ytick_Font,YLabel_Font,pad_Font,Title_Font,Legend_Font,W_Fig,H_Fig,LegendP,TitleP,PadV,PadH,Padsize,PadTrans=FontPSO()
    Minn=[]
    Maxx=[]
    for k in range(NSD):
        PPU=[]
        DDD=[]
        
        for i in range(NOP):
            for j in range(MNIt):
                if np.isnan(AllSim[0][i][j][k])==False:
                    PPU.append(AllSim[0][i][j][k])
        NFP=np.percentile((PPU[0:NSD]),[2.5,97.5])
        Minn.append(NFP[0])
        Maxx.append(NFP[1])
    C=0
    for i in range(NSD):
        if i==int(N3ObsDate[C]):
            DDD.append(N3ObsDate[C])
            C=C+1
    plt.rc('font',family='Times New Roman')
    date = datetime.date(SDate.year,SDate.month,SDate.day)
    dateplot=[]
    value=[]
    for j in range(NSD):
        dateplot.append(date)
        date += datetime.timedelta(days=1)
    dateplot2=[]   
    value=[]
    for i in range(len(DDD)):
        date2 = datetime.date(SDate.year,SDate.month,SDate.day)
        dateplot2.append(date2+datetime.timedelta(days=DDD[i]))
        a=DDD[i]
        value.append(NO3Obs[i]*NO3Stream[int(DDD[i])]*60*60*24/1000)
    fig=plt.figure(figsize=(W_Fig,H_Fig))
    ax = fig.gca()
    ax.plot()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.xticks(ticks=None,fontsize=Xtick_Font)
    plt.yticks(ticks=None,fontsize=Ytick_Font)
    plt.title("NO3 loads at Goondi station",fontsize=Title_Font, loc=TitleP)
    plt.plot(dateplot[0:NSD],Sim[0:NSD], 'red',linewidth=1)
    plt.plot(dateplot2[0:-1],value[:-1], 'blue',linewidth=1,linestyle=' ', marker='o')
    plt.fill_between(dateplot[0:NSD], Minn[0:NSD],Maxx[0:NSD],color='green',alpha=.25)
    plt.ylabel(f'NO3 (kg/day)',fontsize=YLabel_Font)
    #NAshValue=NS(Sim[0:NSD],Obs[0:NSD])
    #PBias=pc_bias(Sim[0:NSD],Obs[0:NSD])
    #MAE=mae(Sim[0:NSD],Obs[0:NSD])
    try:
        Rfactor=(sum(np.array(Maxx[0:NSD])-np.array(Minn[0:NSD]))/(len(Minn[0:NSD])))/(statistics.stdev(value[0:-1]))
    except:
        Rfactor=-999
    C=1
    for i in range(len(value)):
        if 1.2*value[i]>np.array(Minn[int(N3ObsDate[i])]) and 0.8*value[i]<np.array(Maxx[int(N3ObsDate[i])]):
            C=C+1
    try:
        Pfactor=C/(len(value))
    except:
        Pfactor=-999
    try:
        plt.text(dateplot[np.int(NSD-PadH*NSD)], max(value)-PadV*(max(value)-min(value)), f'R-factor={"% +1.3f"%Rfactor}\nP-factor={"% +1.2f"%Pfactor}', style='italic',
        bbox={'facecolor': 'white', 'alpha': PadTrans, 'pad': Padsize},fontsize=pad_Font)
    except:
        print('no values for the plot')
    plt.legend(('Simulated','Observed', '95PPU'),fontsize=Legend_Font, loc=LegendP) 
    fig.savefig(Dir, dpi=DPI)
    plt.close("all")
