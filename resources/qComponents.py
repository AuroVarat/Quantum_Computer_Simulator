import sys
sys.path.append("../resources")
sys.path.append("./resources")
import numpy as np
from qCircuit import LazyCircuit

class reusableComponents():
        def __init__(self) : 
            pass
        @staticmethod
        def grover_iterate(nqbits,oracle):
            qc = LazyCircuit(nqbits,"Grover Iterator")
            qc.set_oracle(oracle)
            qc.addToCircuit(oracle)
            qc.h()
            qc.reflect()  
            qc.h()
        
            # We will return the diffuser as a gate
            U_s = qc.to_gate()
            U_s = qc.power(U_s,qc.rotations)
        
            return U_s
        @staticmethod
        def qft_dagger(nqbits):
            """n-qubit QFTdagger the first n qubits in circ"""
            
            qc = LazyCircuit(nqbits,"QFTdagger")
            # Don't forget the Swaps!
            for qubit in range(nqbits//2):
                qc.swap(qubit+1, nqbits)
            for j in range(nqbits):
                for m in range(j):
                
                    qc.cp(int(m+1), int(j+1),phi=-np.pi/float(2**(j-m)))
        
                qc.h(j+1)
                
        
            return  qc.to_gate()

        
    