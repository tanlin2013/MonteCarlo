import numpy as np
import sys ; sys.path.append("./src")
from lattice import lattice
import metropolis
import measurement
import matplotlib.pyplot as plt

class Ising:
    def __init__(self,lattice,J1,J2,h):
        self.J1=J1
        self.J2=J2
        self.h=h
        self.BC=lattice.periodic_boundary_condition
        
    def hamiltonian(self,state,site):
        ham=state[site[0]][site[1]]*(-self.J1*(state[self.BC(site[0]+1),site[1]]+state[self.BC(site[0]-1),site[1]])-self.J2*(state[site[0],self.BC(site[1]+1)]+state[site[0],self.BC(site[1]-1)])-self.h)
        return ham

if __name__=='__main__':    
    L=40
    J1=1.0
    J2=J1
    h=0.0
    kb=1.0
    Ts=np.arange(1.0,2.8,0.1)
    Nconf=10000.0

    latt=lattice(2,L,[1,-1])
    model=Ising(latt,J1,J2,h)

    for T in Ts:
        beta=1/(T*kb)
        histogram=metropolis.sampling(latt,model.hamiltonian,beta,Nconf)
        hist_T.append(histogram)

    mlist=[] ; chilist=[] 
    for i in xrange(len(hist_T)):
        mhist=[] ; chihist=[]
        for j in xrange(int(Nconf)):
            MS=measurement.(latt,Is.hamiltonian,hist_T[i][j])
            m,chi=MS.magnetization()
            mhist.append(np.abs(m)) ; chihist.append(chi)
        mlist.append(np.sum(mhist)/Nconf)
        chilist.append(np.sum(chihist)/Nconf)
    
