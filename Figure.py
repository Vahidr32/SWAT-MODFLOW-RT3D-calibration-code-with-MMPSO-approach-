def Figure(Sim, Obs, Dir, Name,GS):
    import datetime
    from DirSM import DirSM
    from Initialization import Initialization
    from hfunction import NSE, R2, MSE, KGE, Pbias
    import matplotlib.pyplot as plt
    import numpy as np
    from FontPSO import FontPSO
    Xtick_Font,Ytick_Font,YLabel_Font,pad_Font,Title_Font,Legend_Font,W_Fig,H_Fig,LegendP,TitleP,PadV,PadH,Padsize,PadTrans=FontPSO()
    DM, DBM, DP, DRR=DirSM()
    [NSB,NOP,MNIt,NSY,BYS,BJDS,EJDS,NYSKIP,C1I,C1F,C2I,C2F,RC,NG, NOW, NSD, SDate, FDate,NCores,MMPSO, TCir1, TCir2,DPI]=Initialization(DM=DM)
    
    
    plt.rc('font',family='Times New Roman')
    date = datetime.date(SDate.year,SDate.month,SDate.day)
    dateplot=[]
    for j in range(NSD):
        date += datetime.timedelta(days=1)
        dateplot.append(date)
    fig=plt.figure(figsize=(W_Fig,H_Fig))
    ax = fig.gca()
    ax.plot()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.title(Name,fontsize=Title_Font, loc=TitleP)
    plt.plot(dateplot[:-1],Sim[:-1], 'red',linewidth=1,alpha=0.8)
    plt.plot(dateplot[:-1],Obs[:-1], 'blue',linewidth=1,alpha=0.8)
    if GS=='Baseflow' or GS=='Streamflow':
        plt.ylabel('streamflow (m\u00b3/s)',fontsize=YLabel_Font)
        #if GS=='Streamflow':
           # if np.max(Sim)>1000:
            #    plt.yscale('symlog', linthresh=300)
           # if np.max(Sim)>100 and np.max(Sim)<500:
            #    plt.yscale('symlog', linthresh=50)
           # if np.max(Sim)<50:
            #    plt.yscale('symlog', linthresh=10)
    if GS=='Head':
        plt.ylim(np.nanmin([np.nanmin(Sim),np.nanmin(Obs)])-0.1*(np.nanmax([np.nanmax(Sim), np.nanmax(Obs)])-np.nanmin([np.nanmin(Sim),np.nanmin(Obs)])), np.nanmax([np.nanmax(Sim),np.nanmax(Obs)])+0.3*(np.nanmax([np.nanmax(Sim),np.nanmax(Obs)])-np.nanmin([np.nanmin(Sim),np.nanmin(Obs)])))
        plt.ylabel('Head (m)',fontsize=YLabel_Font)
    plt.xticks(ticks=None,fontsize=Xtick_Font)
    plt.yticks(ticks=None,fontsize=Ytick_Font) 
    NAshValue=NSE(Sim[:NSD],Obs[:NSD])
    PBias=Pbias(Sim[:NSD],Obs[:NSD])
    MSE=MSE(Sim[:NSD],Obs[:NSD])
    R2=R2(Sim[0:NSD],Obs[0:NSD])
    plt.text(dateplot[np.int(NSD-PadH*NSD)], max(Obs)-PadV*(max(Obs)-min(Obs)), f'NSE={"% +1.3f"%NAshValue}\nMSE={"% +1.3f"%MSE}\nPBias={"% +1.3f"%PBias}\nR\u00b2={"% +1.3f"%R2}', style='italic',
        bbox={'facecolor': 'white', 'alpha': PadTrans, 'pad': Padsize},fontsize=pad_Font)
    plt.legend(('Simulated','Observed'),fontsize=Legend_Font, loc=LegendP) 
    fig.savefig(Dir, dpi=DPI)
    plt.close("all")
