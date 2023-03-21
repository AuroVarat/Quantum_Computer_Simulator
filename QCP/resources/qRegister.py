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
from qPreloader import GateMatrices

class QbitRegister(QbitGate,qVisualiser):
  
    """
    Qbit Register Class initialises a quantum register with nqbits qbits and initialises all qbits to |0>l,
    and contains methods to apply gates to the qbits in the register. 
    """
 
    def __init__(self,nqbits,cqbits=None,name = "register"):
        """Defines a Quantum Register with nqbits qbits and initialises all qbits to |0>.
        The Quantum Register is represented by a vector in the 2^nqbits dimensional basis space, i.e. the Hilbert Spac of the nqbits.

        
        :param nqbits (int, optional): Number of Qbits in the Quantum Register. Required.
        :param cqbits (int, optional): Number of classical bits in the Quantum Register. Defaults to the same number of Qbits.
        :param name (str, optional): Label of the register. Defaults to "qregister".
        
        
        :ivar RegisterName (str): Label of the register.
        :ivar nqbits (int): Number of Qbits in the Quantum Register.
        :ivar cqbits (int): Number of classical bits in the Quantum Register.
        :ivar N (int): Dimension of the Hilbert Space of the Quantum Register.
        :ivar M (int): Number of the targets for Grover. Defaults to 1.
        :ivar basisSpace (numpy.ndarray): Vector in the Hilbert Space of the Quantum Register.
        :ivar circuitSeq (list): List of gates applied to the Quantum Register.
        :ivar registerStates (list): List of all possible states of the Quantum Register.
        :ivar state_history (list): List of all states of the Quantum Register at each step of the circuit
        
   
        """
       
        
        self.RegisterName = name
        self.nqbits = nqbits
        if cqbits != None:
            self.cqbits = np.empty(cqbits,dtype=int)
        else:
            self.cqbits = np.empty(nqbits)
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
        
        return self.circuitSeq

    def set_state(self,state):
        """
        Sets the state of the quantum register to the state specified by the input state.

        
        :param: state (int/list): can be a int showing the qubit state("110") or list of qubit states([ [1,0],[0,1],[0.5,0.5]]). The list supports float values. 
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
        """Prints the circuit sequence of the quantum register. Alternative to str() method.
        """
        print("Circuit Sequence: {}".format(self.circuitSeq))
    
    def output(self):
        """ Prints the output of the quantum register probabilities in the basis space. Shows the states with the maximum probability.
        This method should be called after the measurement of the register.
        

        :return: basisSpace (list): The basis space of the quantum register.
        """
        assert self.measured_all == True, "Please measure the register before printing the output."
        print("State\t\tProbability")
        print("-----\t\t-----------")
        for i in range(len(self.registerStates)):
            #print if probability is greater than 5%
            if self.state_probability[i] == np.amax(self.state_probability):
            
                print("{} ({})\t\t{:.2f}%".format( self.registerStates[i],int( self.registerStates[i],2),self.state_probability[i]*100))
        return self.basisSpace


        
    def measure_one_qubit(self,i_nqbit):
        """ Measures the state of a single qbit in the quantum register. The qbit is specified by the index i_nqbits.

        :param i_nqbits (int, optional): The Qubit to collapse. Required.

    
        :param float: The collapsed state of the specified qbit.
        """
        p0 = np.sum(self.state_probability[np.where(['0' in s[-i_nqbit] for s in self.registerStates])])
        
        return np.random.choice([0,1], p=[p0,1-p0])