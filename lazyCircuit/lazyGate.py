
import numpy as np
from art import *
from scipy.linalg import hadamard
isq2 = 1/np.sqrt(2) # 1/sqrt(2)
from scipy.sparse import diags


class SingleQbitGate():
           
    # def operation(self, register,gate, ith_qbit):
    #     """Applies a gate to the ith qbit in the quantum register. If the gate is a 2D gate then it is applied to the ith and (i+1)th qbit.
    #     Args:
    #         gate (Numpy Array): Gate to be applied
    #         ith_qbit (int): ith qbit to be operated on
    #     """
        
    #     ith_qbit = ith_qbit - 1 # removes 0th qubit and makes the first qubit -> 1 
    #     eyeL = np.eye(2**ith_qbit, dtype=np.complex)
    #     eyeR = np.eye(2**(self.nqbits - ith_qbit - int(gate.shape[0]**0.5)), 
    #         dtype = np.complex)
   
    #     # Tensor product of the gate and the identity matrices
    #     # eyeL ⊗ t ⊗ eyeR
    #     t_all = np.kron(np.kron(eyeL, gate), eyeR)
       
    #     # Apply the gate
    #     return np.matmul(t_all, register)
    # #Single Qbit Gates
    
 
    #Single Qbit Gates
    # Hadamard gate
    def hadamard(self,ith_qbit=None,name="Hadamard"):
        """
        Hadamard Gate

        Args:
            ith_qbit (nth qubit): Selects the qubit to be operated on
        """
        # tprint("Hadamard Operation",font="monospace")
        # tprint(" ---------------------------",font="monospace")
        h_matrix = isq2 * hadamard(2)
        if ith_qbit != None:
 
            self.addToCircuit(h_matrix, ith_qbit,name)
        else:
     
            self.addToCircuit((isq2**self.nqbits)*hadamard(self.N),name=name)
    
    def x(self,ith_qbit):
        """Not Gate
        Args:
            ith_qbit (nth qubit): Selects the qubit to be operated on
        """
        # tprint("Not Operation",font="monospace")
        # tprint(" ---------------------------",font="monospace")
        # x matrix using sparse
            
        x_matrix = np.array([
            [0, 1],
            [1, 0]
        ])
        
        self.addToCircuit(x_matrix, ith_qbit)
    def z(self,ith_qbit):
        """Z Gate
        Args:
            ith_qbit (nth qubit): Selects the qubit to be operated on
        """
        # tprint("Z Operation",font="monospace")
        # tprint(" ---------------------------",font="monospace")
      
        #z using sparse
        z_matrix = diags([1, -1])
        self.addToCircuit(z_matrix, ith_qbit)
        
     
    def cx(self,ith_qbit,jth_qbit):
        assert  ith_qbit != jth_qbit, "The qubits must be different"
        assert ith_qbit < self.nqbits, "The qubit must be less than the number of qubits"
        assert jth_qbit < self.nqbits, "The qubit must be less than the number of qubits"
        assert ith_qbit >= 0, "The qubit must be greater than 0"
        assert jth_qbit >= 0, "The qubit must be greater than 0"
        assert jth_qbit == ith_qbit + 1, "Qubit j must be the qubit after qubit i"
            
       
        # cx_matrix = np.array([
        #     [1, 0, 0, 0],
        #     [0, 1, 0, 0],
        #     [0, 0, 0, 1],
        #     [0, 0, 1, 0]
        # ])
        cx_matrix = diags([[0,0,1],[1, 1, 0, 0],[0,0,1]],[-1,0,1])


        self.addToCircuit(cx_matrix, ith_qbit,jth_qbit)
    
    def cz(self,ith_qbit,jth_qbit):
        assert ith_qbit != jth_qbit, "The qubits must be different"
        assert ith_qbit < self.nqbits, "The qubit must be less than the number of qubits"
        assert jth_qbit < self.nqbits, "The qubit must be less than the number of qubits"
        assert ith_qbit >= 0, "The qubit must be greater than 0"
        assert jth_qbit >= 0, "The qubit must be greater than 0"
        assert jth_qbit == ith_qbit + 1, "Qubit j must be the qubit after qubit i"
        
        cz_matrix = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, -1]
        ])
        diag = np.ones(4)
        diag[-1] = -1
        cz_matrix = diags(diag)
        self.addToCircuit(cz_matrix, ith_qbit)
    
    def swap(self,ith_qbit,jth_qbit):
        # assert ith_qbit != jth_qbit, "The qubits must be different"
        # assert ith_qbit < self.nqbits, "The qubit must be less than the number of qubits"
        # assert jth_qbit < self.nqbits, "The qubit must be less than the number of qubits"
        # assert ith_qbit >= 0, "The qubit must be greater than 0"
        # assert jth_qbit >= 0, "The qubit must be greater than 0"
        # assert jth_qbit == ith_qbit + 1, "Qubit j must be the qubit after qubit i"
        
        swap_matrix = np.array([
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1]
        ])
        swap_matrix =   diags([[0,1,1],[1, 0, 0, 1],[0,1,0]],[-1,0,1])
        self.addToCircuit(swap_matrix, ith_qbit)

    def mcz( self, control_qubits, target_qubit):
        """Applies a multi-controlled Toffoli gate.
        Args:
            control_qubits (list(int)): List of control qubits
            target_qubit (int): Target qubit
            ancilla_qubits (list(int)): List of ancilla qubits
            gate (Gate): Gate to be applied
            use_basis_gates (bool): If True, decompose the multi-controlled Toffoli
                gate into basis gates. Otherwise, use the quantum volume circuit
                defined in https://arxiv.org/abs/1811.12926.
        # """
        # assert len(control_qubits) > 1, "There must be more than one control qubit"
        # assert target_qubit not in control_qubits, "The target qubit cannot be a control qubit"
        # assert target_qubit < self.nqbits, "The qubit must be less than the number of qubits"
        # assert target_qubit >= 0, "The qubit must be greater than 0"
        # for qubit in control_qubits:
        #     assert qubit < self.nqbits, "The qubit must be less than the number of qubits"
        #     assert qubit >= 0, "The qubit must be greater than 0"
        # if ancilla_qubits is None:
        #     ancilla_qubits = []
        # assert len(ancilla_qubits) >= len(control_qubits) - 2, "Insufficient number of ancilla qubits"
        # for qubit in ancilla_qubits:
        #     assert qubit < self.nqbits, "The qubit must be less than the number of qubits"
        #     assert qubit >= 0, "The qubit must be greater than 0"
        #     assert qubit not in control_qubits, "The ancilla qubit cannot be a control qubit"
        #     assert qubit != target_qubit, "The ancilla qubit cannot be the target qubit"
        # if use_basis_gates:
        #     self._apply_mct_basis_gates(control_qubits, target_qubit, ancilla_qubits, gate)
        # else:
        #     self._apply_mct(control_qubits, target_qubit, ancilla_qubits, gate)
        mcz_diag = np.zeros(self.N)
        mcz_diag[control_qubits+1] = 1
        mcz_diag[target_qubit] = -1
        
        self.addToCircuit(diags(mcz_diag))
      
    def control_phase_shift(self, except_state = 1, phi = np.pi):
        """Controlled Phase Shift Gate

        Args:
            ith_qbit (nth qubit): Selects the qubit to be operated on
            phi (float): Phase shift angle in radians
        """

        
        except_state -= 1 
        diagonal = np.full(2**self.nqbits, np.exp(1j * phi))
        diagonal[except_state] = 1
        control_phase_shift_matrix = diags(diagonal)
        
        self.addToCircuit(control_phase_shift_matrix)
    
    
        
    def customGate(self, gate_matrix, qubits=None,name="Custom Gate"):
        """Custom Gate

        Args:
            gate_matrix (matrix): The matrix of the gate
            qubits (list): The qubits to be operated on
        """
        if qubits != None: 
                
            self.addToCircuit(gate_matrix, qubits,name)
        else:
            self.addToCircuit(gate_matrix,name=name)