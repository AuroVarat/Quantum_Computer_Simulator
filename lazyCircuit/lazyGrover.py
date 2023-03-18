from lazyRegister import QbitRegister
import numpy as np
import inspect
import cProfile
import time
from scipy.sparse import diags,identity,eye,csr_matrix
from scipy.linalg import hadamard


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
    #oracle
    def grover_iterate(nqubits,n):
        qc = QbitRegister(nqubits)
    
        qc.addToCircuit(oracle)
        qc.hadamard()
        qc.mcz()  # multi-controlled-toffoli
        qc.hadamard()
     
        # We will return the diffuser as a gate
        U_s = qc.to_gate()
        U_s = qc.power(U_s,n)
        # U_s.name = "U$_s$"
        return U_s
    



    
    t1= time.time()
    
    
    Q = QbitRegister(nqubits)
    Q.hadamard()

    Q.addToCircuit(grover_iterate(nqubits,Q.rotations))
   
    Q.measure()
    
    t2 = time.time()

    return t2-t1
    #%%

    # print(np.linalg.norm(register.basisSpace.real))
    # print(register.basisSpace.real[register.basisSpace.real > 0.])
    
    #print("target found" if np.argmax(register.basisSpace.real) == target else "target not found")
    # turn a numy array into a square matrix
    # plt.plot(np.abs(register.basisSpace.real))
    # plt.savefig("result.png")
    #%%

if __name__ == '__main__':
    # print('profiling 2')
    # pr = cProfile.Profile()
    # pr.enable()
   
    main()
  
    # pr.disable()
    # pr.print_stats(sort='time')
  