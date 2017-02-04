import numpy as np

def save(path,histo):
    np.savez(path,*histo)
    return None
    
def read(path):
    npzfile=np.load(path)
    histo=[npzfile[i] for i in npzfile]
    histo.reverse() ; npzfile.close()
    return histo
