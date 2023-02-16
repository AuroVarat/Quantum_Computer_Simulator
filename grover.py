import cProfile
import numpy as np
from circuitElements.qRegister import QbitRegister
from tqdm import tqdm

def main():
    #%%
    dictionary = np.genfromtxt('dictionary.txt',dtype=str)
  

    #%%
    # Simple Grover's Algorithm #ha
    register = QbitRegister(13,name = "GROVER") #initialise qbit register
    register.grover_dict_search(dataset = dictionary,target="atoms")
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
  