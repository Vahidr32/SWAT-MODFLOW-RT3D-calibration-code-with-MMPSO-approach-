def ObservationName(DM):
    f=open(DM+"/SWAT-MODFLOW-PSO/ObservationName.txt","r")
    lines=f.readlines()
    SON=[]
    BON=[]
    HON=[]
    NON=[]
    
    SOB=[]
    BOB=[]
    HOC=[]
    NOB=[]
    
    SMO=[]
    BMO=[]
    HMO=[]
    NMO=[]
    
    SW=[]
    BW=[]
    HW=[]
    NW=[]
  
    S_KGEW1=[]
    S_KGEW2=[]
    S_KGEW3=[]
    
    B_KGEW1=[]
    B_KGEW2=[]
    B_KGEW3=[]
    
    H_KGEW1=[]
    H_KGEW2=[]
    H_KGEW3=[]
    
    N_KGEW1=[]
    N_KGEW2=[]
    N_KGEW3=[]
    
    SG=[]
    BG=[]
    HG=[]
    NO3G=[]
    for i in range (len(lines)):
        if "NSOS" in lines[i]:
            NSOS=int(lines[i].split()[0])
            for j in range(NSOS):
                SG.append(float(lines[i+j+1].split()[0]))
                SON.append(lines[i+j+1].split()[1])
                SOB.append(int(lines[i+j+1].split()[2]))
                
                SW.append(float(lines[i+j+1].split()[3]))
                SMO.append(lines[i+j+1].split()[4])
                
                if lines[i+j+1].split()[4]=='KGE':
                    S_KGEW1.append(float(lines[i+j+1].split()[5]))
                    S_KGEW2.append(float(lines[i+j+1].split()[6]))
                    S_KGEW3.append(float(lines[i+j+1].split()[7]))
                else:
                    S_KGEW1.append(0)
                    S_KGEW2.append(0)
                    S_KGEW3.append(0)
                    

        if "BSOS" in lines[i]:
            BSOS=int(lines[i].split()[0])
            for j in range(BSOS):
                BG.append(float(lines[i+j+1].split()[0]))
                BON.append(lines[i+j+1].split()[1])
                BOB.append(int(lines[i+j+1].split()[2]))
                
                BW.append(float(lines[i+j+1].split()[3]))
                BMO.append(lines[i+j+1].split()[4])
          
                if lines[i+j+1].split()[4]=='KGE':
                    B_KGEW1.append(float(lines[i+j+1].split()[5]))
                    B_KGEW2.append(float(lines[i+j+1].split()[6]))
                    B_KGEW3.append(float(lines[i+j+1].split()[7]))
                else:
                    B_KGEW1.append(int(0))
                    B_KGEW2.append(0)
                    B_KGEW3.append(0)
                    
                    
        if "NHOS" in lines[i]:
            NHOS=int(lines[i].split()[0])
            for j in range(NHOS):
                HG.append(float(lines[i+j+1].split()[0]))
                HON.append(lines[i+j+1].split()[1])
                HOC.append(int(lines[i+j+1].split()[2]))
                
                HW.append(float(lines[i+j+1].split()[3]))
                HMO.append(lines[i+j+1].split()[4])
                
                if lines[i+j+1].split()[4]=='KGE':
                    H_KGEW1.append(float(lines[i+j+1].split()[5]))
                    H_KGEW2.append(float(lines[i+j+1].split()[6]))
                    H_KGEW3.append(float(lines[i+j+1].split()[7]))
                else:
                    H_KGEW1.append(0)
                    H_KGEW2.append(0)
                    H_KGEW3.append(0)
                    
        if "NSNOS" in lines[i]:
            NSOS=int(lines[i].split()[0])
            for j in range(NSOS):
                NO3G.append(float(lines[i+j+1].split()[0]))
                NON.append(lines[i+j+1].split()[1])
                NOB.append(int(lines[i+j+1].split()[2]))
                
                NW.append(float(lines[i+j+1].split()[3]))
                NMO.append(lines[i+j+1].split()[4])
                
                if lines[i+j+1].split()[4]=='KGE':
                    N_KGEW1.append(float(lines[i+j+1].split()[5]))
                    N_KGEW2.append(float(lines[i+j+1].split()[6]))
                    N_KGEW3.append(float(lines[i+j+1].split()[7]))
                else:
                    N_KGEW1.append(0)
                    N_KGEW2.append(0)
                    N_KGEW3.append(0)
    f.close()
    return(SG, SON,SOB,SW, SMO,S_KGEW1,S_KGEW2,S_KGEW3,BG, BON,BOB,BW, BMO,B_KGEW1,B_KGEW2,B_KGEW3, HG, HON,HOC,HW,HMO, H_KGEW1, H_KGEW2,H_KGEW3, NO3G, NON,NOB, NW, NMO,N_KGEW1,N_KGEW2,N_KGEW3)
