from lazyCircuit.lazyCircuit import QbitRegister

import numpy as np
import inspect
import cProfile
import time
from scipy.sparse import diags,identity,eye,csr_matrix,kron





def main():
      
    nqbits = 8
    Uqbits = 4
    
    def c_amod15(a,power):
        if a not in [2,4,7,8,11,13]:
            raise ValueError("'a' must be 2,4,7,8,11 or 13")
        U = QbitRegister(Uqbits)
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
    def qft_dagger(n):
        """n-qubit QFTdagger the first n qubits in circ"""
        qc = QbitRegister(n)
        # Don't forget the Swaps!
        for qubit in range(n//2):
            qc.swap(qubit+1, n-qubit)
        for j in range(n):
            for m in range(j):
            
                qc.control_phase_shift(m+1, j+1,phi=-np.pi/float(2**(j-m)))
                
            qc.hadamard(j+1)
      
        return  qc.to_gate()

    
        # Specify variables
    n_count = 8  # number of counting qubits
    a = 7
 

    Q = QbitRegister(n_count + 4)
    Q.hadamard()
    Q.x(n_count+1)


    for q in range(1,8):
        
        Q.swap(q,8)     
        Q.addToCircuit(c_amod15(a, 2**q), 8,name="c_amod15")  
        
        Q.unswap(q,8)
        
    Q.addToCircuit(c_amod15(a, 2**8), 8,name="c_amod15")
      
    g = qft_dagger(n_count).shape
    
    # # Do inverse-QFT
    eyeL = eye(2**1, dtype=np.complex,format='csr')
    eyeR = eye(2**(12 - 0 - 8), 
                dtype = np.complex,format='csr')
    
            # Tensor product of the gate and the identity matrices
            # eyeL ⊗ t ⊗ eyeR
    t_all = kron(kron(eyeL, g), eyeR)
    # print(t_all.shape)
    
    Q.addToCircuit(qft_dagger(n_count),ith_qbit= 1, name="qft_dagger")



    # Measure circuit
    print(Q.measure())




    

    
    

if __name__ == '__main__':
    # pr = cProfile.Profile()
    # pr.enable()

    main()

    # pr.disable()
    # pr.print_stats(sort='time')
  