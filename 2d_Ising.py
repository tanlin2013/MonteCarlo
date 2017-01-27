import numpy as np
import matplotlib.pyplot as plt

class Ising:
    def __init__(self,L,J1,J2,h):
        self.L=L
        self.J1=J1
        self.J2=J2
        self.h=h
        self.state=state
        
    def BC(self,site):
        if (site<0):
            site=self.L-1
        elif(site>self.L-1):
            site=0
        return site
    
    def hamiltonian(self,site):
        ham=self.state[site[0]][site[1]]*(-self.J1*(self.state[self.BC(site[0]+1),site[1]]+self.state[self.BC(site[0]-1),site[1]])-self.J2*(self.state[site[0],self.BC(site[1]+1)]+self.state[site[0],self.BC(site[1]-1)])-self.h)
        return ham
      
    def energy(self):
        U=0.0 ; U2=0.0
        for site in np.ndindex(self.L,self.L):
            U+=0.5*self.ham(site)
            U2+=U**2
        E=U/float(self.L**2) ; E2=U2/float(self.L**2)
        Cv=E2-E**2
        return E,Cv
    
    def magnetization(self):
        m=np.abs(np.sum(self.state)/float(self.L**2))
        m2=np.sum(np.square(self.state))/float(self.L**2)
        chi=m2-m**2
        return m,chi   
      
    def sampling(self,N_flip,maxstep=1e+6):
        time=0; histogram=[]
        while time < self.maxstep:
            for site xrange(self.N_flip):                
                
        return histogram

    
    
if __name__=='__main__':
    L=40
    
