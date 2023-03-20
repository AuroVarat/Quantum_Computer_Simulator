"""
Preloader Class preloads all the commonly used gate matrices and other constants required for the simulation.
"""
"""
Title: Preloader Class
Author: Auro Varat Patnaik
Date: 2023-03-07    
Code version: 3.0

"""

import numpy as np
from scipy.linalg import hadamard
from scipy.sparse import diags,csr_matrix,eye
import sys
sys.path.append("../resources")
sys.path.append("./resources")

isq2 = 1/np.sqrt(2) # 1/sqrt(2)

class gateMatrices():
    """

    :ivar I: Identity Matrix: :math:`I = \\begin{bmatrix} 1 & 0 \\\\ 0 & 1 \\end{bmatrix}`
    :ivar H_2x2, H_all, H: Hadamard Matrix(N), (Hadamard Matrix for all Qubits, Hadamard Matrix for Single Qubit): :math:`H = \\frac{1}{\\sqrt{2}} \\begin{bmatrix} 1 & 1 \\\\ 1 & -1 \\end{bmatrix}`
    :ivar V: Square Root of NOT matrix: :math:`V = \\begin{bmatrix} 1 & 0 \\\\ 0 & i \\end{bmatrix}`
    :ivar X_2x2, X_all, X: Pauli X Matrix(N), (Pauli X Matrix for all Qubits, Pauli X Matrix for Single Qubit): :math:`X = \\begin{bmatrix} 0 & 1 \\\\ 1 & 0 \\end{bmatrix}`
    :ivar Z_2x2, Z_all, Z: Pauli Z Matrix(N), (Pauli Z Matrix for all Qubits, Pauli Z Matrix for Single Qubit): :math:`Z = \\begin{bmatrix} 1 & 0 \\\\ 0 & -1 \\end{bmatrix}`
    :ivar swap_4x4: Swap Matrix: :math:`swap = \\begin{bmatrix} 1 & 0 & 0 & 0 \\\\ 0 & 0 & 1 & 0 \\\\ 0 & 1 & 0 & 0 \\\\ 0 & 0 & 0 & 1 \\end{bmatrix}`
    :ivar cX_4x4: Controlled Pauli X Matrix: :math:`CX = \\begin{bmatrix} 1 & 0 & 0 & 0 \\\\ 0 & 1 & 0 & 0 \\\\ 0 & 0 & 0 & 1 \\\\ 0 & 0 & 1 & 0 \\end{bmatrix}`
    :ivar cZ_4x4: Controlled Pauli Z Matrix: :math:`CZ = \\begin{bmatrix} 1 & 0 & 0 & 0 \\\\ 0 & 1 & 0 & 0 \\\\ 0 & 0 & 1 & 0 \\\\ 0 & 0 & 0 & -1 \\end{bmatrix}`
    :ivar t: Toffoli Matrix :math:`t = \\begin{bmatrix} 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\\\ 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\\\ 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\\\ 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\\\ 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\\\ 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\\\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\\\ 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\end{bmatrix}`
    :ivar mct: Multi-Controlled Toffoli Gate: :math:`mct = \\begin{bmatrix} 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\\\ 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\\\ 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\\\ 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\\\ 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\\\ 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\\\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\\\ 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\end{bmatrix}`
    :ivar mcZ: Multi-Controlled Pauli Z Gate: :math:`mcZ = \\begin{bmatrix} 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\\\ 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\\\ 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\\\ 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\\\ 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\\\ 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\\\ 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\\\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & -1 \\end{bmatrix}`
    :ivar reflection: Reflection Matrix: :math:`reflection = \\begin{bmatrix} 1 & 0 \\\\ 0 & -1 \\end{bmatrix}`
    """
    def __init__(self):
       
        self.root_factor = lambda n : isq2**n
        
        
        self.I = lambda n: eye(2**n)
      
      
        #Hadamard
        self.H = lambda N: self.root_factor(N) * hadamard(2**N) # Hadamard for n qubits
        self.H_all = self.H(self.nqbits)
        self.H_2x2 = self.H(1)
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
        self.cP = lambda phi : self.addControl(self.P_2x2(phi))
        #Reflection about the 1st Qubit
        self.reflection = diags([1,*-np.ones(self.N-1)],format='csr')
        
     
    @staticmethod
    def addControl(gate,control_qubits=1):
        """
        Add control qubits to a gate
        

     
        :param gate (2D Numpy/Sparse): Gate to be controlled
        :param control_qubits (int, optional): Number of Control Qubits. Defaults to 1.

        :returns: (2D Numpy/Sparse) : Gate with control qubits added
        """
        number_of_qubits = int(np.log2(gate.shape[0]))
        total_qubits = number_of_qubits + control_qubits
        control_add = eye(2**total_qubits,format='lil')
        control_add[2**total_qubits-2**number_of_qubits:,2**total_qubits-2**number_of_qubits:] = gate

        return control_add




