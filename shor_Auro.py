import cProfile
import numpy as np
from circuitElements.qRegister import QbitRegister
from tqdm import tqdm




def main():
      
    nqbits = 8
    Uqbits = 4
    
    def c_amod15(a,power):
        if a not in [2,4,7,8,11,13]:
            raise ValueError("'a' must be 2,4,7,8,11 or 13")
        U = register(4,name="Phase Estimator")
        
        
        for _ in range(power):
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
                for q in range(Uqbits):
                    U.x(q)
            
            
    
  
    register =  QbitRegister(nqbits+Uqbits,name = "SHOR") #initialise qbit register
    
    # Initialize counting qubits
    # in state |+>
    for i in range(1,nqbits+1):
        register.hadamard(i)
    # And auxiliary register in state |1>
    for i in range(nqbits+1,nqbits+Uqbits+1):
        register.x(i)
        
    #controlled U operations
    for i in range(1,nqbits+1):
        c_amod15(7,i)


    

    
    

if __name__ == '__main__':
    # pr = cProfile.Profile()
    # pr.enable()

    main()

    # pr.disable()
    # pr.print_stats(sort='time')
  