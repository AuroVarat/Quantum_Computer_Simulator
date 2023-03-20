
import numpy as np
import sys
sys.path.append("../resources")
sys.path.append("./resources")
from qCircuit import LazyCircuit
from scipy.sparse import diags
import time


isq2 = 1/np.sqrt(2) # 1/sqrt(2)isq2 = 1/np.sqrt(2) # 1/sqrt(2)


from tqdm import tqdm
from matplotlib import pyplot as plt


#take nqubits as input terminal
import sys
nqubits = int(sys.argv[1])


max_dataset_size = 2**nqubits
dataset_size = 2**nqubits
assert dataset_size <= max_dataset_size, "dataset size must be less than or equal to 2**nqbits"
def main():
    #%%
    dataset = np.arange(0,dataset_size)
    target = np.random.randint(0,dataset_size)
    oracle = diags(np.where(dataset == target, -1, 1))
 
    
 
    def grover_iterate(nqubits,oracle):
        qc = LazyCircuit(nqubits,"Grover Diffuser Gate")
        qc.set_oracle(oracle)
        qc.addToCircuit(oracle)
        qc.h()
        qc.reflect()  
        qc.h()
     
        # We will return the diffuser as a gate
        U_s = qc.to_gate()
        U_s = qc.power(U_s,qc.rotations)
       
        return U_s,qc.rotations
    
  
    
    Q = LazyCircuit(nqubits,"Grover")
    
    Q.h()
    gi,number_of_rotations = grover_iterate(nqubits,oracle)
    
    Q.addToCircuit(gi,name="Grover Diffuser")
    # Q.sequence()
    return Q.measure(),number_of_rotations

    # t2 = time.time()

    # tt = t2-t1

    # #append to a txt file nqbit and time tt to a txt file
    # with open("groverLazy.txt", "a") as f:
    #     f.write("{},{},{}\n".format(nqubits,tt,accuracy))
  
    #%%

    #%%

if __name__ == '__main__':
    
   
    circuit_output = main()
    #append circuit output to a txt file
    with open("groverLazy.txt", "a") as f:
        f.write(str(nqubits)+",")
        f.write(','.join(map(str, circuit_output[0])))
        f.write(","+str(circuit_output[1])+"\n")
        
   
        
  