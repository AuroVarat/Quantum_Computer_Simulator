import sys
sys.path.append("../resources")
sys.path.append("./resources")
import numpy as np
from qCircuit import LazyCircuit

class ReusableComponents():
    
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

        @staticmethod
        def qft(nqbits):
            
            """Creates an n-qubit QFT circuit"""
            circuit = LazyCircuit(nqbits)
            def swap_registers(circuit, n):
                for qubit in range(n//2):
                    circuit.swap(qubit+1, (n-qubit-1)+1)
                return circuit
            def qft_rotations(circuit, n):
                """Performs qft on the first n qubits in circuit (without swaps)"""
                if n == 0:
                    return circuit
                n -= 1
                circuit.h()
                for qubit in range(n):
                
                    circuit.cp(qubit+1,n+1,np.pi/2**((n-qubit)+1))
                qft_rotations(circuit, n)
            
            qft_rotations(circuit, nqbits)
            swap_registers(circuit, nqbits)
            return circuit.to_gate()
    