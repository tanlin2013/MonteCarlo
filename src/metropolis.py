import numpy as np
import copy

def sampling(lattice,ham,beta,Nconf,init_state=None,Nflip=10,maxstep=1e+5,show_stats=True):
    time=0 ; histogram=[]
    if init_state is None:
        state=lattice.initialize_lattice("ColdStart")
    else:
        state=init_state
    while time < maxstep:
        trail=0 ; trailist=[] ; MirrorState=copy.copy(state)
        while trail < Nflip:
            site=tuple(np.random.randint(0,lattice.L,(lattice.dim,)))
            DM=copy.copy(lattice.domain) ; DM.remove(state[site])
            flipState=np.random.choice(DM,1).item()
            if trail > 0 and site in trailist:
                trail-=1
            else:
                MirrorState[site]=flipState                
                trailist.append(site) ; trail+=1
        if Nflip==1:        
            dE=ham(MirrorState,site)-ham(state,site)
        else:
            dE=totalEnergy(lattice,ham,MirrorState)-totalEnergy(lattice,ham,state)
        if not((dE>0.0)and(np.random.random()>=np.exp(-beta*dE))):
            state=MirrorState        
        if maxstep-time <= Nconf: 
            histogram.append(state)       
        if show_stats and time%(maxstep/100)==0:       
            print "beta=%.3f, thermalize stage: %.f%%" %(beta,100*(time/float(maxstep)))
        time+=1     
    return histogram

def totalEnergy(lattice,ham,state):
    E=0.0 ; size=size=tuple([lattice.L]*lattice.dim)
    for site in np.ndindex(size):
        E+=0.5*ham(state,site)
    return E
