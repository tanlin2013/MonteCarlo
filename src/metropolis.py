import numpy as np
import copy

def sampling(lattice,ham,beta,init_state=None,Nflip=2,maxstep=1e+5,show_stats=True):
    time=0 ; histogram=[]
    if init_state is None:
        state=lattice.initialize_state("HotStart")
    while time < maxstep:
        dE=0.0 ; trail=0 ; trailist=[]
        while trial < Nflip:
            site=np.random.randint(0,lattice.L,(lattice.dim,))
            DM=copy.copy(lattice.domain)
            flipState=np.random.choice(DM.remove(state[site]),1).item()
            if trail > 0 and site is in trailist:
                trail-=1
            else:
                dE+=ham(flipState,site)-ham(state,site)    
                trailist.append((site,flipState)) ; trail+=1
        if not((dE>0.0)and(np.random.random()>=np.exp(-beta*dE))):
            for site,flipState in trailist:
                state[site]=flipState
        histogram.append(state) ; time+=1
        if show_stats and time%(maxstep/100)==0:
            print "beta=%.3f, thermalize stage: %.f%%" %(beta,100*(time/float(maxstep)))
    return histogram
