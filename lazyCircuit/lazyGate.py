
import numpy as np
from art import *
from scipy.linalg import hadamard
isq2 = 1/np.sqrt(2) # 1/sqrt(2)
from scipy.sparse import diags
from scipy.sparse import csr_matrix,identity,eye,kron
from scipy.sparse.linalg import inv


class QbitGate():
    def __init__(self):
        self.h_matrix = isq2 * np.array([
        [1,1],
        [1,-1]
        ])
        self.hadamard_matrix = isq2**self.nqbits * hadamard(self.N)
        
        self.x_matrix = csr_matrix( np.array([
        [0, 1],
        [1, 0]
        ]))
        self.X_matrix = csr_matrix( np.fliplr(np.eye(self.N)))
        self.z_matrix =csr_matrix( np.array([
        [1, 0],
        [0, -1]
        ]))
        self.cx_matrix = csr_matrix(np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]
        ]))
        self.cz_matrix =csr_matrix( np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, -1]
        ]) )
        self.swap_matrix =csr_matrix( np.array([
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1]
        ]))

       
        self.control_phase_shift_matrix = lambda phi : csr_matrix(np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, np.exp(1j*phi)]])  )
        
     
    
        mcz_diag = -np.ones(self.N)
        mcz_diag[0] = 1
        
        self.mcz_matrix = diags(mcz_diag)

        

    def hadamard(self,ith_qbit=None,name="Hadamard"):
        """
        Hadamard Gate

        Args:
            ith_qbit (nth qubit): Selects the qubit to be operated on
        """
        # tprint("Hadamard Operation",font="monospace")
        # tprint(" ---------------------------",font="monospace")
      
        if ith_qbit != None:
 
            self.addToCircuit(self.h_matrix, ith_qbit,name)
        else:
     
            self.addToCircuit(self.hadamard_matrix,name=name)
    
    def x(self,ith_qbit=None,name="X"):
        """Not Gate
        Args:
            ith_qbit (nth qubit): Selects the qubit to be operated on
        """
        # tprint("Not Operation",font="monospace")
        # tprint(" ---------------------------",font="monospace")
        if ith_qbit != None:
 
            self.addToCircuit(self.x_matrix, ith_qbit,name)
        else:
     
            self.addToCircuit(self.X_matrix,name=name)

        
    def z(self,ith_qbit):
        """Z Gate
        Args:
            ith_qbit (nth qubit): Selects the qubit to be operated on
        """
        # tprint("Z Operation",font="monospace")
        # tprint(" ---------------------------",font="monospace")
       
        self.addToCircuit(self.z_matrix, ith_qbit)    
     
    def cx(self,ith_qbit,jth_qbit):
        # assert  ith_qbit != jth_qbit, "The qubits must be different"
        # assert ith_qbit < self.nqbits, "The qubit must be less than the number of qubits"
        # assert jth_qbit < self.nqbits, "The qubit must be less than the number of qubits"
        # assert ith_qbit >= 0, "The qubit must be greater than 0"
        # assert jth_qbit >= 0, "The qubit must be greater than 0"
        # assert jth_qbit == ith_qbit + 1, "Qubit j must be the qubit after qubit i"
            
     
        self.addToCircuit(self.cx_matrix, ith_qbit,jth_qbit)
    
    def cz(self,ith_qbit,jth_qbit):
        # assert ith_qbit != jth_qbit, "The qubits must be different"
        # assert ith_qbit < self.nqbits, "The qubit must be less than the number of qubits"
        # assert jth_qbit < self.nqbits, "The qubit must be less than the number of qubits"
        # assert ith_qbit >= 0, "The qubit must be greater than 0"
        # assert jth_qbit >= 0, "The qubit must be greater than 0"
        # assert jth_qbit == ith_qbit + 1, "Qubit j must be the qubit after qubit i"
        
        
        self.addToCircuit(self.cz_matrix, ith_qbit)
    
    def swap(self,ith_qbit,jth_qbit,name="Swap"):
      
        assert ith_qbit != jth_qbit, "The qubits must be different"
        assert ith_qbit <= self.nqbits, "The qubit must be less than the number of qubits"
        assert jth_qbit <= self.nqbits, "The qubit must be less than the number of qubits"
        assert ith_qbit >= 1, "The qubit must be greater than 0"
        assert jth_qbit >= 1, "The qubit must be greater than 0"
        assert jth_qbit >= ith_qbit + 1, "Qubit j must be the qubit after qubit i"
        
        if jth_qbit - ith_qbit == 1:
            self.addToCircuit(self.swap_matrix, ith_qbit,name =(name + "({},{})".format(ith_qbit,jth_qbit)))
            self.unswap_matrix = inv(self.swap_matrix)
        else:
            swap,self.unswap_matrix = self.nonadjacent_control(ith_qbit,jth_qbit,unswap=True)
            self.addToCircuit(swap,name =(name + "({},{})".format(ith_qbit,jth_qbit)))
            
    def unswap(self,ith_qbit,jth_qbit,name="Unswap"):
        
        if jth_qbit - ith_qbit == 1:
            self.addToCircuit(self.swap_matrix, ith_qbit,name =(name + "({},{})".format(ith_qbit,jth_qbit)))
      
        else:
          
            self.addToCircuit(self.unswap_matrix,name =(name + "({},{})".format(ith_qbit,jth_qbit)))
            
        
 
    def mcz( self):
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
     
        
        self.addToCircuit(self.mcz_matrix)
      
    def control_phase_shift(self, ith_qbit,jth_qbit,phi = np.pi):
        """Controlled Phase Shift Gate

        Args:
            ith_qbit (nth qubit): Selects the qubit to be operated on
            phi (float): Phase shift angle in radians
        """
        assert ith_qbit <= self.nqbits, "The qubit must be less than the number of qubits"
        assert ith_qbit >= 1, "The qubit must be greater than 0"
        assert jth_qbit <= self.nqbits, "The qubit must be less than the number of qubits"
        assert jth_qbit >= 1, "The qubit must be greater than 0"
        
        # assert phi >= 0, "The phase shift must be greater than 0"
        # assert phi <= 2*np.pi, "The phase shift must be less than 2pi"
        if jth_qbit - ith_qbit == 1:
            self.addToCircuit(self.control_phase_shift_matrix(phi), ith_qbit)
        else:
            self.swap(ith_qbit+1,jth_qbit)
            self.addToCircuit(self.control_phase_shift_matrix(phi),ith_qbit)
            self.unswap(ith_qbit+1,jth_qbit)
            
    
    def nonadjacent_control(self,ith_qbit,jth_qbit,unswap=False):
        
        swap = self.create_apply(self.swap_matrix,ith_qbit)
        for j in range(ith_qbit+1,jth_qbit):
            swap = swap @ self.create_apply(self.swap_matrix,j)
    
      
        # if ~unswap:
        #     return swap 
        
        return swap,inv(swap)
    
    def create_apply(self,gate,ith_qbit):
        ith_qbit = ith_qbit - 1 # removes 0th qubit and makes the first qubit -> 1 
            #sparse eye matrices
 
        eyeL = eye(2**ith_qbit, dtype=np.complex,format='csr')
        eyeR = eye(2**(self.nqbits - ith_qbit - 2), 
            dtype = np.complex,format='csr')

        # Tensor product of the gate and the identity matrices
        # eyeL ⊗ t ⊗ eyeR
        return kron(kron(eyeL, gate), eyeR)
    
    
        
# class customGate():
#     """Custom Gate

#     Args:
#         gate_matrix (matrix): The matrix of the gate
#         qubits (list): The qubits to be operated on
#     """
#     def __new__(self,gate_matrix,name="Custom Gate"):
#         self.name = name
     
#         self.gate_matrix = gate_matrix
#         return self.gate_matrix
        
       
#     def power(self, n):
  
#         if n == 0:
#             self.gate_matrix = np.eye(self.gate_matrix.shape[0])
      
#         else:
#             return np.linalg.matrix_power(self.gate_matrix,n)
        
#     def control(self):
#         """Controlled Gate

#         Args:
#             gate_matrix (matrix): The matrix of the gate
#             qubits (list): The qubits to be operated on
#         """
#         self.addToCircuit(self.control_matrix)
       
#     # if qubits != None: 
            
#     #     self.addToCircuit(csr_matrix(gate_matrix),qubits,name=name)
#     # else:
#     #     self.addToCircuit(csr_matrix(gate_matrix),name=name)