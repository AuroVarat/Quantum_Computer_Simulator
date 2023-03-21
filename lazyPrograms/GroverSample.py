
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


max_dataset_size = 2**nqubits
dataset_size = 2**nqubits
assert dataset_size <= max_dataset_size, "dataset size must be less than or equal to 2**nqbits"
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

    Q.measure()

  
    #%%

    #%%

if __name__ == '__main__':
    
   
    circuit_output = main()
    #append circuit output to a txt file
    # with open("groverLazy.txt", "a") as f:
    #     f.write(str(nqubits)+",")
    #     f.write(','.join(map(str, circuit_output[0])))
    #     f.write(","+str(circuit_output[1])+"\n")
        
   
        
  