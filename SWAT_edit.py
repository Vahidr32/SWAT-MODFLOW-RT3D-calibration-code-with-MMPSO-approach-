def SWAT_edit(DP, SVN, SWAT_parameter, Max, Min):
    from SWAT_myEdit import SWAT_myEdit
    import re
    txt = "{:2.6f}"
    f = open(DP+"/model.in", "w")
    for i in range(len(SVN)):
        f.write(SVN[i]+'      '+txt.format((float(SWAT_parameter[i])))+ "\n")
    f.close() 
    ff=open(DP+'/model.in', 'r')
    lines=ff.readlines()
    for i in range(len(lines)):
        sentence=lines[i]
        sentence = re.sub(r"\s+|__|,", " ", sentence, flags=re.UNICODE)
        q=sentence.split(' ')
        SWAT_myEdit(DP=DP, DG=q[0], V=q[1].split('.')[0], VS=q[1].split('.')[1], VF=q[4:-2], VV=float(q[-2]))
    ff.close()
    f.close()