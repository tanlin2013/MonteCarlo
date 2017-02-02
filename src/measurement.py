import numpy as np

class physical:
    def __init__(self,lattice,ham,state,kb):
        self.L=lattice.L
        self.dim=lattice.dim
        self.ham=ham
        self.state=state
        self.kb=kb
    
    def energy(self,beta):
        U=0.0 ; U2=0.0 ; size=tuple([self.L]*self.dim)
        for site in np.ndindex(size):
            U+=0.5*self.ham(self.state,site)
            U2+=U**2
        E=U/float(self.L**self.dim) ; E2=U2/float(self.L**self.dim)
        Cv=self.kb*beta**2*(E2-E**2)
        return E,Cv
    
    def magnetization(self,beta):
        m=np.sum(self.state)/float(self.L**self.dim)
        m2=np.sum(np.square(self.state))/float(self.L**self.dim)
        chi=beta*(m2-m**2)
        return m,chi  

def AutoCorrelation(histogram,method="integral"):
    n=len(histogram) ; mean=np.mean(histogram) ; var=np.var(histogram)  
    gamma=np.correlate(histogram-mean,histogram-mean,mode='full')[-n:]
    gamma/=(var*(np.arange(n,0,-1)))
    if method=="fit":
        tau,b=np.polyfit(np.arange(n-1),np.log(gamma),1)
    elif method=="integral":
        tau=np.sum(gamma)
    else:
        raise Exception("Only fit or integral are allowed")
    return gamma,tau
