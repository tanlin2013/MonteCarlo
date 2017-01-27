import numpy as np
import lattice

class physical:
    def __init__(self,dim,L,config):
        self.dim=dim
        self.L=L
        self.config=config
        
    def magnetization(self):
        m=0
        for state in np.nditer(self.config):
            m+=np.array(state)
        return np.linalg.norm(m)/float(N**dim)
    
    def HeatCapacity(self):
        
        return Cv
    
    def susceptibility(self):
        
        return chi

class statistical:
    def __init__(self,config):
        self.config=config
        
    def AutoCorrelation(self):
        
        return gamma,tau
  
