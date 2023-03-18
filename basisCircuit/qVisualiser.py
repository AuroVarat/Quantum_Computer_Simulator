from matplotlib import pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
import matplotlib.cm as cm

class qVisualiser():
    #good function name for grahm schmidt orthogonalisation
    
    def visualise_state_history(self):
        vectors_i = self.state_history
        #save the state history using np.savetxt
       
   
        vectors = vectors_i[::8] 
      
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
        plt.savefig("./state_reflections.png")
        plt.close()
        
    
    def visualise_basisSpace(self):
        """Visualises the quantum register in the basis space using matplotlib bar chart"""
        plt.plot(self.basisSpace.real)
        # plt.bar([format(i, f'0{self.nqbits}b') for i in range(self.N)],self.basisSpace.real)
        plt.ylabel("Proabability")
        plt.xlabel("State")
        plt.savefig("./dict.png")
        plt.close()
    def visualise_marked_state(self):
        print(self.marked_state_history)
        plt.plot(self.marked_state_history)
        plt.ylabel("Proabability")
        plt.xlabel("Iteration")
        plt.savefig("./marked_state.png")
        plt.close()
        