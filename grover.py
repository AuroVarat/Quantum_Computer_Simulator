import cProfile
import numpy as np
from circuitElements.qRegister import QbitRegister
from tqdm import tqdm
from matplotlib import pyplot as plt

nqbits = 3
max_dataset_size = 2**nqbits
dataset_size = 2**nqbits
assert dataset_size <= max_dataset_size, "dataset size must be less than or equal to 2**nqbits"
def main():
    #%%
    
    

    # dataset = np.random.randint(0,10,dataset_size)
    dataset = np.arange(0,dataset_size)
    target = np.random.randint(0,dataset_size)
    
    # dataset = np.genfromtxt("b.txt")
    


    #%%
    # Simple Grover's Algorithm #ha
    register = QbitRegister(nqbits,name = "GROVER") #initialise qbit register
  
    # register.hadamard() #apply hadamard to all qbits
    
    # register.z(1)
    # register.hadamard(1)
 
   
  
    register.grover_search(dataset=dataset,target=target)

    # print(np.linalg.norm(register.basisSpace.real))
    # print(register.basisSpace.real[register.basisSpace.real > 0.])
    
    #print("target found" if np.argmax(register.basisSpace.real) == target else "target not found")
    # turn a numy array into a square matrix
    # plt.plot(np.abs(register.basisSpace.real))
    # plt.savefig("result.png")
    #%%

if __name__ == '__main__':
    # pr = cProfile.Profile()
    # pr.enable()

    main()

    # pr.disable()
    # pr.print_stats(sort='time')
  