"""Unsorted Dictionary Search using Quantum Grover

The file shows a possible application of Grover's Algorithm to a simple problem. 
This was inspired to possibly set up a Circuit that can play wordle.

Both Eager and Lazy methods are used to create separate circuits.

Problem : Search for a 5 letter word in a dictionary of 8192 words( actually close to 5K words but we added more empty words to simplify to the whole number of qubits).
"""
"""
Title: Quantum Circuit for Shor \n
Author: Auro Varat Patnaik \n
Date: 2023-03-07 \n
Code version: 3.0 \n
  
"""

import sys
sys.path.append("../resources")
sys.path.append("./resources")
import numpy as np
from qCircuit import LazyCircuit,EagerCircuit
from qComponents import reusableComponents as rc
from scipy.sparse import diags

nqbits = 13
#import dataset/ dictionary
# This oracle is created without a gate, 
# to see examples of Oracle creation with gates, 
# see the sample files inside LazyPrograms folder and EagerPrograms
dictionary = np.loadtxt("dataset/dictionary.txt",dtype=str)
search_word = "hello"
oracle = diags(np.where(dictionary == search_word,-1,1))


#Eager Circuit
Eager_Searcher = EagerCircuit(nqbits,name="Grover")
Eager_Searcher.h()
Eager_Searcher.set_oracle(oracle)
#Eager_Searcher.addToCircuit(gi) can also be used to avoid the for loop
for _ in range(Eager_Searcher.rotations):
    
    Eager_Searcher.oracle()
    Eager_Searcher.h()
    Eager_Searcher.reflect()  
    Eager_Searcher.h()

Eager_Searcher.measure()



gi = rc.grover_iterate(nqbits,oracle)
Lazy_Searcher = LazyCircuit(nqbits,"Grover")
Lazy_Searcher.h()
Lazy_Searcher.addToCircuit(gi,name="Grover Iteration")
Lazy_Searcher.sequence()
Lazy_Searcher.measure()





