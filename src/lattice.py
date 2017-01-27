import numpy as np

class lattice:
    def __init__(self,dim,L):
        self.dim=dim
        self.L=L
        
    def initialize_lattice(self,init):
        size=tuple([L]*dim)
        if init=="ColdStart":
            return np.ones(size,dtype=int)  
        elif init=="HotStart":
            return np.array((np.random.randint(0,2,size)-0.5)*2,dtype=int) 
        else:
            raise Exception("")
            
    def boundary_condition(self,site):
        if (site<0):
            site=self.L-1
        elif(site>self.L-1):
            site=0
        return site
    
    
