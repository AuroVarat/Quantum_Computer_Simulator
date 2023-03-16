#%%
from circuitElements.qGate import SingleQbitGate,TwoQbitGate,MultiQbitGate
from circuitElements.qVisualiser import qVisualiser
import numpy as np
from art import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation 
from tqdm import tqdm
# import seaborn as sns
# sns.set_style("white")
isq2 = 1/np.sqrt(2) # 1/sqrt(2)


class QbitRegister(SingleQbitGate,TwoQbitGate,MultiQbitGate,qVisualiser):
  
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
        self.basisSpace = np.zeros(2**self.nqbits, dtype=int) #  basis state formed by tensor product of all qbits
        self.basisSpace[0] = 1 #all qbits are by default initialised to |0>
        self.rotations = int(np.ceil((((np.pi/2)/np.arcsin(1/np.sqrt(self.N)))-1)/2)) #set to optimum
        
        
        self.state_history = []
        self.marked_state_history = []
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
  
  
    
    def f(self,x):
        return (x == self.target).any(axis=1)
    
    # Oracles
    def applyOracle(self):
        """" this is the oracle function that performs a conditional phase shift for the item we're looking for  """
  
        self.basisSpace = np.matmul(self.oracle_matrix, self.basisSpace)
        
    def create_oracle_matrix(self,dataset):
       
        oracle_values = np.power(-1, self.f(dataset))
      
        oracle_values = np.pad(oracle_values,(0,self.N-len(oracle_values)),'constant',constant_values=(1))
        
        
        self.target_basis_Space = (oracle_values == -1)
        self.oracle_matrix = np.diag(oracle_values) # make a diagonal matrix with the oracle values 
        
    def Gram_Schmidt(self):
        a = self.target_basis_Space
       
        self.s_prime = self.basisSpace.real # initial vector with s
        self.s_prime -=  np.dot(self.s_prime,a)/np.dot(a,a)*a
        self.s_prime = self.s_prime/np.linalg.norm(self.s_prime)
        
    def state_vector_projection(self):
        w = self.target_basis_Space
        s = self.basisSpace.real
        
        x = np.dot(s,self.s_prime)
        y = np.dot(s,w)
        
        self.state_history.append([x,y])
        

        
    def grover_search(self,dataset,target,accuracy=1.0):
        
        self.target = target
 
        self.datasetSmall = dataset.shape[0]

        self.create_oracle_matrix(dataset)
        #self.marked_state_history.append(self.basisSpace.real[self.target_basis_Space])

        # frames = [] # for storing the generated images
        # fig = plt.figure()
        # width = int(np.sqrt(self.datasetSmall))
        self.hadamard() # apply hadamard gate to register
        #frames.append([plt.imshow(self.basisSpace[:self.datasetSmall].real.reshape(width,width),animated=True,vmin=0,vmax = .1 )])
        #plt.colorbar()
        self.Gram_Schmidt()
        self.state_vector_projection()
        #self.marked_state_history.append(self.basisSpace.real[self.target_basis_Space])
        def grover_iterate():
       
            self.applyOracle() # apply oracle gate to qbit 1 and 2
            self.hadamard() # apply hadamard gate to the register
            self.control_phase_shift(except_state=1,phi=np.pi) #apply phase shift to qbit 2
            self.hadamard() # apply hadamard gate to qbit 1
            #self.marked_state_history.append(self.basisSpace.real[self.target_basis_Space])
            self.state_vector_projection()
            #frames.append([plt.imshow(self.basisSpace[:self.datasetSmall].real.reshape(width,width),animated=True,vmin=0,vmax = .1)])
        
        for _ in tqdm(range(self.rotations)):
            grover_iterate()
            
            # if np.max(self.basisSpace.real) > accuracy:
                
            #     break
        # ani = animation.ArtistAnimation(fig, frames, interval=1000, blit=True,
        #                       )
        # ani.save("result.mp4")
        # np.savetxt("./state_history.txt",np.c_[self.state_history],delimiter=",")
  
       
   
       
       
       
       
       
        
  

   

# %%
