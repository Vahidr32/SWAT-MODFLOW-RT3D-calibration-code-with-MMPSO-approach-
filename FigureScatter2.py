def FigureScatter2(Sim, ObsNO3,ObsStream, Dir, Name, NSD):
    from hfunction import NSE, R2, MAE, KGE, Pbias
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.font_manager import FontProperties
    font = FontProperties()
    font.set_family('serif')
    font.set_name('Times New Roman')
    font.set_style('normal')
    font.set_size('large')
    
    fig=plt.figure(figsize=(10,7))
    plt.xlabel('Observed NO3 (kg/day)', fontsize='large',fontproperties=font)
    plt.ylabel('Simulated NO3 (kg/day)', fontsize='large',fontproperties=font)
    plt.title('Goondi NO3 loads',fontsize='large',fontproperties=font)
    
    plt.grid(True)
    C=0
    B=[]
    D=[]
    E=[]
    F=[]
    for i in range (NSD):
        if i in ObsNO3[0][0:NSD]:
            D.append(Sim[i])
            B.append(ObsNO3[1][C])
            E.append(ObsStream[i])
            F.append(E[C]*B[C]*3600*24/1000)
            plt.scatter(F[C], D[C], alpha=1,color='black' )
            C=C+1
        
    ax = fig.gca()
    ax.plot()
    dd=1.2*max(max(D[:-1]),max(F[:-1]))
    dd2=1.2*min(min(D[:-1]),min(F[:-1]))
    ax.set_xlim([0, dd])
    ax.set_ylim([0, dd]) 
    
    xx=[0, dd]
    yy=[0, dd]
   
    plt.plot(xx, yy, 'black')
    x_values=np.zeros([len(B)])
    y_values=np.zeros([len(B)])
    for i in range(len(B)):
        x_values[i] = D[i]
        y_values[i] = F[i]

    plt.xscale('symlog', linthresh=np.round(np.log(max(abs(y_values)))))
    plt.yscale('symlog', linthresh=np.round(np.log(max(abs(y_values)))))
    NSE=NSE(x_values,y_values)
    R2=R2(x_values,y_values)
    Pbias=Pbias(x_values,y_values)

    plt.text(dd2, 0.2*dd, f'R\u00b2={"% +1.3f"%R2}\nNSE={"% +1.3f"%NSE}\nPbias={"% +1.3f"%Pbias}',bbox={'facecolor': 'white', 'alpha': 1, 'pad': 15},fontproperties=font) 
    
    fig.savefig(Dir, dpi=150)
    plt.close("all")
