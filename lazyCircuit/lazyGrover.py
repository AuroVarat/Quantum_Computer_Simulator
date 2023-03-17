from lazyRegister import QbitRegister
import numpy as np
import inspect
from scipy.sparse import diags,identity,eye
from scipy.linalg import hadamard

isq2 = 1/np.sqrt(2) # 1/sqrt(2)isq2 = 1/np.sqrt(2) # 1/sqrt(2)


from tqdm import tqdm
from matplotlib import pyplot as plt

nqubits = 12
max_dataset_size = 2**nqubits
dataset_size = 2**nqubits
assert dataset_size <= max_dataset_size, "dataset size must be less than or equal to 2**nqbits"
def main():
    #%%
    
    
    dataset = np.ones(dataset_size)
    target = np.random.randint(0,dataset_size)
    dataset[target] = -1
    oracle   = diags(dataset)
   
    # dataset = np.genfromtxt("b.txt")
        
    register = QbitRegister(nqubits)
    register.hadamard()



    for _ in tqdm(range(register.rotations)):
        register.customGate(oracle,name="Oracle")
        register.hadamard()
        register.control_phase_shift(except_state=1,phi=np.pi)
        register.hadamard()




    register.measure(amax=True)
    


    #%%

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
  