import numpy as np

class lattice:
    def __init__(self,dim,L,domain):
        self.dim=dim
        self.L=L
        self.domain=domain
        
    def initialize_lattice(self,init):
        size=tuple([self.L]*self.dim)
        if init=="ColdStart":
            return self.domain[0]*np.ones(size,dtype=int)  
        elif init=="HotStart":
            return np.random.choice(self.domain,size)
        else:
            raise Exception("Only ColdStart or HotStart are allowed.")
            
    def boundary_condition(self,site):
        if (site<0):
            site=self.L-1
        elif(site>self.L-1):
            site=0
        return site
    
    
