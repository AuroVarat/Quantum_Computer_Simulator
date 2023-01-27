#%%
import numpy as np

# class for qunatum gates
class QubitRegister:
 
    def __init__(self,qubits_init=[0,0,0]):
        basisSpace = np.identity(2)
        self.qubits = np.take(basisSpace, qubits_init,axis=0)
        print("Quantum Register: \n |{:.0f}> ⊗ |{:.0f}> ⊗ |{:.0f}> initialised".format(*self.qubits[:,1]))
    def __getitem__(self, qubit):
        return self.qubits[qubit]

    def __repr__(self):
        return "Quantum Register: \n |{:.0f}> ⊗ |{:.0f}> ⊗ |{:.0f}>".format(*self.qubits[:,1])
    
 
        
class Gate:
   
    def __init__(self,size = 2):
        self.size = size
        
        self.hadamard = (1/np.sqrt(2))*np.array([[1,1],[1,-1]])
        self.phase_shift = lambda phi : np.round(np.array([[1,0],[0,np.exp(1j*phi)]]))
    
    
    
# %%
