import cProfile
import numpy as np
from circuitElements.qRegister import QbitRegister
from tqdm import tqdm
def main():
    #%%
    all_5_letter_words = np.genfromtxt('dictionary.txt',dtype=str)
    all_5_letter_words=np.pad(all_5_letter_words,(0,(2**13)-all_5_letter_words.size),mode='constant',constant_values=' ') #blank words to fill up the rest of the register states
    print(all_5_letter_words.shape)
    #%%
    # Simple Grover's Algorithm #ha
    register = QbitRegister(13, dataset = all_5_letter_words,target="atoms",name = "GROVER") #initialise qbit register
    register.hadamard() # apply hadamard gate to register 
    def grover_iterate():

        register.oracle() # apply oracle gate to qbit 1 and 2
        register.hadamard() # apply hadamard gate to the register
        register.control_phase_shift(except_state=1,phi=np.pi) #apply phase shift to qbit 2
        register.hadamard() # apply hadamard gate to qbit 1

    for i in tqdm(range(100)):
        grover_iterate()
        if np.max(register.basisSpace.real) > 0.9:
            break
    #%%
    print("Found word: '{}' at position {} in the dictionary of five words".format(all_5_letter_words[np.argmax(register.basisSpace.real)],np.argmax(register.basisSpace.real)))
    register.visualise()
    #%%

if __name__ == '__main__':
    pr = cProfile.Profile()
    pr.enable()

    main()

    pr.disable()
    pr.print_stats(sort='time')
  