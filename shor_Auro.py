import cProfile
import numpy as np
from circuitElements.qRegister import QbitRegister
from tqdm import tqdm




def main():
    
    
    def c_amod15(a,power):
        if a not in [2,4,7,8,11,13]:
            raise ValueError("'a' must be 2,4,7,8,11 or 13")
        U = register(4,name="Phase Estimator")
        for _ in range(a):
            if a in [2,13]:
                U.swap(2,3)
                U.swap(1,2)
                U.swap(0,1)
            if a in [7,8]:
                U.swap(0,1)
                U.swap(1,2)
                U.swap(2,3)
            if a in [4, 11]:
                U.swap(1,3)
                U.swap(0,2)
            if a in [7,11,13]:
                for q in range(4):
                    U.x(q)
            
            
    
    
    nqbits = 8
    Uqbits = 4
    register =  QbitRegister(nqbits+Uqbits,name = "SHOR") #initialise qbit register
    
    # Initialize counting qubits
    # in state |+>
    for i in range(nqbits):
        register.hadamard(i+1)
    # And auxiliary register in state |1>
    for i in range(nqbits,nqbits+Uqbits):
        register.x(i+1)
        
    

    

    
    

if __name__ == '__main__':
    # pr = cProfile.Profile()
    # pr.enable()

    main()

    # pr.disable()
    # pr.print_stats(sort='time')
  