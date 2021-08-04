def Baseflow(Sim, SDate, NSD):
    import datetime
    import os 
    import subprocess
    import numpy as np
    from DirSM import DirSM
    import stat
    if np.isnan(sum(Sim))==True:
        g=np.NaN*np.empty([NSD])
        return(np.array(g))
    else:
        DM, DBM, DPP, DRR=DirSM()
        os.chmod(DBM+'/bflow', stat.S_IRWXU+ stat.S_IRWXO+stat.S_IRWXG)
        txt = "{:1.3E}"
        date = datetime.date(SDate.year,SDate.month,SDate.day)
        with open(DBM+'/08095300.prn', "w") as file:
            file.write('Date    Flow\n')
            for j in range(NSD):
                file.write(str(date).replace("-","")+'    '+txt.format(Sim[j])+'\n')
                date += datetime.timedelta(days=1)  
        os.chdir(DBM)
        subprocess.run(DBM+'/bflow', shell=False, capture_output=False)
        C=0
        while os.path.isfile(DBM+'/08095300.out') is False:
            C=C+1
            if C>300:
                break
            with open(DBM+'/file.lst',"r") as file: 
                lines=file.readlines()
                a=np.random.randint(1, 450)
                b=a+50
                lines[1]=f'   {a}  !NDMIN: minimum number of days for alpha calculation\n'
                lines[2]=f'   {b}  !NDMAX: maximum number of days for alpha calculation\n'
            with open(DBM+'/file.lst',"w") as file:  
                for i in range(len(lines)):
                    file.write(lines[i])
            subprocess.run(DBM+'/bflow.exe', shell=False, capture_output=False)
        else:
            with open(DBM+'/08095300.out',"r") as file: 
                lines=file.readlines()
                a,b,c,d,e,f,g=[],[],[],[],[],[],[]
                for i in range(len(lines)):
                    if i>1:
                        a.append(lines[i][0:4])
                        b.append(lines[i][4:6])
                        c.append(lines[i][6:9])
                        d.append(float(lines[i][9:21]))
                        e.append(float(lines[i][22:34]))
                        f.append(float(lines[i][35:47]))
                        g.append(float(lines[i][48:60]))    
            os.path.isfile(DBM+'/08095300.out')
            os.remove(DBM+'/08095300.out')
            if len(g)>NSD and sum(f)!=0:
                return(np.array(f[:NSD]))
            else:
                f=np.NaN*np.empty([NSD])
                return(f)