
import numpy as np
from art import *
from scipy.linalg import hadamard
isq2 = 1/np.sqrt(2) # 1/sqrt(2)



class SingleQbitGate():
           
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
        # tprint("Hadamard Operation",font="monospace")
        # tprint(" ---------------------------",font="monospace")
        h_matrix = isq2 * np.array([
            [1,1],
            [1,-1]
        ])    
        
       
        if ith_qbit != None:
         
         
            self.operation(h_matrix, ith_qbit)
            
        else:
          

      
            self.basisSpace = (isq2**self.nqbits)*np.matmul(hadamard(int(2**self.nqbits)), self.basisSpace)
          
        
    


    def phase_shift(self, ith_qbit, phi):
        """Phase Shift Gate
        Args:
            ith_qbit (nth qubit): Selects the qubit to be operated on
            phi (float): Phase shift angle in radians
        """
        # tprint("Phase Shift Operation with phi = {}° degrees".format(np.rad2deg(phi)),font="monospace")
        # tprint(" ---------------------------",font="monospace")
        phase_shift_matrix = np.array([
            [1, 0],
            [0, np.exp(1j * phi)]
        ])
        self.operation(phase_shift_matrix, ith_qbit)
        
    def x(self,ith_qbit):
        """Not Gate
        Args:
            ith_qbit (nth qubit): Selects the qubit to be operated on
        """
        # tprint("Not Operation",font="monospace")
        # tprint(" ---------------------------",font="monospace")
        not_matrix = np.array([
            [0, 1],
            [1, 0]
        ])
        self.operation(not_matrix, ith_qbit)
        
    def y(self, ith_qbit):
        """Pauli Y Gate
        Args:
            ith_qbit (nth qubit): Selects the qubit to be operated on
        """
        # tprint("Pauli Y Operation",font="monospace")
        # tprint(" ---------------------------",font="monospace")
        pauli_y_matrix = np.array([
            [0, -1j],
            [1j, 0]
        ])
        self.operation(pauli_y_matrix, ith_qbit)
        
    def z(self, ith_qbit):
        """Pauli Z Gate
        Args:
            ith_qbit (nth qubit): Selects the qubit to be operated on
        """
        # tprint("Pauli Z Operation",font="monospace")
        # tprint(" ---------------------------",font="monospace")
        pauli_z_matrix = np.array([
            [1, 0],
            [0, -1]
        ])
        self.operation(pauli_z_matrix, ith_qbit)

class TwoQbitGate():
    def operation(self, gate, ith_qbit):
        """Applies a gate to the ith and (i+1)th qbit in the quantum register. If the gate is a 2D gate then it is applied to the ith and (i+1)th qbit.
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
    #Two Qbit Gates
    def cnot(self, control_qbit):
        """Controlled Not Gate
        Args:
            control_qbit (nth qubit): Selects the control qubit
            target_qbit (nth qubit): Selects the target qubit
        """
      
        cnot_matrix = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]
        ])
        self.operation(cnot_matrix, control_qbit)
        
        
    def swap(self,control,target):
        """Swap Gate
        Args:
            other (nth qubit): Selects the qubit to be swapped
        """
        # tprint("Swap Operation",font="monospace")
        # tprint(" ---------------------------",font="monospace")
        
        
        swap_matrix = np.array([
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1]
        ])
        
        if target == control + 1:
            self.operation(swap_matrix, control)
        else:
            self.swap_over_distance(control,target)
            
    def swap_over_distance(self,control,target):
        """Swap Gate
        Args:
            other (nth qubit): Selects the qubit to be swapped
        """
        # tprint("Swap Operation",font="monospace")
        # tprint(" ---------------------------",font="monospace")
        
        swap_matrix = np.array([
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1]
        ])
        
        #swap
        for _ in range(control,target):
           
            self.operation(swap_matrix, target)
        
        #unswap
        
        for _ in range(target-2,control-1,-1):
                self.operation(swap_matrix, control)
      
        
class MultiQbitGate():
    
    # Controlled Phase Shift
    def control_phase_shift(self, except_state = 1, phi = np.pi):
        """Controlled Phase Shift Gate

        Args:
            ith_qbit (nth qubit): Selects the qubit to be operated on
            phi (float): Phase shift angle in radians
        """

        
        except_state -= 1 
        diagonal = np.full(2**self.nqbits, np.exp(1j * phi))
        diagonal[except_state] = 1
        control_phase_shift_matrix = np.diag(diagonal)
        
    
        self.basisSpace = np.matmul(control_phase_shift_matrix, self.basisSpace)
        
       
    