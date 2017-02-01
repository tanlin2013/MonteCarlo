import numpy as np
import copy

def sampling(lattice,ham,beta,Nconf,init_state=None,maxstep=1e+5,show_stats=True):
    time=0 ; histogram=[]
    if init_state is None:
        state=lattice.initialize_lattice("ColdStart")
    else:
        state=init_state
    while time < maxstep:       
        site=tuple(np.random.randint(0,lattice.L,(lattice.dim,)))
        flipState=copy.copy(state) ; DM=copy.copy(lattice.domain) ; DM.remove(state[site])
        flipState[site]=np.random.choice(DM,1).item()
        dE=ham(flipState,site)-ham(state,site)
        if not((dE>0.0)and(np.random.random()>=np.exp(-beta*dE))):
            state=flipState        
        if maxstep-time <= Nconf: 
            histogram.append(state)       
        if show_stats and time%(maxstep/100)==0:       
            print "beta=%.3f, sampling stage: %.f%% of maxstep" %(beta,100*(time/float(maxstep)))
        time+=1     
    return histogram
