"""
Title: Preloader Class
Author: Auro Varat Patnaik
Date: 2023-03-07    
Code version: 3.0
Description: Preloader Class preloads all the commonly used gate matrices and other constants required for the simulation.
"""

import numpy as np
from scipy.linalg import hadamard
from scipy.sparse import diags,csr_matrix,eye

isq2 = 1/np.sqrt(2) # 1/sqrt(2)

class gateMatrices():
    def __init__(self):
       
        self.root_factor = lambda n : isq2**n
        
        
        self.I = lambda n: eye(2**n)
      
      
        #Hadamard
        self.H = lambda N: self.root_factor(N) * hadamard(2**N) # Hadamard for n qubits
        self.H_all = self.H(self.nqbits)
        self.H_2x2 = self.H(2)
        #V gate
        self.V = diags([1,1j],format='csr')
        #Pauli X and derivatives
        self.X = lambda n: csr_matrix(np.fliplr(np.eye(n)))
        self.X_all = csr_matrix(np.fliplr(np.eye(self.N)))
        self.X_2x2 = self.X(2)
        self.cX_4x4 = self.addControl(self.X_2x2)
        self.t = self.addControl(self.X_2x2,control_qubits=2)
        self.mct = lambda nC:  self.addControl(self.X_2x2,control_qubits=nC)
        #Pauli Z and derivatives
        self.Z_2x2 = diags([1,-1],format='csr')
        self.cZ_4x4 = self.addControl(self.Z_2x2)
        self.mcZ = lambda nC: self.addControl(self.Z_2x2,control_qubits=nC)
        #Swap
        self.swap_4x4 = diags([[0,1,0],[1,0,0,1],[0,1,0]],offsets=[-1,0,1],format='csr')
        #Phase Shift
        self.P_2x2 = lambda phi : diags([1,np.exp(1j*phi)],format ='csr')
        self.cP = lambda phi : self.addControl(self.p(phi))
        #Reflection about the 1st Qubit
        self.reflection = diags([1,*-np.ones(self.N-1)],format='csr')
        
     
    @staticmethod
    def addControl(gate,control_qubits=1):
        number_of_qubits = int(np.log2(gate.shape[0]))
        total_qubits = number_of_qubits + control_qubits
        control_add = eye(2**total_qubits,format='lil')
        control_add[2**total_qubits-2**number_of_qubits:,2**total_qubits-2**number_of_qubits:] = gate

        return control_add




