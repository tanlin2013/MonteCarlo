# MonteCarlo

A simple pythonic implementation of Monte Carlo. This module is used for the study of classical statistical mechanics, and mainly supports to the Ising-like Hamiltonian. For the Hamiltonian defined on the continuous value, as XY model, limited supports are also possible. There are two types of algorithms provided:

* Metropolis
* Wolff cluster (developing) 

# Requirement:
Only Numpy is required and Anaconda is highly recommanded.
* Numpy

# Classes
A list of fundemental class.
* lattice
* metropolis
* wolff_cluster
* measurement

# How to use it?
1. Declaim a lattice. There are 3 variables required for the lattice construction: dim, L and domain. The constructor will generate a np.ndarray with size L**dim, and full of the value from domain.
```
""" An example of 2d Ising model. """
from lattice import lattice

mylattice=lattice(dim=2,L=10,domain=[1,-1])
```
