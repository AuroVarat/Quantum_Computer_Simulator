"""
Qbit Register Class initialises a quantum register with nqbits qbits and initialises all qbits to |0>. 
It contains method for qbits in the register.
"""
"""
Title: Qbit Register Class
Author: Auro Varat Patnaik
Date: 2023-03-07
Code version: 3.0

"""

import numpy as np
from qGates import QbitGate
import sys
sys.path.append("../resources")
sys.path.append("./resources")
from qVisualiser import qVisualiser
from qPreloader import gateMatrices

class QbitRegister(QbitGate,qVisualiser):
  
    """
    Qbit Register Class initialises a quantum register with nqbits qbits and initialises all qbits to |0>l,
    and contains methods to apply gates to the qbits in the register. 
    """
 
    def __init__(self,nqbits=2,name = "register"):
        """Defines a Quantum Register with nqbits qbits and initialises all qbits to |0>.
        The Quantum Register is represented by a vector in the 2^nqbits dimensional basis space, i.e. the Hilbert Spac of the nqbits.

        Args:
            nqbits (int, optional): Number of Qbits in the Quantum Register. Defaults to 2.
            name (str, optional): Label of the register. Defaults to "qregister".
        """
       
        
        self.name = name
        self.nqbits = nqbits
        self.N = 2**self.nqbits
        self.M = 1
        self.basisSpace = np.zeros(self.N, dtype=int) #  basis state formed by tensor product of all qbits
        self.basisSpace[0] = 1 #all qbits are by default initialised to |0>
        self.circuitSeq = []
        QbitGate.__init__(self)
        
       
       

    def output(self):
        print(str(np.around(self.basisSpace.real))+"\n")
        return self.basisSpace
           
    def __str__(self):
        """Prints the quantum register in the basis space
        """

        return "Register in the {} dimension basis space.\n".format(self.nqbits)

    def set_state(self,state):
        self.basisSpace = state
    
    def sequence(self):
        """Prints the circuit sequence of the quantum register
        """
        print("Circuit Sequence: {}".format(self.circuitSeq))
      
   