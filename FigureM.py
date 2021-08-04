def FigureM(s,o,Name,GS):
    from Initialization import Initialization
    from Get_Directory import Get_Directory
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from hfunction import NSE, R2, MSE, KGE, Pbias
    import datetime
    from matplotlib.ticker import MaxNLocator
    from matplotlib.ticker import StrMethodFormatter
    from matplotlib.dates import DateFormatter
    from FontPSO import FontPSO
    #importing priting variables
    Xtick_Font,Ytick_Font,YLabel_Font,pad_Font,Title_Font,Legend_Font,W_Fig,H_Fig,LegendP,TitleP,PadV,PadH,Padsize,PadTrans=FontPSO()
    #setting the font family
    plt.rc('font',family='Times New Roman')
    # reading the directory
    DBM,DP,DRR,DM=Get_Directory()
    # importing initialization variables from initialization.txt
    [NSB,NOP,MNIt,NSY,BYS,BJDS,EJDS,NYSKIP,C1I,C1F,C2I,C2F,RC,NG, NOW, NSD, SDate, FDate,NCores,MMPSO, TCir1, TCir2,DPI]=Initialization(DM=DM)
    dti = pd.date_range(SDate, FDate, freq="D")
    fig=plt.figure(figsize=(W_Fig,H_Fig))
    ax = fig.gca()
    ax.plot()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    df1=pd.DataFrame({'SimulatedStream':s[0:NSD], 'Date':dti})
    df1 = df1.resample('M', on='Date').mean()
    plt.plot(df1.SimulatedStream, color='red',linewidth=1)
    df2=pd.DataFrame({'ObservedStream':o[0:NSD], 'Date':dti})
    df2 = df2.resample('M', on='Date').mean()
    plt.plot(df2.ObservedStream,color='blue',linewidth=1,alpha=0.9)
    date = datetime.date(SDate.year,SDate.month,SDate.day)
    if GS=="Streamflow" or GS=="Baseflow" :
        plt.ylabel(f'{GS} (m\u00b3/s)',fontsize=YLabel_Font)
    else:
        plt.ylabel(f'{GS} (m)',fontsize=YLabel_Font)
    plt.title(f'{Name}_Monthly',fontsize=Title_Font, loc=TitleP)
    dateplot=[]
    for j in range(NSD):
        date += datetime.timedelta(days=1)
        dateplot.append(date)
    plt.xticks(ticks=None,fontsize=Xtick_Font)
    plt.yticks(ticks=None,fontsize=Ytick_Font)
    plt.gca().xaxis.set_major_locator(MaxNLocator(f'{int(NSY*3)}'))
    date_form = DateFormatter("%Y-%m")
    plt.gca().xaxis.set_major_formatter(date_form)
    NAshValue=NSE(np.array(df1.SimulatedStream),np.array(df2.ObservedStream))
    PBias=Pbias(np.array(df1.SimulatedStream),np.array(df2.ObservedStream))
    MSE=MSE(np.array(df1.SimulatedStream),np.array(df2.ObservedStream))
    R2=R2(np.array(df1.SimulatedStream),np.array(df2.ObservedStream))
    plt.text(dateplot[np.int(NSD-PadH*NSD)], max(np.array(df2.ObservedStream))-PadV*(max(np.array(df2.ObservedStream))-min(np.array(df2.ObservedStream))), f'Nash={"% +1.3f"%NAshValue}\nMSE={"% +1.3f"%MSE}\nPBias={"% +1.3f"%PBias}\nR\u00b2={"% +1.3f"%R2}', style='italic',
        bbox={'facecolor': 'white', 'alpha': PadTrans, 'pad': Padsize},fontsize=pad_Font)
    plt.legend(('Monthly Simulated','Monthly Observed'),fontsize=Legend_Font, loc=LegendP) 
    fig.savefig(DRR+f'/{Name}_Monthly.png', dpi=DPI)
    plt.close("all")