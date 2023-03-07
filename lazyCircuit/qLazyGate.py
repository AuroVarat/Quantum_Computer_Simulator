
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
    
 
    def hadamard(qbit=None,except_state=None):
        # h = lambda qubit : [[1, 0], [isq2, isq2]] if np.array_equal(qubit,[1,0]) else qubit
        
        return lambda qubits : np.where(qubits == [1,0],[isq2, isq2],qubits)
        # if qbit != None:
 
        #     return lambda qubits :np.where(h )     h(qubits[qbit])
        # elif except_state:
        #     return lambda qubits : h(qubits[~except_state])
        # else:
        #     return lambda qubits : (h(q) for q in qubits)
      
      
            
        
    
      

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
        
        
    def swap_and_unswap(self,control,target):
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
        for _ in range(1,target-control):
            target = target - 1
            self.operation(swap_matrix, target)
        
        #unswap
        
        for _ in range(1,target-control):
                control = control + 1
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
        
       
    