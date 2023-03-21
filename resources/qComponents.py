import sys
sys.path.append("../resources")
sys.path.append("./resources")
import numpy as np
from qCircuit import LazyCircuit

class reusableComponents():
    
        def __init__(self) : 
            """This class contains reusable components for quantum circuits.
            """
            pass
        @staticmethod
        def grover_iterate(nqbits,oracle):
            """This function creates a Grover Iterator circuit element.

            :param nqbits:  number of qubits in the circuit
            :param oracle:  oracle to be used in the circuit
            
            :return:  a quantum gate representing the Grover Iterator
            """
            qc = LazyCircuit(nqbits,name="Grover Iterator")
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
            """ This function creates an inverse QFT circuit element.

            :param nqbits:  number of qubits in the circuit
            :return:  a quantum gate representing the inverse QFT
            """
            qc = LazyCircuit(nqbits,name="QFTdagger")
            # Don't forget the Swaps!
            for qubit in range(nqbits//2):
            
                qc.swap(qubit+1, (nqbits-qubit-1)+1)
            for j in range(nqbits):
                for m in range(j):
                
                    qc.cp(m+1, j+1,phi=-np.pi/float(2**(j-m)))
        
                qc.h(j+1)
                
     
            return  qc.to_gate()

        
    