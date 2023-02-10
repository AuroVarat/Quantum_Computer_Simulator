#%%
import numpy as np
from art import *

isq2 = 1/np.sqrt(2) # 1/sqrt(2)


class QbitRegister:
  
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
        
        self.nqbits = nqbits
        self.N = 2**self.nqbits
        self.basisSpace = np.zeros(2**self.nqbits, dtype=np.int) #  basis state formed by tensor product of all qbits
        self.basisSpace[0] = 1 #all qbits are by default initialised to |0>
       
        #Pretty printing showing the initialisation of the quantum register
        tprint("Quantum",font="starwars")
        tprint(" ---------------------------",font="digital")
        tprint("Quantum Register {} Initialised: |".format(name)+nqbits*"0"+">",font="monospace")
        tprint(" ---------------------------",font="monospace")
        
    def __str__(self):
        """Prints the quantum register in the basis space
        """
        tprint(str(self.basisSpace.real)+"\n",font="monospace")
        return "Register in the {} dimension basis space.\n".format(self.nqbits)

    def output(self):
        """Prints the quantum register in the basis space and returns the circuit output
        Returns:
            (Numpy Array): Hilbert Space of the quantum register, post circuit operation.
   
        """
        tprint(str(self.basisSpace.real)+"\n",font="monospace")
        return self.basisSpace
            
    def operation(self, gate, ith_qbit):
        """Applies a gate to the ith qbit in the quantum register. If the gate is a 2D gate then it is applied to the ith and (i+1)th qbit.
        Args:
            gate (Numpy Array): Gate to be applied
            ith_qbit (int): ith qbit to be operated on
        """
        
        ith_qbit = ith_qbit - 1 # removes 0th qubit and makes the first qubit -> 1 
        eyeL = np.eye(2**ith_qbit, dtype=np.complex)
        eyeR = np.eye(2**(self.nqbits - ith_qbit - int(gate.shape[0]**0.5)), 
            dtype = np.complex)
   
        # Tensor product of the gate and the identity matrices
        # eyeL ⊗ t ⊗ eyeR
        t_all = np.kron(np.kron(eyeL, gate), eyeR)
       
        # Apply the gate
        self.basisSpace = np.matmul(t_all, self.basisSpace)
        
    #Single Qbit Gates
    # Hadamard gate
    def hadamard(self, ith_qbit = None ):
        """
        Hadamard Gate

        Args:
            ith_qbit (nth qubit): Selects the qubit to be operated on
        """
        tprint("Hadamard Operation",font="monospace")
        tprint(" ---------------------------",font="monospace")
        h_matrix = isq2 * np.array([
            [1,1],
            [1,-1]
        ])    
        
        h_matrix_0 = isq2 * np.array([
            [1,1],
            [1,-1]
        ])    
        
     
        if ith_qbit != None:
         
         
            self.operation(h_matrix, ith_qbit)
            
        else:
          
            for _ in range(self.nqbits-1):
                h_matrix = np.kron(h_matrix,h_matrix_0)
      
            self.basisSpace = np.matmul(h_matrix, self.basisSpace)
            
        
    
      

    def phase_shift(self, ith_qbit, phi):
        """Phase Shift Gate
        Args:
            ith_qbit (nth qubit): Selects the qubit to be operated on
            phi (float): Phase shift angle in radians
        """
        tprint("Phase Shift Operation with phi = {}° degrees".format(np.rad2deg(phi)),font="monospace")
        tprint(" ---------------------------",font="monospace")
        phase_shift_matrix = np.array([
            [1, 0],
            [0, np.exp(1j * phi)]
        ])
        self.operation(phase_shift_matrix, ith_qbit)
   
   # Two Qbit Gates
    # CNOT gate
    def cnot(self, ith_qbit):
        """CNOT Gate

        Args:
            ith_qbit (nth qubit): Selects the qubit to be operated on
        """
        tprint("XOR Operation",font="monospace")
        tprint(" ---------------------------",font="monospace")
        cnot_matrix = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]
        ])
        self.operation(cnot_matrix, ith_qbit)
        
    # Oracles
    def oracle(self, winner = 4):
        """" this is the oracle function that performs a conditional phase shift for the item we're looking for  """
        tprint("Oracle function", font="monospace")
        tprint(" ---------------------------", font="monospace")


        oracle_matrix = np.eye(self.N)
        oracle_matrix[winner-1, winner-1] = -1  # flip sign of entry corresponding to w
        # is a sparse matrix, make it faster

        # Apply the gate
        self.basisSpace = np.matmul(oracle_matrix, self.basisSpace)
        
    
    # Controlled Phase Shift
    def control_phase_shift(self, except_state = 1, phi = np.pi):
        """Controlled Phase Shift Gate

        Args:
            ith_qbit (nth qubit): Selects the qubit to be operated on
            phi (float): Phase shift angle in radians
        """
        tprint("Controlled Phase Shift Operation with phi = {:.2f}° degrees".format(np.rad2deg(phi)),font="monospace")
        tprint(" ---------------------------",font="monospace")
        
        except_state -= 1 
        diagonal = np.full(2**self.nqbits, np.exp(1j * phi))
        diagonal[except_state] = 1
        control_phase_shift_matrix = np.diag(diagonal)
        
    
        self.basisSpace = np.matmul(control_phase_shift_matrix, self.basisSpace)
        
       
       
       
       
       
       
       
       
       
       
       
        
    # Incomplete gates below / no usage yet
    # Swap two qubits
    def swap(self, i):
        """ Swap two qubits

        Args:
            ith_qbit (nth qubit): Selects the qubit to be operated on
        """
        swap_matrix = np.array([
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1]
        ])
        self.operation(swap_matrix, i)
 # T gate
    def t(self, i):
        """_summary_

        Args:
            ith_qbit (int): Select the qbit to be operated on.
        """
        t_matrix = np.array([
            [1,0],
            [0,isq2 + isq2 * 1j]
        ])
        self.operation(t_matrix, i)

    # S gate
    def s(self, i):
        """_summary_

        Args:
            ith_qbit (nth qubit): Selects the qubit to be operated on
            phi (_type_): _description_
        """
        s_matrix = np.array([
            [1,0],
            [0,0+1j]
        ])    
        self.operation(s_matrix,i)


    # def hadamard(self,qbit,n=(1,)):
    #     n = slice(*n)
    #     qbit[n] = qbit[n]@((1/np.sqrt(2))*np.array([[1,1],[1,-1]]))
    #     return qbit
    # @staticmethod
    # def phase_shift(qbit,n=(1,),phi=2*np.pi):
    #     n = slice(*n)
    #     qbit[n] = qbit[n]@np.round(np.array([[1,0],[0,np.exp(1j*phi)]]))
        
    #     return qbit
    
    # @staticmethod
    # def cnot(qbit,target_control=[1,3]):
    #     #using tensordot right now but will chanhe it later
    #     return np.tensordot(qbit[target_control[0]-1],qbit[target_control[1]-1],axes=0).flatten()@np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
    
        
               

   

   

# %%
