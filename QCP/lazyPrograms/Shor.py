
"""
Below is the code for Shor's algorithm. 
The code is written in a way that it can be used to find the period of any function.
The function is specified by the user in the c_amod15 function. The function takes in two parameters, a and power. 
The function is defined as follows:
f(x) = a^x mod N


The current implementation only goes as far to plot the counts of the measured states. It uses LazyCircuit to create circuit elements.
Eager Circuit is used for the evaluation of the circuit.
"""
"""
Title: Quantum Circuit for Shor \n
Author: Auro Varat Patnaik \n
Date: 2023-03-07 \n
Code version: 3.0 \n
  
"""

import numpy as np
import sys
sys.path.append("../resources")
sys.path.append("./resources")
from qCircuit import LazyCircuit,EagerCircuit
from qComponents import reusableComponents as rc
from tqdm import tqdm
from matplotlib import pyplot as plt
from scipy.sparse.linalg import expm_multiply,inv


def main():
      
    nqbits = 8
    Uqbits = 4
    
    # ## Create 7mod15 gate
    # N = 15
    # m = int(np.ceil(np.log2(N)))

    # U_qc = LazyCircuit(m)
    # U_qc.x()
    # U_qc.swap(2, 3)
    # U_qc.swap(3, 4)
    # U_qc.swap(1, 4)

    # U = U_qc.to_gate()
   
    
    # def cU_multi(k):
    #     circ = LazyCircuit(m)
    #     for _ in range(2**k):
    #         circ.addToCircuit(U)
        
    #     U_multi = circ.to_gate()
      
    #     cU_multi = circ.addControl(U_multi)
    #     return cU_multi
    
    # def qft(n):
    #     """Creates an n-qubit QFT circuit"""
    #     circuit = LazyCircuit(n)
    #     def swap_registers(circuit, n):
    #         for qubit in range(n//2):
    #             circuit.swap(qubit+1, (n-qubit-1)+1)
    #         return circuit
    #     def qft_rotations(circuit, n):
    #         """Performs qft on the first n qubits in circuit (without swaps)"""
    #         if n == 0:
    #             return circuit
    #         n -= 1
    #         circuit.h()
    #         for qubit in range(n):
            
    #             circuit.cp(qubit+1,n+1,np.pi/2**((n-qubit)+1))
    #         qft_rotations(circuit, n)
        
    #     qft_rotations(circuit, n)
    #     swap_registers(circuit, n)
    #     return circuit.to_gate()
            
            
    # t = 2*m
    # shor_QPE = EagerCircuit(t+m, t)
    # shor_QPE.h()

    # shor_QPE.x(t+1)
    # for idx in range(1,t):
    #     shor_QPE.swap(idx, t, one_directional=True)
    #     shor_QPE.addToCircuit(cU_multi(idx-1), t, name="cU_multi")
    #     shor_QPE.unswap(idx, t)

    # qft_dag = np.linalg.inv(qft(t))


    # shor_QPE.addToCircuit(qft_dag,1 , name="qft_dagger")
    # return shor_QPE.measure(t)
    
        
        
    def c_amod15(a,power):
        if a not in [2,4,7,8,11,13]:
            raise ValueError("'a' must be 2,4,7,8,11 or 13")
        U = LazyCircuit(Uqbits,name="c_amod15")
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
 


    
    #     # Specify variables
    n_count = 8  # number of counting qubits
    a =7
    
    # #using eager circuit to run main loop since its faster for 12 qubits case.

    Q = EagerCircuit(n_count + 4)
    Q.h()
    Q.x(n_count+1)


    for q in range(1,n_count):
        
        Q.swap(q,8,one_directional=True)  
        Q.addToCircuit(c_amod15(a, 2**(q-1)), 8,name="c_amod15")  
        Q.unswap(q,8)
        
  
    Q.addToCircuit(c_amod15(a, 2**7), 8,name="c_amod15")   

    
   
    
    Q.addToCircuit(rc.qft_dagger(n_count),1, name="qft_dagger")



    # Measure circuit
    return Q.measure(8)
 
    # np.savetxt("Shor.txt", np.c_[np.asarray(Q.registerStates),np.asarray(result)],delimiter = ',',fmt="%s")
 



    

    
    

if __name__ == '__main__':

    p = []
    for _ in tqdm(range(100)):
        p.append(main())
    np.savetxt("Shor.txt", p,delimiter = ',',fmt="%s")
    #x label
    plt.xlabel('Measured value')
    #rotate
    plt.xticks(rotation=90)
    #add border to bar
        
    n, bins,_=plt.hist(p)
 
    plt.gca().set_xticks(bins)
    plt.show()
   
    plt.savefig("Shor.png")

  