import numpy as np
import sys ; sys.path.append("./src")
from lattice import lattice
import metropolis
import measurement
import matplotlib.pyplot as plt

class XY:
    def __init__(self,lattice,J):
        self.J=J
        self.BC=lattice.periodic_boundary_condition
        
    def hamiltonian(self,state,site):
        ham=-self.J*(np.cos(state[site]-state[self.BC(site[0]+1),site[1]])+np.cos(state[site]-state[self.BC(site[0]-1),site[1]])+np.cos(state[site]-state[site[0],self.BC(site[1]+1)])+np.cos(state[site]-state[site[0],self.BC(site[1]-1)]))
        return ham
    
    def magnetization(self,state,beta):
        m=np.absolute((np.sum(np.cos(state))+np.sum(np.sin(state))*j)/float(self.L**2))
        m2=1
        chi=beta*(m2-m**2)
        return m,chi   
    
if __name__=='__main__':
    
    L=40
    J=1.0
    kb=1.0
    Ts=np.arange(1.8,2.5,0.1)    
    Nconf=10000.0

    domain=(np.arange(16)/(2*np.pi)).tolist()
    latt=lattice(2,L,domain)
    model=XY(latt,J)

    hist_T=[]
    for T in Ts:
        beta=1/(T*kb)
        histogram=metropolis.sampling(latt,model.hamiltonian,beta,Nconf) 
        hist_T.append(histogram)
    
    mlist=[] ; chilist=[] 
    for i in xrange(len(hist_T)):
        mhist=[] ; chihist=[] ; beta=1/(Ts[i]*kb)
        for j in xrange(int(Nconf)):
            #MS=measurement.physical(latt,Is.hamiltonian,hist_T[i][j])
            #m,chi=MS.magnetization()
            m,chi=model.magnetization(hist_T[i][j],beta)
            mhist.append(np.abs(m)) ; chihist.append(chi)
        mlist.append(np.sum(mhist)/Nconf)
        chilist.append(np.sum(chihist)/Nconf)
      
