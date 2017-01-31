import numpy as np

def sampling(lattice,ham,beta,init_state=None,Nflip=2,maxstep=1e+5,show_stats=True):
    time=0 ; histogram=[]
    if init_state is None:
        state=lattice.initialize_state("HotStart")
    while time < maxstep:
        trail=0 ; trailist=[]
        while trial < Nflip:
            site=np.random.randint(0,lattice.L,(lattice.dim,))
            if trail > 0 and site is in trailist:
                trail-=1
            else:    
                state[site]=flip(state,site,lattice.domain)
                trail+=1
        dE=   
        if ((dE>0.0)and(np.random.random()<=np.exp(-self.beta*dE))):
            for site in trailist:
                state[site]=flip(state,site,lattice.domain)
        histogram.append(state) ; time+=1
        if show_stats and time%(maxstep/100)==0:
            print "beta=%.3f, thermalize stage: %.f%%" %(beta,100*(time/float(maxstep)))
    return histogram

def flip(state,site,domain):
    
    return state
