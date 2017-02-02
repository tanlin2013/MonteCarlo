# MonteCarlo

A simple pythonic implementation of Monte Carlo. This module is used for the study of classical statistical mechanics, and mainly supports to the Ising-like Hamiltonian. For the Hamiltonian defined on the continuous value, as XY model, limited supports are also possible. There are two types of algorithms provided:

* Metropolis
* Wolff cluster (developing) 

## Requirement:
Only Numpy is required and Anaconda is highly recommanded.
* Numpy

## Classes
A list of fundemental class.
* lattice
* metropolis
* wolff_cluster
* measurement

## How to use it?
1. Declaim a lattice. 
    There are 3 variables required for the lattice construction: dim, L and domain. The constructor will generate a np.ndarray with size=L**dim, and full of its value from domain.
    
    ```
    # An example of 2d Ising model with size=10*10.
    
    from lattice import lattice
    mylattice=lattice(dim=2,L=10,domain=[1,-1])
    ```
    to specify how to assign the value explicitly
    ```
    state=mylattice.initialize_lattice(init="HotStart") # or init="ColdStart"
    ```
2. Define the Hamiltonian. 
    It has to be a function with two arguments: state and site. In order to pass the other parameters needed in Hamiltonian. Users may pass them by class objects or by the global variables. 
    ```
    class Ising:
        def __init__(self,lattice,J1,J2,h):
            self.J1=J1
            self.J2=J2
            self.h=h
            self.BC=lattice.periodic_boundary_condition
        
        def hamiltonian(self,state,site):
            ham=state[site]*(-self.J1*(state[self.BC(site[0]+1),site[1]]+state[self.BC(site[0]-1),site[1]])
                -self.J2*(state[site[0],self.BC(site[1]+1)]+state[site[0],self.BC(site[1]-1)])-self.h)
            return ham
    ```
3. Call the sampling method.
    ```
    import metropolis

    beta=1/(T*kb)
    model=Ising(mylattice,J1,J2,h)
    histogram=metropolis.sampling(mylattice,model.hamiltonian,beta,Nconf=100.0)
    ```
