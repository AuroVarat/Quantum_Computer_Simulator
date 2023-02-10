#%%
from circuitElements.qGate import SingleQbitGate,TwoQbitGate,MultiQbitGate
import numpy as np
from art import *
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("white")
isq2 = 1/np.sqrt(2) # 1/sqrt(2)


class QbitRegister(SingleQbitGate,TwoQbitGate,MultiQbitGate):
  
    """
    Qbit Register Class initialises a quantum register with nqbits qbits and initialises all qbits to |0>l,
    and contains methods to apply gates to the qbits in the register. 
    """
 
    def __init__(self,nqbits=2,name = "qregister"):
        """Defines a Quantum Register with nqbits qbits and initialises all qbits to |0>.
        The Quantum Register is represented by a vector in the 2^nqbits dimensional basis space, i.e. the Hilbert Spac of the nqbits.

        Args:
            nqbits (int, optional): Number of Qbits in the Quantum Register. Defaults to 2.
            name (str, optional): Label of the register. Defaults to "qregister".
        """
        
        self.nqbits = nqbits
        self.N = 2**self.nqbits
        self.basisSpace = np.zeros(2**self.nqbits, dtype=np.int) #  basis state formed by tensor product of all qbits
        self.basisSpace[0] = 1 #all qbits are by default initialised to |0>
       
        #Pretty printing showing the initialisation of the quantum register
        tprint("Quantum",font="starwars")
        tprint(" ---------------------------",font="digital")
        tprint("Quantum Register {} Initialised: |".format(name)+nqbits*"0"+">",font="monospace")
        tprint(" ---------------------------",font="monospace")
        
    def __str__(self):
        """Prints the quantum register in the basis space
        """
        tprint(str(self.basisSpace.real)+"\n",font="monospace")
        return "Register in the {} dimension basis space.\n".format(self.nqbits)

    def output(self):
        """Prints the quantum register in the basis space and returns the circuit output
        Returns:
            (Numpy Array): Hilbert Space of the quantum register, post circuit operation.
   
        """
        tprint(str(self.basisSpace.real)+"\n",font="monospace")
        return self.basisSpace
  
    def visualise(self):
        """Visualises the quantum register in the basis space using matplotlib bar chart"""

        plt.bar([format(i, f'0{self.nqbits}b') for i in range(self.N)],self.basisSpace.real)
        plt.ylabel("Proabability")
        plt.xlabel("State")
        plt.show()
   

    # Oracles
    def oracle(self, winner = 4):
        """" this is the oracle function that performs a conditional phase shift for the item we're looking for  """
    


        oracle_matrix = np.eye(self.N)
        oracle_matrix[winner-1, winner-1] = -1  # flip sign of entry corresponding to w
        # is a sparse matrix, make it faster

        # Apply the gate
        self.basisSpace = np.matmul(oracle_matrix, self.basisSpace)
        

       
       
       
       
       
       
       
       
       
        
  

   

# %%
