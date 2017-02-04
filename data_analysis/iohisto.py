import numpy as np

def save(path,histo):
    np.savez(path,*histo)
    return None
    
def read(path):
    npzfile=np.load(path)
    histo=[npzfile[i] for i in npzfile]
    npzfile.close() ; histo.reverse()
    return histo
