

import numpy as np

from scipy.sparse import eye,kron
import sys
sys.path.append("../resources")
sys.path.append("./resources")
from qCircuit import LazyCircuit
from components import reusableComponents as rc



def main():
      
    nqbits = 8
    Uqbits = 4
    
    def c_amod15(a,power):
        if a not in [2,4,7,8,11,13]:
            raise ValueError("'a' must be 2,4,7,8,11 or 13")
        U = LazyCircuit(Uqbits)
        for _ in range(power):
            if a in [2,13]:
                U.swap(3,4)
                U.swap(2,3)
                U.swap(1,2)
            if a in [7,8]:
                U.swap(1,2)
                U.swap(2,3)
                U.swap(3,4)
            if a in [4, 11]:
                U.swap(2,4)
                U.swap(1,3)
            if a in [7,11,13]:
                U.x()
        Us = U.to_gate()
        cU = U.addControl(Us)
        return cU
 


    
        # Specify variables
    n_count = 8  # number of counting qubits
    a = 7
 

    Q = LazyCircuit(n_count + 4)
    Q.hadamard()
    Q.x(n_count+1)


    for q in range(1,8):
        
        Q.swap(q,8)     
        Q.addToCircuit(c_amod15(a, 2**q), 8,name="c_amod15")  
        
        Q.unswap(q,8)
        
    Q.addToCircuit(c_amod15(a, 2**8), 8,name="c_amod15")
      
    g = rc.qft_dagger(n_count).shape
    
    # # Do inverse-QFT
    eyeL = eye(2**1, dtype=np.complex,format='csr')
    eyeR = eye(2**(12 - 0 - 8), 
                dtype = np.complex,format='csr')
    
            # Tensor product of the gate and the identity matrices
            # eyeL ⊗ t ⊗ eyeR
    t_all = kron(kron(eyeL, g), eyeR)
    # print(t_all.shape)
    
    Q.addToCircuit(rc.qft_dagger(n_count),ith_qbit= 1, name="qft_dagger")



    # Measure circuit
    print(Q.measure())




    

    
    

if __name__ == '__main__':
    # pr = cProfile.Profile()
    # pr.enable()

    main()

    # pr.disable()
    # pr.print_stats(sort='time')
  