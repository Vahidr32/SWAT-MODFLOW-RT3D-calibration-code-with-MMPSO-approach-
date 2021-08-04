def Get_Directory():
    import os 
    CA_PSO = os.path.dirname(os.path.abspath(__file__))
    DBM=os.path.dirname(CA_PSO)+'/Baseflow'
    DP=os.path.dirname(CA_PSO)+'/Particles'
    DRR=os.path.dirname(CA_PSO)+'/Results'
    DM=os.path.dirname(os.path.dirname(CA_PSO))
    with open(DM+'/SWAT-MODFLOW-PSO/Directory.txt', 'w') as file:
        file.write(f'DM: {DM}\n')
        file.write(f'DP: {DP}\n')
        file.write(f'DRR: {DRR}\n')
        file.write(f'DBM: {DBM}\n')
        
    return(DBM,DP,DRR,DM)