def OFSM(s, o, Wieght, Method, KGEw1,KGEw2,KGEw3, ty):
    
    import numpy as np
    from hfunction import NSE, R2, MAE, KGE, Pbias, MSE,SE, RE, RMSE
    
    if np.isnan(s).any()==True:
        return(np.nan) 
    else:
        if ty=='GW':
            OBF=Wieght*(KGEw1*NSE(s,o)+KGEw2*R2(s,o)-KGEw3*MSE(s,o))
            return (OBF)
        if ty=='SF':
            #s= [1 / (x+0.01) for x in s]
            #o= [1 / (x+0.01) for x in o]
            #OBF=Wieght*(KGE(s,o,KGEw1,KGEw2,KGEw3))
            OBF=Wieght*(KGEw1*NSE(s,o)+KGEw2*R2(s,o)-KGEw3*MSE(s,o))
            return (OBF)
        if ty=='BF':
            #s= [1 / (x+0.01) for x in s]
            #o= [1 / (x+0.01) for x in o]
            #OBF=Wieght*(KGE(s,o,KGEw1,KGEw2,KGEw3))
            OBF=Wieght*(KGEw1*NSE(s,o)+KGEw2*R2(s,o)-KGEw3*MSE(s,o))
            return (OBF)
