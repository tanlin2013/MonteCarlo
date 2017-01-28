import numpy as np

class XY:
    def __init__(self):
        self.L=L
        self.J=J
        self.beta=beta
        self.state=state
        self.domain=
        
    def BC(self,site):
        if (site<0):
            site=self.L-1
        elif(site>self.L-1):
            site=0
        return site    
        
    def hamiltonian(self,site):
        ham=-self.J*(np.cos(self.state[site[0]][site[1]]-self.state[self.BC(site[0]+1),site[1]])+np.cos(self.state[site[0]][site[1]]-self.state[self.BC(site[0]-1),site[1]])+np.cos(self.state[site[0]][site[1]]-self.state[site[0],self.BC(site[1]+1)])+np.cos(self.state[site[0]][site[1]]-self.state[site[0],self.BC(site[1]-1)]))
        return ham
    
    def energy(self,return_capacity=False):
        U=0.0 ; U2=0.0
        for site in np.ndindex(self.L,self.L):
            U+=0.5*self.hamiltonian(site)
            if return_capacity: U2+=U**2
        E=U/float(self.L**2)
        if return_capacity:
            Cv=U2/float(self.L**2)-E**2
            return E,Cv
        else:
            return E
        
    def magnetization(self):
        m=np.absolute((np.sum(np.cos(self.state))+np.sum(np.sin(self.state))j)/float(self.L**2))
        m2=1
        chi=m2-m**2
        return m,chi   
      
    def sampling(self,N_flip,maxstep):
        time=0 ; histogram=[]
        while time < maxstep:
            E0=self.energy()
            for trial in xrange(N_flip):
                site=np.random.randint(0,self.L,(2,))
                self.state[site[0]][site[1]]*=
            dE=self.energy()-E0    
            if ((dE>0.0)and(np.random.random()<=np.exp(-self.beta*dE))):
                self.state[site[0]][site[1]]*=-1
            histogram.append(self.state)
            time+=1
        return histogram
    
    def AutoCorrelation(self,histogram,method="integral"):
        mean=np.mean(histogram) ; std=np.std(histogram)
        n=len(histogram) ; k=0 ; gamma=[]
        while k < n:
            G=0
            for t in xrange(n-k):
                G+=(histogram[t]-mean)*(histogram[t+k]-mean)
            gamma.append(G/((n-k)*std))
            k+=1
        if method=="fit":
            tau,b=np.polyfit(np.arange(n-1),np.log(gamma),1)
        elif method=="integral":
            tau=np.sum(gamma)
        else:
            raise Exception("Only fit or integral are allowed")
        return gamma,tau
    
if __name__=='__main__':
    L=40
    J=1.0
    kb=1.0
    Ts=np.arange(1.8,2.5,0.1)
    
    hist_T=[]
    state=np.ones((L,L),dtype=int)
    for T in Ts:
        beta=1/(T*kb)
        montecarlo=Ising(L,J1,J2,h,beta,state)
        histogram=montecarlo.sampling(N_flip=2,maxstep=1e+6)
    hist_T.append(histogram)
      
