import numpy as np

class lattice:
    def __init__(self,dim,L):
        self.dim=dim
        self.L=L
      
    def lattice(self,init):
        if init=="ColdStart":
            return  
        elif init=="HotStart":
            return
        else:
            raise Exception("")
            
    def boundary_condition(self,site):
        if (site<0):
            site=self.L-1
        elif(site>self.L-1):
            site=0
        return site
    
    
