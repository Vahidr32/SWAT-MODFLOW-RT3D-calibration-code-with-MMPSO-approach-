def Pval(DP, Parameter, VN):
    from MNAME import MNAME
    MNAME=MNAME()
    with open(DP+f"/{MNAME}.pval", "r") as datafile:
        VN2=(datafile.read().split()[11::2])
        
    f=open(DP+f"/{MNAME}.pval", "w")
    f.write("# PVAL file created on 09/25/2020 by ModelMuse version 4.3.0.0.""\n")
    f.write(f"{len(VN2)}"+"\n")
    txt = "{:2.4E}"
    for i in range(len(VN2)):
        if "EVT_NJ" in VN2[i] or "SS" in VN2[i] or "SY" in VN2[i] or "SS2_" in VN2[i] or "SY2_" in VN2[i] or "SS3_" in VN2[i] or "SY3_" in VN2[i] or "HK" in VN2[i] or "VK" in VN2[i] or "HK2_" in VN2[i] or "VK2_" in VN2[i] or "HK3_" in VN2[i] or "VK3_" in VN2[i]:
            f.write(VN2[i]+" "+txt.format((float(10**Parameter[VN.index(VN2[i])])))+ "\n")
        else:
            f.write(VN2[i]+" "+txt.format((float(Parameter[VN.index(VN2[i])])))+ "\n")
        
    f.close()