"""
Grover Sample using Lazy Method, this is a sample program to show how to use the Lazy Method to create a Grover's Algorithm circuit.
The MCZ gate is used to create a random oracle, which is then used to create a Grover's Algorithm circuit.
It searches for marked states where the first three qubits are 1. Then it measures the first four qubits. This has potential to be used for a tic tac toe game.

"""
"""
Title: Grover Sample for Lazy Method \n
Author: Auro Varat Patnaik \n
Date: 2023-03-07 \n
Code version: 3.0 \n 
"""

import numpy as np
import sys
sys.path.append("../resources")
sys.path.append("./resources")
from qCircuit import LazyCircuit
from qComponents import reusableComponents as rc
from scipy.sparse import diags
import time

isq2 = 1/np.sqrt(2) # 1/sqrt(2)isq2 = 1/np.sqrt(2) # 1/sqrt(2)


from tqdm import tqdm
from matplotlib import pyplot as plt


#take nqubits as input terminal
import sys
# nqubits = int(sys.argv[1])
nqubits = 10

def main():
    #%%
    #create oracle, marks a state with 1 in the first 6 qubits
    #possible tic tac toe implementation
    qc = LazyCircuit(nqubits,"Random Oracle")
    #checks if the first 3 qubits are 1
    qc.mcz([1,2,3],10)
    

    # qc.mcz([1,2,3],10)
    # qc.mcz([4,5,6],10)
    # qc.mcz([7,8,9],10)
    oracle = qc.to_gate()

  
    gi= rc.grover_iterate(nqubits,oracle)
    
    Q = LazyCircuit(nqubits,"Grover")
  
    Q.h()

    Q.addToCircuit(gi,name="Grover Iterator")

    Q.measure(4)
    Q.output() # returns the probability of each state, prints the state with the highest probability

  
    #%%

    #%%

if __name__ == '__main__':
    
   
    circuit_output = main()
    #append circuit output to a txt file
    # with open("groverLazy.txt", "a") as f:
    #     f.write(str(nqubits)+",")
    #     f.write(','.join(map(str, circuit_output[0])))
    #     f.write(","+str(circuit_output[1])+"\n")
        
   
        
  