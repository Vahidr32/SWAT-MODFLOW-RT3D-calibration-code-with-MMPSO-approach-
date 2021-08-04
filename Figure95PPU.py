def Figure95PPU(AllSim, Sim, Obs, Name, GS):
    from Initialization import Initialization
    from DirSM import DirSM
    import datetime
    from hfunction import NSE, R2, MSE, KGE, Pbias
    import matplotlib.pyplot as plt
    import numpy as np
    import statistics
    from FontPSO import FontPSO
    Xtick_Font,Ytick_Font,YLabel_Font,pad_Font,Title_Font,Legend_Font,W_Fig,H_Fig,LegendP,TitleP,PadV,PadH,Padsize,PadTrans=FontPSO()
    DM, DBM, DP, DRR=DirSM()
    plt.rc('font',family='Times New Roman')
    [NSB,NOP,MNIt,NSY,BYS,BJDS,EJDS,NYSKIP,C1I,C1F,C2I,C2F,RC,NG, NOW, NSD, SDate, FDate,NCores,MMPSO, TCir1, TCir2,DPI]=Initialization(DM=DM)
    Minn=[]
    Maxx=[]
    for k in range(NSD):
        PPU=[]
        for i in range(NOP):
            for j in range(MNIt):
                PPU.append(AllSim[i][j][k])
        NFP=np.nanpercentile((PPU[0:NSD]),[2.5,97.5])
        Minn.append(NFP[0])
        Maxx.append(NFP[1])
    date = datetime.date(SDate.year,SDate.month,SDate.day)
    dateplot=[]
    for j in range(NSD):
        dateplot.append(date)
        date += datetime.timedelta(days=1)
    fig=plt.figure(figsize=(W_Fig,H_Fig))
    ax = fig.gca()
    ax.plot()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.title(Name,fontsize=Title_Font, loc=TitleP)
    plt.plot(dateplot[0:NSD],Sim[0:NSD], 'red',linewidth=1)
    plt.plot(dateplot[0:NSD],Obs[0:NSD], 'blue',linewidth=1)
    plt.xticks(ticks=None,fontsize=Xtick_Font)
    plt.yticks(ticks=None,fontsize=Ytick_Font)  
    plt.fill_between(dateplot[0:NSD], Minn[0:NSD],Maxx[0:NSD],color='green',alpha=.30)
    if GS=="Head":
        plt.ylabel(f'GW head elevation (m)',fontsize=YLabel_Font)
    if GS=="Stream":
        plt.ylabel(f'Streamflow (m3/s)',fontsize=YLabel_Font)
    NAshValue=NSE(Sim[0:NSD],Obs[0:NSD])
    PBias=Pbias(Sim[0:NSD],Obs[0:NSD])
    MSE=MSE(Sim[0:NSD],Obs[0:NSD])
    R2=R2(Sim[0:NSD],Obs[0:NSD])
    try:
        Rfactor=(sum(np.array(Maxx[0:NSD])-np.array(Minn[0:NSD]))/(len(Minn[0:NSD])))/(statistics.stdev(Obs[0:NSD]))
    except:
        Rfactor=-999
        
    C=1
    for i in range(NSD):
        if 1.1*Obs[i]>np.array(Minn[i]) and 0.9*Obs[i]<np.array(Maxx[i]):
            C=C+1
    Pfactor=C/(NSD)
    plt.text(dateplot[np.int(NSD-PadH*NSD)],max(Maxx)-PadV*(max(Maxx)-min(Maxx)) , f'Nash={"% +1.3f"%NAshValue}\nMSE={"% +1.3f"%MSE}\nPBias={"% +1.3f"%PBias}\nR\u00b2={"% +1.3f"%R2}\nR-factor={"% +1.3f"%Rfactor}\nP-factor={"% +1.2f"%Pfactor}', style='italic',
        bbox={'facecolor': 'white', 'alpha': PadTrans, 'pad': Padsize},fontsize=pad_Font)
    plt.legend(('Simulated','Observed', '95PPU'),fontsize=Legend_Font, loc=LegendP) 
    fig.savefig(f'{DRR}/{Name}.png', dpi=DPI)
    plt.close("all")