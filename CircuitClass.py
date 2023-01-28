#%%
import numpy as np
from art import *
# class for qunatum gates
class QbitRegister:
 
    def __new__(self,qbits_init=[0,0,0],name = "qregister"):
        basisSpace = np.identity(2,dtype = 'complex_')
        qbits = np.take(basisSpace, qbits_init,axis=0)
        tprint("Quantum",font="starwars")
        tprint(" ---------------------------",font="digital")
        print("Quantum Register {} Initialised: |".format(name)+len(qbits_init)*"{}".format(*qbits_init)+">")
        return qbits
        
        
    # def __getitem__(self, qbit):
    #     return self.qbits[qbit]

    # def __str__(self):
    #     return "Quantum Register: \n |{:.0f}> ⊗ |{:.0f}> ⊗ |{:.0f}>".format(*self.qbits[:,1])
    
 
        
class Gate:
   

    @staticmethod 
    def hadamard(qbit,n=(1,)):
        n = slice(*n)
        qbit[n] = qbit[n]@((1/np.sqrt(2))*np.array([[1,1],[1,-1]]))
        return qbit
    @staticmethod
    def phase_shift(qbit,n=(1,),phi=2*np.pi):
        n = slice(*n)
        qbit[n] = qbit[n]@np.round(np.array([[1,0],[0,np.exp(1j*phi)]]))
        
        return qbit
    
    @staticmethod
    def cnot(qbit,target_control=[1,3]):
        #using tensordot right now but will chanhe it later
        return np.tensordot(qbit[target_control[0]-1],qbit[target_control[1]-1],axes=0).flatten()@np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
    
    
# %%
