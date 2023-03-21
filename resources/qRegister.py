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
       
        
        self.RegisterName = name
        self.nqbits = nqbits
        self.N = 2**self.nqbits
        self.M = 1
        self.basisSpace = np.zeros(self.N, dtype=int) #  basis state formed by tensor product of all qbits
        self.basisSpace[0] = 1 #all qbits are by default initialised to |0>
        self.circuitSeq = []
        self.registerStates=[format(i, f'0{self.nqbits}b') for i in range(self.N)]
        QbitGate.__init__(self)
        
       
       

           
    def __str__(self):
        """Prints the quantum register in the basis space
        """

        return "Register in the {} dimension basis space.\n".format(self.nqbits)

    def set_state(self,state):
        """
        Sets the state of the quantum register to the state specified by the input state.

        
        :param:    state (int/list): can be a int showing the qubit state("110") or list of qubit states([ [1,0],[0,1],[0.5,0.5]]). The list supports float values. 
        """
        if type(state) == str:
            try:
                index = np.where(np.asarray(self.registerStates) == str(state))[0][0]
            except:
                print("Invalid state. Please enter a valid state.")
                return
          
        
            
            basis = np.zeros(self.N, dtype=int)
            basis[index] = 1
            self.basisSpace = basis
        elif type(state) == list:
            basis = state[0]
            for i in range(len(state)):
                basis = state[i]@basis
            self.basisSpace = basis
            
                
        else:
            print("Invalid state. Please enter a valid state.")
            return
    def sequence(self):
        """Prints the circuit sequence of the quantum register
        """
        print("Circuit Sequence: {}".format(self.circuitSeq))
      
   