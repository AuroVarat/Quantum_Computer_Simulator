import cProfile
import numpy as np
from circuitElements.qRegister import QbitRegister
from tqdm import tqdm

accuracy = 0.90


def main():
    #Load Dictionary dataset
    dictionary = np.genfromtxt('dictionary.txt',dtype=str)

    
    register = QbitRegister(13,name = "GROVER") #initialise qbit register
    register.hadamard() #apply hadamard gate to all qbits
    register.dict_search_oracle_init(dataset = dictionary,target="atoms")
    
    for _ in tqdm(range(register.number_of_rotation())):
        register.oracle()
        register.hadamard()
        register.control_phase_shift(except_state=1,phi=np.pi)
        register.hadamard()
        
        if np.max(register.basisSpace.real) > accuracy:
            break
 
        
   

    #%%
    print("Found word: '{}' at position {} in the dictionary of five words".format(dictionary[np.argmax(register.basisSpace.real)],np.argmax(register.basisSpace.real)))
    register.visualise()
    #%%

if __name__ == '__main__':
    # pr = cProfile.Profile()
    # pr.enable()
    main()
    # pr.disable()
    # pr.print_stats(sort='time')
  