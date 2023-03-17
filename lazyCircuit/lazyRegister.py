#%%
from lazyGate import *
import numpy as np
from art import *
from scipy.sparse import diags,identity,eye

isq2 = 1/np.sqrt(2) # 1/sqrt(2)




class QbitRegister(SingleQbitGate):
  
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
        self.name = name
        self.nqbits = nqbits
        self.N = 2**self.nqbits
        self.basisSpace = np.zeros(2**self.nqbits, dtype=float) #  basis state formed by tensor product of all qbits
        self.basisSpace[0] = 1 #all qbits are by default initialised to |0>
        self.rotations = int(np.ceil((((np.pi/2)/np.arcsin(1/np.sqrt(self.N)))-1)/2)) #set to optimum
        self.circuit = self.create_circuit()
        self.circuitSeq = []
       
        # self.N = 2**self.nqbits
        # self.basisSpace = np.zeros(2**self.nqbits, dtype=np.int) #  basis state formed by tensor product of all qbits
        # self.basisSpace[0] = 1 #all qbits are by default initialised to |0>
       
        tprint("Quantum",font="starwars")
        tprint(" ---------------------------",font="digital")
        tprint("Quantum Register {} Initialised: |".format(self.name)+self.nqbits*"0"+">",font="monospace")
        tprint(" ---------------------------",font="monospace")  
        # self.init_print()
        
    def create_circuit(self):   
        def circuitElement(register):
            
            return lambda t_all,measure=False: circuitElement(register @ t_all) if measure != True else  t_all @ register
        return circuitElement
    
 
          
    def measure(self,amax=True):
        """Measures the quantum register in the computational basis and returns the result."""
        result = self.circuit(self.basisSpace,measure=True)
        
        
        if amax:
   
            tprint(str(np.amax(result.real))+"\n",font="monospace")
        else:
             tprint(str(np.around(result.real,decimals=2))+"\n",font="monospace")
        return result
        
    def __str__(self):
        """Prints the quantum register in the basis space
        """
        # tprint(str(self.register)+"\n",font="monospace")
        # return "Register in the {} dimension basis space.\n".format(self.nqbits)
        return str(self.basisSpace.real)
    def output(self):
        """Prints the quantum register in the basis space and returns the circuit output
        Returns:
            (Numpy Array): Hilbert Space of the quantum register, post circuit operation.
   
        """
     
        tprint(str(self.basisSpace.real)+"\n",font="monospace")
        
 
        
    def addToCircuit(self,  gate, ith_qbit=None,name=None):
        """Applies a gate to the ith qbit in the quantum register. If the gate is a 2D gate then it is applied to the ith and (i+1)th qbit.
        Args:
            gate (Numpy Array): Gate to be applied
            ith_qbit (int): ith qbit to be operated on
        """
        if ith_qbit != None:
            ith_qbit = ith_qbit - 1 # removes 0th qubit and makes the first qubit -> 1 
            #sparse eye matrices

            eyeL = eye(2**ith_qbit, dtype=np.complex)
            eyeR = eye(2**(self.nqbits - ith_qbit - int(gate.shape[0]**0.5)), dtype=np.complex)
          
    
            # Tensor product of the gate and the identity matrices
            # eyeL ⊗ t ⊗ eyeR
            t_all = np.kron(np.kron(eyeL, gate), eyeR)
            self.circuit = self.circuit(t_all)
            self.circuitSeq.append((name,ith_qbit+1))
        else:
        # Apply the gate
   
            self.circuit = self.circuit(gate)
            self.circuitSeq.append((name))
       
        
        
        
    def to_gate(self):
        """Converts the quantum register to a gate
        """
        return self.circuit(identity(self.N),measure=True)