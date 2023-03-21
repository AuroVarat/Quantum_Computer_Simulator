"""
Qbit Visualiser Class has methods to visualise the state of a quantum register.
"""
"""
Title: Qbit Visualiser Class
Author: Auro Varat Patnaik
Date: 2023-03-07
Code version: 3.0

"""
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
import matplotlib.cm as cm

class qVisualiser():
    """ Qbit Visualiser Class has methods to visualise the state of a quantum register.
    """
    def visualise_state_history(self):
        """Plots the state history of the quantum register as a quiver plot.
        """
        assert len(self.state_history) > 0, "No state history to visualise"
        vectors_i = self.state_history
        #save the state history using np.savetxt
       
   
        vectors = vectors_i[::1] 
      
        vectors = np.asarray(vectors)
        #plt figure size to square
        colors = np.arctan2(vectors[:,0],vectors[:,1])

        norm = Normalize()
        norm.autoscale(colors)
        # we need to normalize our colors array to match it colormap domain
        # which is [0, 1]

        colormap = cm.inferno

        plt.figure(figsize=(10,10))
        plt.quiver(np.zeros(len(vectors)),np.zeros(len(vectors)),vectors[:,0],vectors[:,1], color=colormap(norm(colors)),angles='xy',scale_units='xy',scale=1,alpha=0.7)
        plt.xlim(-1,1)
        plt.ylim(-1,1)
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
      
        plt.xlabel("s'")
        plt.ylabel("w")
        plt.title("Evolution of Basis State of Qubits")
        plt.savefig("./output/{}_state_reflections.png".format(self.name))
        plt.close()
        
    
    def visualise_probability(self):
        """Visualises the quantum register in the basis space using matplotlib bar chart"""
     
        if self.nqbits > 4:
            print("Warning: Too many qbits for a pretty visualising")
      
        plt.bar([format(i, f'0{self.nqbits}b') for i in range(self.N)],self.basisSpace.real**2)
        #make bar y label rotation 90

        plt.xticks(rotation=90)
        plt.ylabel("Proabability")
        plt.xlabel("State")
        plt.savefig("./output/{}_probability.png".format(self.name))
        plt.close()
        
    def visualise_marked_state(self):
        """Visualises the marked state in the basis space using matplotlib bar chart"""
        assert self.marked_state_history != [], "No marked state history to visualise"
       
        plt.plot(np.asarray(self.marked_state_history)**2)
        plt.title("Probability amplitude of a fixed target state for {} qubits register".format(self.nqbits))
        plt.ylabel("Proabability Amplitude")
        plt.xlabel("Iteration")
        plt.savefig("./output/{}_marked_state.png".format(self.name))
        plt.close()
        