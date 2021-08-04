def RNO(D,OSNF,SDate,NSD):
    #here we read the stream nitrate observation
    import numpy as np
    #D=Directory of the folder
    with open(D+OSNF, "r") as datafile:
        ObservedNO3=(datafile.read().split()[1::2])
    with open(D+OSNF, "r") as datafile:
        dateNO3=(datafile.read().split()[0::2])
    from datetime import datetime
    D=[]
    OBS=[]
    for i in range(len(dateNO3)):
        ObservedNO3[i]=float(ObservedNO3[i])
        OBSdate=  datetime.strptime(dateNO3[i],'%m/%d/%Y')-SDate
        if int(OBSdate.days+1)<NSD:
            D.append(OBSdate.days+1)
            OBS.append(ObservedNO3[i])

    return(D,OBS)
