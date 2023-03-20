
import numpy as np
from art import *
from scipy.linalg import hadamard
isq2 = 1/np.sqrt(2) # 1/sqrt(2)
from scipy.sparse import diags
import sys
from scipy.sparse import csr_matrix,identity,eye,kron
from scipy.sparse.linalg import inv
sys.path.append('../resources')

from qResources import gateMatrices


class QbitGate(gateMatrices):
    def __init__(self):
       gateMatrices.__init__(self)
       self.swap_status = []

    @staticmethod
    def is_series(lst):
        if len(lst) < 2:
            return False
        diff = 1
        for i in range(2, len(lst)):
            if lst[i] - lst[i-1] != diff:
                return False
        return True
    
    
    def check_qubit_input_for_gate(self,ith_qbit):
        assert ith_qbit == None or type(ith_qbit) == int or type(ith_qbit) == list, "ith_qbit must be an integer or a list of integers"
        if type(ith_qbit) == int:
            assert ith_qbit <= self.nqbits, "The qubit must be less than the number of qubits"
            assert ith_qbit >= 1, "The qubit must be greater than 1"
        if type(ith_qbit) == list:
            ith_qbit = np.asarray(ith_qbit)
            assert (ith_qbit <= self.nqbits).all(), "The qubit must be less than the number of qubits"
            assert (ith_qbit >= 1).all(), "The qubit must be greater than or equal to 1"
            if ~self.is_series(ith_qbit) and self.is_series(np.sort(ith_qbit)):
                #add warning
                print("Warning: The qubits are not in series. The gate will be applied to the qubits in the order they are passed. It is more efficient to pass the qubits in series for some gates.")
            # assert ith_qbit[1] - ith_qbit[0] == 1, "The qubits must be adjacent"
   
    def check_qubit_input_for_cgate(self,ith_qbit,jth_qbit):
        self.check_qubit_input_for_gate(ith_qbit)
        self.check_qubit_input_for_gate(jth_qbit)
        
  
        ith_qbit = np.asarray(ith_qbit)
        jth_qbit = np.asarray(jth_qbit)
        assert (jth_qbit > ith_qbit).any(), "All target qubits must be greater than the control qubits"
        
 
         
        
    def h(self,ith_qbit=None,name="Hadamard"):
        """
        Hadamard Gate

        Args:
            ith_qbit (nth qubit): Selects the qubit(s) to be operated on. If None, applies to all qubits. 
            Multiple Qubits can be selected by passing a list of qubits, but the qubits must be adjacent.
            
            name (str): Name of the gate. Default is "Hadamard"
        """
        
        self.check_qubit_input_for_gate(ith_qbit)



        if ith_qbit == None:
            self.addToCircuit(self.H_all,name=name)
        elif len(ith_qbit) == 1:
            self.addToCircuit(self.H_2x2,ith_qbit,name=(name+"_"+str(ith_qbit)))
        elif len(ith_qbit) > 1 & self.is_series(ith_qbit):
            self.addToCircuit(self.H(len(ith_qbit)),ith_qbit[0],name=(name+"_"+str(ith_qbit)))
        elif len(ith_qbit) > 1 & ~self.is_series(ith_qbit):
            for i in ith_qbit:
                self.addToCircuit(self.H_2x2,i,name=(name+"_"+str(i)))
    
    def x(self,ith_qbit=None,name="X"):
        """Pauli-X Gate
        Args:
            ith_qbit (nth qubit): ith_qbit (nth qubit): Selects the qubit(s) to be operated on. If None, applies to all qubits. 
            Multiple Qubits can be selected by passing a list of qubits, but the qubits must be adjacent.
            
            name (str): Name of the gate. Default is "X"
        """
        self.check_qubit_input_for_gate(ith_qbit)
       
        if ith_qbit == None:
            self.addToCircuit(self.X_all,name=name)
        elif len(ith_qbit) == 1:
            self.addToCircuit(self.X_2x2,ith_qbit,name=(name+"_"+str(ith_qbit)))
        elif len(ith_qbit) > 1:
            self.addToCircuit(self.X(len(ith_qbit)),ith_qbit[0],name=(name+"_"+str(ith_qbit)))
        
    def z(self,ith_qbit=None,name="Z"):
        """Pauli-X Gate
        Args:
            ith_qbit (nth qubit): ith_qbit (nth qubit): Selects the qubit(s) to be operated on. If None, applies to all qubits. 
            Multiple Qubits can be selected by passing a list of qubits, but the qubits must be adjacent.
            
            name (str): Name of the gate. Default is "Z"
            
        """
        self.check_qubit_input_for_gate(ith_qbit)
        
        for i in ith_qbit:
            self.addToCircuit(self.Z_2x2,i,name=("Z_"+str(i)))
    
    def p(self,ith_qbit,phi=np.pi,name="Phase Shift"):
        """Phase Gate
        Args:
            ith_qbit (nth qubit): ith_qbit (nth qubit): Selects the qubit(s) to be operated on. If None, applies to all qubits. 
            Multiple Qubits can be selected by passing a list of qubits, but the qubits must be adjacent.
            
            name (str): Name of the gate. Default is "Phase"
            
        """
        self.check_qubit_input_for_gate(ith_qbit)
        assert type(ith_qbit) == int or  type(ith_qbit) == list , "Please select a qubit"

        if type(ith_qbit) == int:
            self.addToCircuit(self.P_2x2,ith_qbit,name=("Phase_"+str(ith_qbit)))
        else:
            for i in ith_qbit:
                self.addToCircuit(self.P_2x2,i,name=("Phase_"+str(i)))
    
    def reflect(self,name="Reflection"):
        """Reflection Gate to reflect the state vector about the origin (first qubit).
        Args:
           
            
            name (str): Name of the gate. Default is "Reflection"
            
        """
        

        self.addToCircuit(self.reflection,name=("Reflection"))
    
    def cp(self,control_qbit,target_qbit,phi=np.pi,name="cPhase Shift"):
        """Controlled Phase Gate
        Args:
            ith_qbit (nth qubit): ith_qbit (nth qubit): Selects the qubit(s) to be operated on. Required.
            jth_qbit (nth qubit): Selects the qubit(s) to be operated on. If None, applies to all qubits. Required.
            Phi (float): Phase angle. Default is pi.

        """
        
        self.check_qubit_input_for_cgate(control_qbit,target_qbit)
        assert type(control_qbit) == int, "The control qubit must be an integer."
        

        if type(target_qbit) == list:
            for j in target_qbit:
                if j - control_qbit != 1:
                    self.swap(control_qbit,j)      
                    self.addToCircuit(self.cP(phi),control_qbit,j,name=(name+"_"+str(control_qbit)+"_"+str(target_qbit)))
                    self.unswap(control_qbit,j)
                else:
                    self.addToCircuit(self.cP(phi),control_qbit,j,name=(name+"_"+str(control_qbit)+"_"+str(target_qbit)))
        else:
            if target_qbit - control_qbit != 1:
                    self.swap(control_qbit,target_qbit)      
                    self.addToCircuit(self.cP(phi),control_qbit,j,name=(name+"_"+str(control_qbit)+"_"+str(target_qbit)))
                    self.unswap(control_qbit,target_qbit)
            else:
                    self.addToCircuit(self.cP(phi),control_qbit,target_qbit,name=(name+"_"+str(control_qbit)+"_"+str(target_qbit)))
                    
    def cx(self,control_qbit,target_qbit,name="CX"):
        """Controlled Pauli-X Gate
        Args:
            ith_qbit (nth qubit): ith_qbit (nth qubit): Selects the qubit(s) to be operated on. Required.
            jth_qbit (nth qubit): Selects the qubit(s) to be operated on. If None, applies to all qubits. Required.

        """
        
        self.check_qubit_input_for_cgate(control_qbit,target_qbit)
        assert type(control_qbit) == int, "The control qubit must be an integer. For multiple control qubits, use the toffoli gate(t) or the Multi-Controlled Toffoli(mct) Gate."

        if type(target_qbit) == list:
            for j in target_qbit:
                if j - control_qbit != 1:
                    self.swap(control_qbit+1,j)
                    self.addToCircuit(self.CX_4x4,control_qbit,name=(name+"_"+str(j)))
                    self.unswap(control_qbit+1,j)
                else:
                    self.addToCircuit(self.CX_4x4,control_qbit,name=(name+"_"+str(j)))
        else:
            if target_qbit - control_qbit != 1:
                self.swap(control_qbit+1,target_qbit)
                self.addToCircuit(self.CX_4x4,control_qbit,name=(name+"_"+str(target_qbit)))
                self.unswap(control_qbit+1,target_qbit)
            else:
                self.addToCircuit(self.CX_4x4,control_qbit,name=(name+"_"+str(target_qbit)))
                   
        
    def cz(self,control_qbit,target_qbit):
        """ Controlled Pauli-Z Gate
        Args:
            ith_qbit (nth qubit): ith_qbit (nth qubit): Selects the qubit(s) to be operated on. Required.
            jth_qbit (nth qubit): Selects the qubit(s) to be operated on. If None, applies to all qubits. Required.
        """
        self.check_qubit_input_for_cgate(control_qbit,target_qbit)
        assert type(control_qbit) == int, "The control qubit must be an integer. For multiple control qubits, use the the Multi-Controlled Z(mcz) Gate."

      
        if type(target_qbit) == list:
            for j in target_qbit:
                if j - control_qbit != 1:
                    self.swap(control_qbit+1,j)
                    self.addToCircuit(self.CZ_4x4,control_qbit,name=("CZ_"+str(j)))
                    self.unswap(control_qbit+1,j)
                else:
                    self.addToCircuit(self.CZ_4x4,control_qbit,name=("CZ_"+str(j)))
        else:
            if target_qbit - control_qbit != 1:
                self.swap(control_qbit+1,target_qbit)
                self.addToCircuit(self.CZ_4x4,control_qbit,name=("CZ_"+str(target_qbit)))
                self.unswap(control_qbit+1,target_qbit)
            else:
                self.addToCircuit(self.CZ_4x4,control_qbit,name=("CZ_"+str(target_qbit)))
    
    def swap(self,ith_qbit,jth_qbit,name="Swap"):
        """Swap Gate
        Args:
            ith_qbit (nth qubit): ith_qbit (nth qubit): Selects the qubit(s) to be operated on. Required.
            jth_qbit (nth qubit): Selects the qubit(s) to be operated on. If None, applies to all qubits. Required.
        """
        self.check_qubit_input_for_cgate(ith_qbit,jth_qbit)
        assert type(ith_qbit) and type(jth_qbit) == int, "The qubits must be integers."
       
        self.swap_status.append((ith_qbit,jth_qbit))
        
        if jth_qbit - ith_qbit == 1:
            self.addToCircuit(self.swap_matrix, ith_qbit,name =(name + "({},{})".format(ith_qbit,jth_qbit)))
        else:
            swap,self.unswap_matrix = self.nonadjacent_control(ith_qbit,jth_qbit,unswap=True)
            self.addToCircuit(swap,name =(name + "({},{})".format(ith_qbit,jth_qbit)))
            
    def unswap(self,ith_qbit,jth_qbit,name="Unswap"):
        """Unswap Gate
            Args:
            ith_qbit (nth qubit): ith_qbit (nth qubit): Selects the qubit(s) to be operated on. Required.
            jth_qbit (nth qubit): Selects the qubit(s) to be operated on. If None, applies to all qubits. Required.
        """
        self.check_qubit_input_for_cgate(ith_qbit,jth_qbit)
        assert type(ith_qbit) and type(jth_qbit) == int, "The qubits must be integers."
        assert (ith_qbit,jth_qbit) in self.swap_status, "The qubits must be swapped before unswapping."
        assert (jth_qbit,ith_qbit) in self.swap_status, "The qubits must be swapped before unswapping. Did you mean {} and {}?".format(ith_qbit,jth_qbit)
        
        if jth_qbit - ith_qbit == 1:
            self.addToCircuit(self.swap_matrix, ith_qbit,name =(name + "({},{})".format(ith_qbit,jth_qbit)))
            #remove unswapped qubits from swap_status
            self.swap_status.remove((ith_qbit,jth_qbit))
        else:
            self.addToCircuit(self.unswap_matrix,name =(name + "({},{})".format(ith_qbit,jth_qbit)))
            #remove unswapped qubits from swap_status
            self.swap_status.remove((ith_qbit,jth_qbit))
            
        
 
    def mcz(self,control_qubits,target_qubit,name="MCZ"):
        """Applies a multi-controlled Toffoli gate.
        Args:
            control_qubits (list(int)): List of control qubits
            target_qubit (int): Target qubit
         
       
        """
        self.check_qubit_input_for_cgate(control_qubits,target_qubit)

        assert type(control_qubits) == list, "The control qubits must be a list of integers."
        assert len(control_qubits) > 1, "Must have more than one control qubit"
        assert type(target_qubit) == int, "The target qubit must be an integer."
        assert target_qubit not in control_qubits, "The target qubit cannot be a control qubit."
        assert len(control_qubits) <= self.nqbits, "The number of control qubits must be less than the number of qubits."
        assert self.is_series(control_qubits), "The control qubits must be in adjacent series."
        

        if target_qubit - control_qubits[-1] == 1:
            self.addToCircuit(self.mcZ,control_qubits[0],name=("MCZ_"+str(target_qubit)))
        elif len(control_qubits) == self.nqbits-1:
            self.addToCircuit(self.mcZ,name=("MCZ_"+str(target_qubit)))
        else:
            self.swap(control_qubits[-1]+1,target_qubit)
            self.addToCircuit(self.mcZ,control_qubits,name=("MCZ_"+str(target_qubit)))
            self.unswap(control_qubits[-1]+1,target_qubit)
        
    

    #Internal Methods
    def nonadjacent_swap(self,ith_qbit,jth_qbit):
        """{Internal Method} Creates a swap gate for non-adjacent qubits.
        Args:
            ith_qbit (nth qubit): ith_qbit (nth qubit): Selects the qubit(s) to be operated on. Required.
            jth_qbit (nth qubit): Selects the qubit(s) to be operated on. If None, applies to all qubits. Required.
            unswap (bool): If true, creates an unswap gate.
        """     
        swap = self.create_apply(self.swap_matrix,ith_qbit)
        for j in range(ith_qbit+1,jth_qbit):
            swap = swap @ self.create_apply(self.swap_matrix,j)
    
      
        return swap,inv(swap)
    
    def create_apply(self,gate,ith_qbit):
        """{Internal Method} Creates a gate that applies to a specific qubit.
        Args:
            gate (matrix): Gate to be applied.
            ith_qbit (nth qubit): Selects the qubit(s) to be operated on. Required.
        """
 
        eyeL = eye(2**ith_qbit, dtype=np.complex,format='csr')
        eyeR = eye(2**(self.nqbits - ith_qbit - 2), 
            dtype = np.complex,format='csr')

        # Tensor product of the gate and the identity matrices
        # eyeL ⊗ t ⊗ eyeR
        return kron(kron(eyeL, gate), eyeR)
    
  