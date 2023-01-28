#%%
import numpy as np
from art import *

isq2 = 1/np.sqrt(2)
# class for qunatum gates
class QbitRegister:
 
    def __init__(self,nqbits=2,name = "qregister"):
        self.nqbits = nqbits
        self.basisSpace = np.zeros(2**self.nqbits, dtype=np.int)
        #all qbits are by default initialised to |0>
        self.basisSpace[0] = 1
       
       
        tprint("Quantum",font="starwars")
        tprint(" ---------------------------",font="digital")
        tprint("Quantum Register {} Initialised: |".format(name)+nqbits*"0"+">",font="monospace")
        tprint(" ---------------------------",font="monospace")
        
    def __str__(self):
        return str(self.basisSpace.real)
        
    def op(self, t, i):
        # I_{2^i}
        eyeL = np.eye(2**i, dtype=np.complex)

        # I_{2^{n-i-1}}
        # t.shape[0]**0.5 denotes how many bits t applies to
        # in case of NOT, t.shape[0]**0.5 == 1
        eyeR = np.eye(2**(self.nqbits - i - int(t.shape[0]**0.5)), 
            dtype = np.complex)

        # eyeL ⊗ t ⊗ eyeR
        t_all = np.kron(np.kron(eyeL, t), eyeR)

        # apply transformation to state (multiplication)
        self.basisSpace = np.matmul(t_all, self.basisSpace)
        
    # Hadamard gate
    def hadamard(self, i):
        h_matrix = isq2 * np.array([
            [1,1],
            [1,-1]
        ])    
        self.op(h_matrix, i)

    # T gate
    def t(self, i):
        t_matrix = np.array([
            [1,0],
            [0,isq2 + isq2 * 1j]
        ])
        self.op(t_matrix, i)

    # S gate
    def s(self, i):
        s_matrix = np.array([
            [1,0],
            [0,0+1j]
        ])    
        self.op(s_matrix,i)

    # CNOT gate
    def cnot(self, i):
        cnot_matrix = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]
        ])
        self.op(cnot_matrix, i)
        
    def phase_shift(self, i, phi):
        phase_shift_matrix = np.array([
            [1, 0],
            [0, np.exp(1j * phi)]
        ])
        self.op(phase_shift_matrix, i)
        
    # Swap two qubits
    def swap(self, i):
        swap_matrix = np.array([
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1]
        ])
        self.op(swap_matrix, i)

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
    
        
               

   

   
