
import numpy as np
from art import *

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
    def cnot(self, control_qbit, target_qbit):
        """Controlled Not Gate
        Args:
            control_qbit (nth qubit): Selects the control qubit
            target_qbit (nth qubit): Selects the target qubit
        """
        tprint("Controlled Not Operation",font="monospace")
        tprint(" ---------------------------",font="monospace")
        cnot_matrix = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]
        ])
        self.operation(cnot_matrix, control_qbit)
        
class MultiQbitGate():
    
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
        
       
       