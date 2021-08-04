def OBJNO3(OBS,SIMCON,NSD, KGEw1,KGEw2,KGEw3):
    from hfunction import NSE, R2, MAE, KGE, Pbias,MSE
    
    import numpy as np
    if np.isnan(SIMCON).any()==True:
        return(np.nan)
    else:
        C=0
        B=[]
        D=[]
        import numpy as np
        for i in range (NSD):
            if i in OBS[0][0:NSD]:
                D.append(SIMCON[i])
                B.append(OBS[1][C])
                C=C+1
        x_values=np.zeros([len(B)])
        y_values=np.zeros([len(B)])

        for i in range(len(B)):
            x_values[i] = D[i]
            y_values[i] = B[i]

        #KGE=KGE(x_values,y_values,KGEw1,KGEw2,KGEw3)
        OBF=0*(R2(x_values,y_values))
        return(OBF)