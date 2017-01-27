import numpy as np

def metropolis(dE,beta):
    if not((dE>0.0)and(np.random.random()>=np.exp(-self.beta*dE))):
        return True
    else:
        return False

def convergence():
