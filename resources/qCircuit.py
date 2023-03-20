"""
Title: Quantum Circuit Class
Author: Auro Varat Patnaik
Date: 2023-03-07
Code version: 3.0
Description: Quantum Circuit Class initialises a quantum circuit with nqbits qbits and initialises all qbits to |0>.
It has two subclasses LazyCircuit and EagerCircuit.
"""

import numpy as np
from scipy.sparse import identity
import sys
sys.path.append("../resources")
from qRegister import QbitRegister


class LazyCircuit(QbitRegister):
  
    """
    Qbit Register Class initialises a quantum register with nqbits qbits and initialises all qbits to |0>l,
    and contains methods to apply gates to the qbits in the register. 
    """
 
    def __init__(self,nqbits=2,name = "qregister"):
        """Defines a Quantum Register with nqbits qbits and initialises all qbits to |0>.
        The Quantum Register is represented by a vector in the 2^nqbits dimensional basis space, i.e. the Hilbert Spac of the nqbits.

        Args:
            nqbits (int, optional): Number of Qbits in the Quantum Register. Defaults to 2.
            name (str, optional): Label of the register. Defaults to "qregister".
        """

        
        self.circuit = self.create_circuit()
        QbitRegister.__init__(self,nqbits,name)

        
    def create_circuit(self):   
        def circuitElement(register):
            return lambda t_all,measure=False: circuitElement(register @ t_all) if measure != True else  t_all @ register
        return circuitElement
    
  
 

        
    def addToCircuit(self,  gate, ith_qbit=None,name=None):
        """Applies a gate to the ith qbit in the quantum register. If the gate is a 2D gate then it is applied to the ith and (i+1)th qbit.
        Args:
            gate (Numpy Array): Gate to be applied
            ith_qbit (int): ith qbit to be operated on
        """
        if ith_qbit != None:
            self.circuit = self.circuit(self.operation(gate,ith_qbit))
            self.circuitSeq.append((name,ith_qbit+1))
        else:
            self.circuit = self.circuit(gate)
            self.circuitSeq.append((name))
       
        
    def measure(self):
        """Measures the quantum register in the computational basis and returns the result."""
        self.basisSpace = self.circuit(self.basisSpace,measure=True)
        print(str(np.around(self.basisSpace.real))+"\n")
        return self.basisSpace
        
    def to_gate(self):
        """Converts the quantum register to a gate
        """
        return self.circuit(identity(self.N),measure=True)
    
class EagerCircuit(QbitRegister):
  
    """
    Qbit Register Class initialises a quantum register with nqbits qbits and initialises all qbits to |0>l,
    and contains methods to apply gates to the qbits in the register. 
    """
 
    def __init__(self,nqbits=2,name = "BasicQregister"):
        """Defines a Quantum Register with nqbits qbits and initialises all qbits to |0>.
        The Quantum Register is represented by a vector in the 2^nqbits dimensional basis space, i.e. the Hilbert Spac of the nqbits.

        Args:
            nqbits (int, optional): Number of Qbits in the Quantum Register. Defaults to 2.
            name (str, optional): Label of the register. Defaults to "qregister".
        """
        
        
        self.state_history = []
        self.marked_state_history = []
        QbitRegister.__init__(self,nqbits,name)
   
       
 


    
    def addToCircuit(self,gate, ith_qbit=None,name=None):
        """Applies a gate to the ith qbit in the quantum register. If the gate is a 2D gate then it is applied to the ith and (i+1)th qbit.
        Args:
            gate (Numpy Array): Gate to be applied
            ith_qbit (int): ith qbit to be operated on
        """
        if ith_qbit != None:
         
            self.basisSpace = self.operation(ith_qbit,gate) @ self.basisSpace
            self.circuitSeq.append((name,ith_qbit+1))
        else:
        # Apply the gate
   
            self.basisSpace =gate @ self.basisSpace
            self.circuitSeq.append((name))
       
        

    def record_state_vector_projection(self):
        assert self.recording == True, "Oracle not set to record"
        w = self.winnerState
        s = self.basisSpace.real
        
        x = np.dot(s,self.s_prime)
        y = np.dot(s,w)
        
        self.state_history.append([x,y])
    
    def record_marked_state(self,marked_state_index):
        assert self.recording == True, "Oracle not set to record"
        
        self.marked_state_history.append(self.basisSpace.real[marked_state_index])

   
       
       
       
       
       
        
  

   

# %%
