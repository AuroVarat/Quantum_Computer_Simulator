"""
Quantum Circuit Class initialises a quantum circuit with nqbits qbits and initialises all qbits to |0>.
It has two subclasses LazyCircuit and EagerCircuit.
"""
"""
Title: Quantum Circuit Class \n
Author: Auro Varat Patnaik \n
Date: 2023-03-07 \n
Code version: 3.0 \n
  
"""

import numpy as np
from scipy.sparse import identity
import sys
sys.path.append("../resources")
sys.path.append("./resources")
from qRegister import QbitRegister
import time

class LazyCircuit(QbitRegister):
  
    """
    Qbit Register Class initialises a quantum register with nqbits qbits and initialises all qbits to |0>l,
    and contains methods to apply gates to the qbits in the register. 
    """
 
    def __init__(self,nqbits=2,name = "qregister"):
        """Defines a Quantum Register with nqbits qbits and initialises all qbits to |0>.
        The Quantum Register is represented by a vector in the 2^nqbits dimensional basis space, i.e. the Hilbert Spac of the nqbits.

     
        :param nqbits (int, optional): Number of Qbits in the Quantum Register. Defaults to 2.
        :param name (str, optional): Label of the register. Defaults to "qregister".
        """
       
        self.timer = time.time()
        self.circuit = self.create_circuit()(identity(2**nqbits,dtype=int))
        QbitRegister.__init__(self,nqbits,name)
        print("--> {} initialised with {} qbits.".format(self.name,self.nqbits))

        
    def create_circuit(self): 
        """ Creates a circuit element that can be applied to the quantum register.
        """ 
        def circuitElement(next_gate):
            """Generates a circuit element that can be applied to the quantum register using Lambda function
        
    
            :param next_gate (2D Numpy Array): Quantum Gate to be applied to the quantum register

            :returns: lambda function : Lambda funtion that applies the circuit element to the quantum register when measure = True and when measure = False it applies to the next gate in the circuit.
            """
            return lambda prev_gate,measure=False: circuitElement(next_gate @ prev_gate) if measure != True else  prev_gate @ next_gate
        return circuitElement
    
  
 

        
    def addToCircuit(self,  gate, ith_qbit=None,name=None):
        """Applies a gate to the ith qbit in the quantum register. If the gate is a 2D gate then it is applied to the ith and (i+1)th qbit.
   
        :param    gate (Numpy Array): Gate to be applied
        :param    ith_qbit (int): ith qbit to be operated on
        
        """

        if ith_qbit != None:
            self.circuit = self.circuit(self.operation(gate,ith_qbit))
            self.circuitSeq.append((name,ith_qbit))
        else:
            self.circuit = self.circuit(gate)
            self.circuitSeq.append((name))
       
        
    def measure(self):
        """Measures the quantum register in the computational basis and returns the result.
        
        :returns: Measurement result (1D Numpy Array) 
        """
        self.timer = time.time() - self.timer #time taken to run the circuit
        self.basisSpace = self.circuit(self.basisSpace,measure=True) #basis space after measurement
        state_probability = np.abs(self.basisSpace)**2 #probability of each state
        #get the index where the probability is highest
        state_found = np.where(state_probability == np.amax(state_probability))
        #get the state with the highest probability
        state = self.registerStates[state_found[0][0]]
      

        #print a table containing the state and its probability only if probability is greater than 0.5%
      
        print("State\t\tProbability")
        print("-----\t\t-----------")
        for i in range(len(self.registerStates)):
            #print if probability is greater than 0.5%
            if state_probability[i] > 0.5:
                print("{}\t\t{:.2f}%".format(self.registerStates[i],state_probability[i]*100))
        print("Time taken to run the circuit: {:.2f} seconds".format(self.timer))

    

        return self.basisSpace
        
    def to_gate(self):
        """Converts the quantum register to a gate
        
        :returns: (2D Sparse or Numpy Matrix)Circuit as a gate 
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

     
        :param nqbits (int, optional): Number of Qbits in the Quantum Register. Defaults to 2.
        :param name (str, optional): Label of the register. Defaults to "qregister".
        """
        
        self.timer = time.time()
        self.state_history = []
        self.marked_state_history = []
        QbitRegister.__init__(self,nqbits,name)
   
    def measure(self):
        """Measures the quantum register in the computational basis and returns the result.
        
        :returns: Measurement result (1D Numpy Array) 
        """
        self.timer = time.time() - self.timer #time taken to run the circuit
      
        self.state_probability = np.abs(self.basisSpace)**2 #probability of each state
        #get the index where the probability is highest
        state_found = np.where(self.state_probability == np.amax(self.state_probability))
        #get the state with the highest probability
        state = self.registerStates[state_found[0][0]]
      
      
        #print a table containing the state and its probability only if probability is greater than 0.5%
      
        print("State\t\tProbability")
        print("-----\t\t-----------")
        for i in range(len(self.registerStates)):
            #print if probability is greater than 0.5%
            if self.state_probability[i] > 0.5:
                print("{}\t\t{:.2f}%".format(self.registerStates[i],self.state_probability[i]*100))
        print("Time taken to run the circuit: {:.2f} seconds".format(self.timer))

        return self.basisSpace


    
    def addToCircuit(self,gate, ith_qbit=None,name=None):
        """Applies a gate to the ith qbit in the quantum register. If the gate is a 2D gate then it is applied to the ith and (i+1)th qbit.
        
        :param  gate (Numpy Array): Gate to be applied
        :param  ith_qbit (int): ith qbit to be operated on
        """
        if ith_qbit != None:
         
            self.basisSpace = self.operation(ith_qbit,gate) @ self.basisSpace
            self.circuitSeq.append((name,ith_qbit+1))
        else:
        # Apply the gate
   
            self.basisSpace =gate @ self.basisSpace
            self.circuitSeq.append((name))
       
        

    def record_state_vector_projection(self):
        """Records the projection of the state vector onto the computational basis.
        """
        assert self.recording == True, "Oracle not set to record"
        w = self.winnerState
        s = self.basisSpace.real
        
        x = np.dot(s,self.s_prime)
        y = np.dot(s,w)
        
        self.state_history.append([x,y])
    
    def record_marked_state(self,marked_state_index):
        """
        Records the Amplitude of the marked state.
        """
        assert self.recording == True, "Oracle not set to record"
        
        self.marked_state_history.append(self.basisSpace.real[marked_state_index])

   
       
       
       
       
       
        
  

   

# %%
