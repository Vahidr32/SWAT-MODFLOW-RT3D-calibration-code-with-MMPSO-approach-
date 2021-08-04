def PVG():
    from Get_Directory import Get_Directory
    from Initialization import Initialization
    import matplotlib.pyplot as plt
    from matplotlib.font_manager import FontProperties
    from matplotlib.ticker import StrMethodFormatter
    from scipy.stats import gaussian_kde
    DBM,DP,DRR,DM=Get_Directory()
    [NSB,NOP,MNIt,NSY,BYS,BJDS,EJDS,NYSKIP,C1I,C1F,C2I,C2F,RC,NG, NOW, NSD, SDate, FDate,NCores,MMPSO, TCir1, TCir2,DPI]=Initialization(DM=DM)
    with open(DRR+'/Particle_BestPosition.txt', 'r') as file:
        lines=file.readlines()
        VN=[]
        for i in range(len(lines[0].split())):
            VN.append(lines[0].split()[i]) 
    with open(DM+'/SWAT-MODFLOW-PSO/Parameter_input.txt') as file:
        lines=file.readlines()
        Max=[]
        Min=[]
        for i in range(1,len(lines)):
            Max.append(float(lines[i].split()[4]))
            Min.append(float(lines[i].split()[6]))       
    import numpy as np
    with open(DRR+'/IO.txt') as file:
        lines=file.readlines()
        Parameter=np.zeros([len(lines),len(VN)])
        Objective=np.zeros([len(lines)])
        for i in range(len(lines)):
            for j in range(NG,NG+len(VN)):
                Parameter[i,j-NG]=float(lines[i].split()[j])
            for o in range(NG):    
                Objective[i]=float(lines[i].split()[o])+Objective[i]  
    alpha=np.nanpercentile(Objective,[0.5, 99.5])[0]
    beta=np.nanpercentile(Objective,[0.5, 99.5])[1]
    for i in range(len(Objective)):
        if Objective[i]< alpha or Objective[i]>Objective[i]:
            Objective[i]=np.nan
    deleting=[]
    for i in range(len(Objective)):
        if np.isnan(Objective[i])==True:
            deleting.append(i)       
    Objective=np.array(list(np.delete(Objective,deleting,0)))
    Parameter=np.array(list(np.delete(Parameter,deleting,0)))
    with open(DM+'/SWAT-MODFLOW-PSO/Dic_Variable.txt','r') as file:
        lines=file.readlines()
        Convert=[]
        for i in range(len(lines)):
            Convert.append(lines[i].split()[2])
        for j in range(len(VN)):
            for i in range(len(lines)):
                if VN[j]==lines[i].split()[0]:
                    VN[j]=lines[i].split()[1]
    font = FontProperties()
    font.set_family('serif')
    font.set_name('Times New Roman')
    font.set_style('normal')
    font.set_size('xx-large')
    #plt.xlabel(fontsize='x-large')
    if len(VN)<10:
        cols = 3
    if len(VN)<20:
        cols = 5
    if len(VN)<50:
        cols = 7
    if len(VN)>50:
        cols=9
    rows = int(len(VN)/cols)
    if rows*cols<len(VN):
        rows=rows+1
    axes=[]
    fig =plt.figure(figsize=(int(5*cols),int(4*cols)))
    from matplotlib.ticker import MaxNLocator
    for j in range(len(VN)):
        axes.append(fig.add_subplot(rows, cols, j+1) )
        subplot_title=(VN[j])
        axes[-1].set_title(subplot_title,fontproperties=font,fontweight='bold') 
        plt.xticks(ticks=None,fontsize='x-large')
        plt.yticks(ticks=None,fontsize='x-large')
        plt.yscale('symlog', linthresh=int(2*cols))
        try:
            plt.xlim(np.nanpercentile(Parameter[:-1,j],[0.5, 99.5])[0], np.nanpercentile(Parameter[:-1,j],[0.5, 99.5])[1])
        except:
               plt.xlim(np.nanmin(Parameter[:-1,j])-abs(np.nanmin(Parameter[:-1,j])), np.nanmax(Parameter[:-1,j])+abs(np.nanmax(Parameter[:-1,j])))
        plt.ylim(np.nanpercentile(Objective[:-1],[2.5, 99.5])[0], np.nanmax(Objective[:-1]))
        plt.gca().xaxis.set_major_locator(MaxNLocator('4'))
        plt.gca().xaxis.set_major_locator(MaxNLocator('3'))
        plt.gca().xaxis.set_major_formatter(StrMethodFormatter('{x:1.1f}'))
        plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:1.0f}'))
        #xy = np.vstack([Parameter[:-1,j],Objective[:-1]])
        #z = gaussian_kde(xy)(xy)
        #plt.scatter(Parameter[:-1,j],Objective[:-1], c=z, s=50)
        plt.plot(Parameter[:-1,j],Objective[:-1], '.r')
    fig.savefig(DRR+'/ParticleGoal.png', dpi=150)    


