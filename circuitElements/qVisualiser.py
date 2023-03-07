from matplotlib import pyplot as plt
import numpy as np

class qVisualiser():
    #good function name for grahm schmidt orthogonalisation
    
    def visualise_state_history(self):
        vectors_i = self.state_history
        vectors = vectors_i[::6] 
        vectors.append(vectors_i[-1])
        vectors = np.asarray(vectors)
        #plt figure size to square
        plt.figure(figsize=(10,10))
        plt.quiver(np.zeros(len(vectors)),np.zeros(len(vectors)),vectors[:,0],vectors[:,1],angles='xy',scale_units='xy',scale=1)
        plt.xlim(-1,1)
        plt.ylim(-1,1)
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
        