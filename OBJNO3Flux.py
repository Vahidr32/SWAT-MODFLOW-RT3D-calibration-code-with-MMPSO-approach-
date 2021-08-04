def OBJNO3Flux(ObsStream,ObsCon,SimFlux,NSD,KGEw1,KGEw2,KGEw3):
    from hfunction import NSE, R2, MAE, KGE, Pbias, MSE,SE,RMSE
    import numpy as np
    if np.isnan(SimFlux).any()==True:
        return(np.nan)
    else:
        C=0
        B,D,F,E=[],[],[],[]
        for i in range (NSD):
            if i in ObsCon[0][0:NSD]:
                D.append(SimFlux[i])
                B.append(ObsCon[1][C])
                E.append(ObsStream[i])
                F.append(B[C]*E[C]*0.001*86400)
                C=C+1
        
        x_values=np.zeros([len(B)])
        y_values=np.zeros([len(B)])
        for i in range(len(B)):
                x_values[i] = D[i]/1000
                y_values[i] = F[i]/1000
        #KGE=KGE(x_values,y_values,KGEw1,KGEw2,KGEw3)
        #OBF=(R2(x_values,y_values)-KGEw3*MSE(x_values,y_values))
        OBF=(KGEw1*NSE(x_values,y_values)+KGEw2*R2(x_values,y_values)-abs(KGEw3*Pbias(x_values,y_values)))
        
       # if OBF<-10^8:
        #    return(np.nan)
        #else:
        return(OBF)