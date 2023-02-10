import cProfile
import numpy as np
from circuitElements.qRegister import QbitRegister
from tqdm import tqdm
def main():
    #%%
 

    #%%
    # Simple Grover's Algorithm #ha
    register = QbitRegister(13, name = "SampleHadamardOperation") #initialise qbit register
    register.hadamard() # apply hadamard gate to register 
    def grover_iterate():

        register.oracle(winner=4) # apply oracle gate to qbit 1 and 2
        register.hadamard() # apply hadamard gate to the register
        register.control_phase_shift(except_state=1,phi=np.pi) #apply phase shift to qbit 2
        register.hadamard() # apply hadamard gate to qbit 1

    for i in tqdm(range(100)):
        grover_iterate()
        if np.max(register.basisSpace.real) > 0.9:
            break
    #%%

    print(np.amax(register.output()))
    #%%

if __name__ == '__main__':
    pr = cProfile.Profile()
    pr.enable()

    main()

    pr.disable()
    pr.print_stats(sort='time')
  