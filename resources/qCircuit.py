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
 
    def __init__(self,nqbits,name = "qregister",cqbits=None):
        """Defines a Quantum Register with nqbits qbits and initialises all qbits to |0>.
        The Quantum Register is represented by a vector in the 2^nqbits dimensional basis space, i.e. the Hilbert Spac of the nqbits.

     
        :param nqbits (int, optional): Number of Qbits in the Quantum Register. Defaults to 2.
        :param name (str, optional): Label of the register. Defaults to "qregister".
        """
       
        self.timer = time.time()
        self.circuit = self.create_circuit()(identity(2**nqbits))
        QbitRegister.__init__(self,nqbits,cqbits,name)
        # print("--> {} initialised with {} qbits.".format(self.RegisterName,self.nqbits))

        
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
            gate = self.operation(gate,ith_qbit)
        
            self.circuit = self.circuit(gate)
            self.circuitSeq.append((name,ith_qbit))
        else:
            self.circuit = self.circuit(gate)
            self.circuitSeq.append((name))
       
        
    def measure(self,i_nqbits=None):
        """ Measures the quantum register in the computational basis and returns the result. If i_nqbits is None then all qbits are measured and the result is returned as a string. If i_nqbits is an integer then the first i_nqbits are measured and the result is returned as a string.

        :param i_nqbits (int, optional): Number of qbits to be measured. Defaults to None.
        :returns: (str) Measurement result
        """
       
        self.basisSpace = self.circuit(self.basisSpace,measure=True) #basis space after measurement
        self.state_probability = np.abs(self.basisSpace)**2 #probability of each state
        self.state_probability = self.state_probability/np.sum(self.state_probability) #normalised probability of each state   
       
        if i_nqbits == None:
            self.measured_all = True
            self.measurement_state = np.random.choice(self.registerStates, p=self.state_probability)
            
            
        elif type(i_nqbits) == int:
            assert i_nqbits <= self.nqbits, "qubits must be less than the number of qbits in the register"
            
            m = []
            for i in range(1,i_nqbits+1):
                m.append(self.measure_one_qubit(i))
                self.cqbits[-i]= self.measure_one_qubit(i)  

            
            self.measurement_state = ''.join(map(str, m[::-1]))
        
        self.timer = time.time() - self.timer #time taken to run the circuit
        print("Measurement Result: {} ({})".format(self.measurement_state,int(self.measurement_state,2)))
        print("Time taken to run the circuit: {:.2f} seconds".format(self.timer))

        return self.measurement_state

        
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
 
    def __init__(self,nqbits,name = "BasicQregister",cqbits=None):
        """Defines a Quantum Register with nqbits qbits and initialises all qbits to |0>.
        The Quantum Register is represented by a vector in the 2^nqbits dimensional basis space, i.e. the Hilbert Spac of the nqbits.

     
        :param nqbits (int, optional): Number of Qbits in the Quantum Register. Defaults to 2.
        :param name (str, optional): Label of the register. Defaults to "qregister".
        """
        
        self.timer = time.time()
   
        self.state_history = []
        self.marked_state_history = []
        QbitRegister.__init__(self,nqbits,cqbits,name)
     
        
        # print("--> {} initialised with {} qbits.".format(self.RegisterName,self.nqbits))
   
    def measure(self,i_nqbits=None):
        """ Measures the quantum register in the computational basis and returns the result. If i_nqbits is None then all qbits are measured and the result is returned as a string. If i_nqbits is an integer then the first i_nqbits are measured and the result is returned as a string.

        :param i_nqbits (int, optional): Number of qbits to be measured. Defaults to None.
        :returns: (str) Measurement result
        """
        assert i_nqbits == None or type(i_nqbits) == int, "qubits must be None, int. Current Implementation only supports measurement of all qubits or the first nth qubits."
       
        self.timer = time.time() - self.timer #time taken to run the circuit
        self.state_probability = np.abs(self.basisSpace)**2
        self.state_probability /=  np.sum(self.state_probability) #probability of each state
        if i_nqbits == None:
            self.measured_all = True
            self.measurement_state = np.random.choice(self.registerStates, p=self.state_probability)
            
            
        elif type(i_nqbits) == int:
            assert i_nqbits <= self.nqbits, "qubits must be less than the number of qbits in the register"
            
            m = []
            for i in range(1,i_nqbits+1):
                m.append(self.measure_one_qubit(i))
                self.cqbits[-i]= self.measure_one_qubit(i)  

            
            self.measurement_state = ''.join(map(str, m[::-1]))
        
        
        print("Measurement Result: {} ({})".format(self.measurement_state,int(self.measurement_state,2)))
        print("Time taken to run the circuit: {:.2f} seconds".format(self.timer))

        return self.measurement_state


        
    
    def addToCircuit(self,gate, ith_qbit=None,name=None):
        """Applies a gate to the ith qbit in the quantum register. If the gate is a 2D gate then it is applied to the ith and (i+1)th qbit.
        
        :param  gate (Numpy Array): Gate to be applied
        :param  ith_qbit (int): ith qbit to be operated on
        """
        if ith_qbit != None:
         
            self.basisSpace = self.operation(gate,ith_qbit) @ self.basisSpace
            self.circuitSeq.append((name,ith_qbit+1))
        else:
        # Apply the gate
   
            self.basisSpace =gate @ self.basisSpace
            self.circuitSeq.append((name))
       
        

    def record_state_vector_projection(self):
        """Records the projection of the state vector onto the computational basis.
            Needs to be called after the oracle is applied and before the measurement is taken.
        """
        assert self.recording == True, "Oracle not set to record"
        w = self.winnerState
        s = self.basisSpace.real
        
        x = np.dot(s,self.s_prime)
        y = np.dot(s,w)
        
        self.state_history.append([x,y])
    
    def record_marked_state(self,marked_state_index):
        """
        Records the Amplitude of the marked state.  Needs to be called after the oracle is applied and before the measurement is taken.
        
        """
        assert self.recording == True, "Oracle not set to record"
        
        self.marked_state_history.append(self.basisSpace.real[marked_state_index])

        
  
       
       
       
        
  

   

# %%
