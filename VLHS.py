def VLHS(NV,NS, MaxB, MinB):
    from scipy.stats.distributions import norm
    from pyDOE import lhs
    #NV=Number of variables
    #NS=Number of samples/simulations
    #MaxB=Maximum `upper boundary of the variables  for example MaxM=[1, 2 3]
    #MinB=Minimum Lower boundary of the variabe, for example MinM=[1, 2 3]
    # Latine Hypercube sampling: lhs(n, [samples, criterion, iterations])
    # see this page for more information about lhs: https://pythonhosted.org/pyDOE/randomized.html
    lhd = lhs(NV, samples=NS)
    for j in range(NV):
        for i in range(NS):
            lhd[i-1,j-1]=lhd[i-1,j-1]*(MaxB[j-1]-MinB[j-1])+MinB[j-1]
    return (lhd)