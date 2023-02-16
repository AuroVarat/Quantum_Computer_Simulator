import cProfile
import numpy as np
from circuitElements.qRegister import QbitRegister
from tqdm import tqdm


def main(N):
    register =  QbitRegister(3,name = "SHOR") #initialise qbit register

    
    

if __name__ == '__main__':
    # pr = cProfile.Profile()
    # pr.enable()

    main(200)

    # pr.disable()
    # pr.print_stats(sort='time')
  